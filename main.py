# -*- coding: utf-8 -*-
#!/usr/local/bin/env python3

#fuzzy as hell, I hope that no one ever would find this piece of code

import pylast
import sys

API_KEY = "API_KEY"
API_SECRET = "API_SECRET"

username = "username"
password_hash = pylast.md5("password")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

user = network.get_user(username)

#temporal unicode printer
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def main():
  library = user.get_library()
  artists = library.get_artists(limit=50)
  for item in artists:
    uprint(item[0])


if __name__ == '__main__':
  main()