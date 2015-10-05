#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys  
import re
import urllib2
import json
import csv
import codecs
import os
import socket
from socket import AF_INET, SOCK_DGRAM

def load_credentials():
    lines = [line.rstrip('\n') for line in open('credentials.ini')]
    chars_to_strip = " \'\""
    for line in lines:
        if "client_id" in line:
            client_id = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
        if "client_secret" in line:
            client_secret = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
        #Currently only need access token to run, the other two perhaps for future implementation
        if "client_access_token" in line:
            client_access_token = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
    return client_id, client_secret, client_access_token

def setup(search_term):
    reload(sys) #dirty (but quick) way to deal with character encoding issues in Python2; if writing for Python3, should remove
    sys.setdefaultencoding('utf8')
    if not os.path.exists("output/"):
        os.makedirs("output/")    
    outputfilename = "output/output-" + re.sub(r"[^A-Za-z]+", '', search_term) + ".csv"
    with codecs.open(outputfilename, 'ab', encoding='utf8') as outputfile:
        outwriter = csv.writer(outputfile)
        if os.stat(outputfilename).st_size == 0:
            header = ["page","id","title","url","path","header_image_url","annotation_count","pyongs_count","primaryartist_id","primaryartist_name","primaryartist_url","primaryartist_imageurl"]
            outwriter.writerow(header)
            return outputfilename
        else:
            return outputfilename
    
def search(search_term,outputfilename,client_access_token):
    with codecs.open(outputfilename, 'ab', encoding='utf8') as outputfile:
        outwriter = csv.writer(outputfile)
        #Unfortunately, looks like it maxes out at 50 pages (approximately 1,000 results), roughly the same number of results as displayed on web front end
        page=1
        while True:
            querystring = "http://api.genius.com/search?q=" + urllib2.quote(search_term) + "&page=" + str(page)
            request = urllib2.Request(querystring)
            request.add_header("Authorization", "Bearer " + client_access_token)   
            request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)") #Must include user agent of some sort, otherwise 403 returned
            while True:
                try:
                    response = urllib2.urlopen(request, timeout=4) #timeout set to 4 seconds; automatically retries if times out
                    raw = response.read()
                except socket.timeout:
                    print("Timeout raised and caught")
                    continue
                break
            json_obj = json.loads(raw)
            body = json_obj["response"]["hits"]

            num_hits = len(body)
            if num_hits==0:
                if page==1:
                    print("No results for: " + search_term)
                break      
            print("page {0}; num hits {1}".format(page, num_hits))
            
            for result in body:
                result_id = result["result"]["id"]
                title = result["result"]["title"]
                url = result["result"]["url"]
                path = result["result"]["path"]
                header_image_url = result["result"]["header_image_url"]
                annotation_count = result["result"]["annotation_count"]
                pyongs_count = result["result"]["pyongs_count"]
                primaryartist_id = result["result"]["primary_artist"]["id"]
                primaryartist_name = result["result"]["primary_artist"]["name"]
                primaryartist_url = result["result"]["primary_artist"]["url"]
                primaryartist_imageurl = result["result"]["primary_artist"]["image_url"]
                row=[page,result_id,title,url,path,header_image_url,annotation_count,pyongs_count,primaryartist_id,primaryartist_name,primaryartist_url,primaryartist_imageurl]
                outwriter.writerow(row) #write as CSV
            page+=1

arguments = sys.argv[1:] #so you can input searches from command line if you want
search_term = arguments[0].translate(None, "\'\"")
outputfilename = setup(search_term)
client_id, client_secret, client_access_token = load_credentials()
search(search_term,outputfilename,client_access_token)
