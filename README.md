# genius-lyrics-search
A quick and dirty Python script for searching lyrics/artists/songs on [https://api.genius.com](https://api.genius.com), parsing the returned JSON, and outputting it in a CSV file.

## Requirements and Setup
Written for Python 2.7 (but could be tweaked for Python 3 pretty easily). Requires a client access token from Genius.com: [https://genius.com/api-clients](https://genius.com/api-clients). (Maybe in future will generate authentication from client_id and client_secret.) Add access token credential to "credentials.ini" in project root folder
```python
client_access_token = 'fillinyourtokenhere'
```
Script passes the access token in a request header as specified in [Genius documentation: Using An Access Token](https://docs.genius.com/#/using-an-access-token).

## Run
```python
python search.py 'search terms here'
```
or if using as imported function
```python
search(search_term,outputfilename,client_access_token)
```

##Limitations/to-do
* Only gets 50 pages worth of results (approximately 1000 results). Appears to be a restriction on Genius' end.
* Currently searches not just lyrics for search term, but also song titles and artist names.
* No way to differentiate between genres or between lyrics vs. text content (e.g. speeches, interviews, magazine articles, books)?
* This was just for fun!

##Sample output
First ten results for search for `albee square` [(web search)](http://genius.com/search?q=albee+square)

 page | id | title | url | path | header_image_url | annotation_count | pyongs_count | primaryartist_id | primaryartist_name | primaryartist_url | primaryartist_imageurl 
------|--------|--------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------------|------------------|--------------|------------------|----------------------|------------------------------------------------|------------------------------------------------------------------------------
 1 | 10388 | Albee Square Mall | http://genius.com/Biz-markie-albee-square-mall-lyrics | /Biz-markie-albee-square-mall-lyrics | https://assets.rapgenius.com/images/default_cover_image.png?1442605042 | 1 | | 26362 | Biz Markie | http://genius.com/artists/Biz-markie | http://images.rapgenius.com/306441a47d61f6f0573172b900c3387e.350x350x1.jpg 
 1 | 582565 | Albee Square Mall | http://genius.com/Skyzoo-and-torae-albee-square-mall-lyrics | /Skyzoo-and-torae-albee-square-mall-lyrics | http://images.rapgenius.com/208ff1c245122e3ddc378e1c4e1d09e7.316x316x1.jpg | 1 | | 211611 | Skyzoo & Torae | http://genius.com/artists/Skyzoo-and-torae | http://bringingdowntheband.com/wp-content/uploads/2014/05/Torae-Skyzoo-1.jpg 
 1 | 136493 | Definition Of A Rap Flow | http://genius.com/Ra-the-rugged-man-definition-of-a-rap-flow-lyrics | /Ra-the-rugged-man-definition-of-a-rap-flow-lyrics | http://s3.amazonaws.com/rapgenius/220px-Legends_Never_Die_cover.jpg | 1 | 13 | 320 | R.A. The Rugged Man | http://genius.com/artists/Ra-the-rugged-man | http://s3.amazonaws.com/rapgenius/R_A__the_Rugged_Man_by_Gainrrom.jpg 
 1 | 236 | Hello Brooklyn 2.0 | http://genius.com/Jay-z-hello-brooklyn-20-lyrics | /Jay-z-hello-brooklyn-20-lyrics | http://s3.amazonaws.com/rapgenius/1313160888_220px-JayZ_American_Gangster_Cover.jpg | 1 | 5 | 2 | Jay Z | http://genius.com/artists/Jay-z | http://images.rapgenius.com/0d53c56a247ef39e4106718deb95f347.1000x500x1.jpg 
 1 | 1705 | Return of the Crooklyn Dodgers | http://genius.com/The-crooklyn-dodgers-return-of-the-crooklyn-dodgers-lyrics | /The-crooklyn-dodgers-return-of-the-crooklyn-dodgers-lyrics | http://images.rapgenius.com/d3e0fd1b9ceea7995279034310c0480c.600x600x1.jpg | 1 | 3 | 861 | The Crooklyn Dodgers | http://genius.com/artists/The-crooklyn-dodgers 
 1 | 3502 | Motherless Child | http://genius.com/Ghostface-killah-motherless-child-lyrics | /Ghostface-killah-motherless-child-lyrics | http://s3.amazonaws.com/rapgenius/220px-SunsetPark-Soundtrack.jpg | 1 | 2 | 20 | Ghostface Killah | http://genius.com/artists/Ghostface-killah | http://images.rapgenius.com/227de22e535416c2ec2a6f012f37c9ef.620x400x1.jpg 
 1 | 9435 | Hey Fuck You | http://genius.com/Beastie-boys-hey-fuck-you-lyrics | /Beastie-boys-hey-fuck-you-lyrics | http://images.rapgenius.com/b9e5dde07b233ec5f15e77eb14777437.400x400x1.jpg | 1 | | 329 | Beastie Boys | http://genius.com/artists/Beastie-boys | http://images.rapgenius.com/28a945e64fc4b3c0e6ce96486f6e4df3.450x450x1.jpg 
 1 | 104 | Angelz | http://genius.com/Mf-doom-angelz-lyrics | /Mf-doom-angelz-lyrics | http://s3.amazonaws.com/rapgenius/1365973654_Born-like-this.jpg | 1 | 1 | 70 | MF DOOM | http://genius.com/artists/Mf-doom | http://s3.amazonaws.com/rapgenius/mf%20doom_jpg_630x420_q85.jpg 
 1 | 21391 | The Mall | http://genius.com/Gang-starr-the-mall-lyrics | /Gang-starr-the-mall-lyrics | http://s3.amazonaws.com/rapgenius/1361526754_Gang-Starr-Moment-Of-Truth.jpg | 1 | 1 | 220 | Gang Starr | http://genius.com/artists/Gang-starr | http://s3.amazonaws.com/rapgenius/gang-starr-dj-premier-guru.jpg 
