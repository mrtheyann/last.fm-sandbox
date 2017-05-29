# -*- coding: utf-8 -*-
#!/usr/local/bin/env python3

#fuzzy as hell, I hope that no one ever would find this piece of code
#Once I commit in this repo just for a green square in github while ending up a semester in university. I still feel uncomfortable about this

import pylast
import sys
import csv

API_KEY = "API_KEY"
API_SECRET = "API_SECRET"

username = "username"
password_hash = pylast.md5("password")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

user = network.get_user(username)

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):

  '''
  Temporal unicode printer for windows console
  '''

    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def get_artists(limit=None):
  
  '''
  Write first N artists sorted by playcount in a csv file
  '''

  if limit is not None:
    limit = int(limit)

  library = user.get_library()
  artists = library.get_artists(limit=limit)
  
  with open('Artists.csv', 'w+', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    
    for item in artists:
      writer.writerow(item)
    
    csv_file.close()

def get_artist_tracks(artist, limit=None):

  '''
  Write first N tracks of artist sorted by popularity in a csv file
  '''

  tracks = artist.get_top_tracks()

  if limit is not None:
    limit = int(limit)

  with open('TopTracks{0}.csv'.format(artist), 'w+', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    for track in tracks:
      writer.writerow(track)

    csv_file.close()


def main():
  if len(sys.argv) < 2:
    get_artists()
  else:
    get_artists(sys.argv[1])

if __name__ == '__main__':
  main()
