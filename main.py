# -*- coding: utf-8 -*-
#!/usr/local/bin/env python3

import pylast
import sys
import csv
import os

API_KEY = "API_KEY"
API_SECRET = "API_SECRET"

username = "username"
password_hash = pylast.md5("password")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

user = network.get_user(username)


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


def get_artist_tracks(name, limit=None):

  '''
  Write first N tracks of artist sorted by popularity in a csv file
  '''

  artist = network.get_artist(name)

  tracks = artist.get_top_tracks(limit=limit)

  if limit is not None:
    limit = int(limit)

  with open('output/TopTracks_{0}.csv'.format(artist), 'w+', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    for track in tracks:
      writer.writerow(track)

    csv_file.close()


def parse_artists(filename='Artists.csv'):

  '''
  Get names of artists from user's csv file
  '''

  artists = []

  with open(filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    for item in reader:
      artists.append(item[0])

    csv_file.close()

  return artists

def main():
  
  '''
  Entry point. Currently fuzzy and non-sense.
  Yet, you can get artists or top tracks.
  '''

  if not os.path.exists('Artists.csv'):
    get_artists()
  else:
    dataset = parse_artists()

    for data in dataset:
      print(data)
      get_artist_tracks(data, 10)

  '''
  if len(sys.argv) < 2:
    #get_artists()
    get_artist_tracks(sys.argv[1])
  else:
    #get_artists(sys.argv[1])
    get_artist_tracks(sys.argv[1], sys.argv[2])
  '''

if __name__ == '__main__':
  main()
