#!/usr/local/bin/env python3

import pylast
import sys

API_KEY = "api_key"
API_SECRET = "api_secret"

username = "your_user_name"
password_hash = pylast.md5("your_password")


network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)


def get_tracks(username):
  user = network.get_user(username)
  return user.get_recent_tracks(limit=50, cacheable=True)


def main():
  tracks = get_tracks(sys.argv[1])
  print(tracks)


if __name__ == '__main__':
  main()