# genius-lyrics-search

## What
A quick and dirty Python script for searching for lyrics/artists/songs from [api.genius.com](api.genius.com), parsing the returned JSON, and outputting it in a CSV file.

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

##Limitations/to-do
* Only gets 50 pages worth of results (approximately 1000 results). Appears to be a restriction on Genius' end.
* Currently searches not just lyrics for search term, but also song titles and artist names.
* No way to differentiate between genres or between lyrics vs. text content (e.g. speeches, interviews, magazine articles, books)?
* This was just for fun!