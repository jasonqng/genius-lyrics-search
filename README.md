# genius-lyrics-search

## What
A quick and dirty Python script for searching for lyrics/artists/songs from [https://api.genius.com](https://api.genius.com), parsing the returned JSON, and outputting it in a CSV file.

## Setup
Requires a client access token from Genius.com: [https://genius.com/api-clients](https://genius.com/api-clients). (Maybe in future will generate authentication from client_id and client_secret.) Add access token credential to "credentials.ini" in project root folder
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

##Sample output
Search for "citibank"
| page | id | title | url | path | header_image_url | annotation_count | pyongs_count | primaryartist_id | primaryartist_name | primaryartist_url | primaryartist_imageurl | 
|------|--------|------|------------|----------|-------------|--------|--------|-------|---------|-------|----------| 
| 1 | 541678 | Q3 2014 Earnings Call Transcript | http://genius.com/Citibank-q3-2014-earnings-call-transcript-annotated | /Citibank-q3-2014-earnings-call-transcript-annotated | https://assets.rapgenius.com/images/default_cover_image.png?1442603759 | 1 | | 240779 | Citibank | http://genius.com/artists/Citibank | | 
| 2 | 240192 | ???€???????? ???€???????? (Proliv Dreyka) | http://genius.com/Oxxxymiron-proliv-dreyka-lyrics | /Oxxxymiron-proliv-dreyka-lyrics | https://assets.rapgenius.com/images/default_cover_image.png?1442603759 | 1 | 9 | 24422 | Oxxxymiron | http://genius.com/artists/Oxxxymiron | | 
| 2 | 390787 | Short Skirt/Long Jacket | http://genius.com/Cake-short-skirt-long-jacket-lyrics | /Cake-short-skirt-long-jacket-lyrics | https://assets.rapgenius.com/images/default_cover_image.png?1442603759 | 1 | 13 | 38835 | Cake | http://genius.com/artists/Cake | | 
| 2 | 74178 | Showtime | http://genius.com/Kollegah-showtime-lyrics | /Kollegah-showtime-lyrics | http://images.rapgenius.com/f0f0e1710e64c8fd072ea0f915083f91.808x606x1.jpg | 1 | 1 | 12077 | Kollegah | http://genius.com/artists/Kollegah | http://images.rapgenius.com/6a655eac4bd6898eb3a7a30dbf0ad7b5.500x417x1.png | 
| 2 | 140760 | Mistaken for Strangers | http://genius.com/The-national-mistaken-for-strangers-lyrics | /The-national-mistaken-for-strangers-lyrics | http://images.rapgenius.com/ba70cff41fe06c384c384481e3caf9b0.400x400x1.jpg | 1 | 5 | 658 | The National | http://genius.com/artists/The-national | http://s3.amazonaws.com/rapgenius/national-album-tour-2010.jpg |

##Limitations/to-do
* Only gets 50 pages worth of results (approximately 1000 results). Appears to be a restriction on Genius' end.
* Currently searches not just lyrics for search term, but also song titles and artist names.
* No way to differentiate between genres or between lyrics vs. text content (e.g. speeches, interviews, magazine articles, books)?
* This was just for fun!
