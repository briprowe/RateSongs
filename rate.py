#!/usr/bin/end python

# Copyright (C) 2011 by Brian Rowe

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import keybinder, gtk, sys

from banshee import current_track, get_rating, set_rating
from notify import Notify

MAX_RATING = 5
MIN_RATING = 0

def song_string(track):
    msg = str(track['name'])
    msg += ' on ' + str(track['album'])
    msg += ' by ' + str(track['artist'])

    return msg

def clamp(rating):
    if rating > MAX_RATING:
        rating = MAX_RATING
    elif rating < MIN_RATING:
        rating = MIN_RATING

    return rating

def bind(key, fun):
    if not keybinder.bind(key, fun):
        sys.stderr.write('Could not bind: ' + key)
        return False
    return True

class RateSong(object):
    def __init__(self):
        self.n = Notify()

        for x in range(1,6):
            key = '<ctrl>F' + str(x)
            if not bind(key, lambda y=x: self.rate(y)):
                exit(1)

        if not bind('<ctrl>F6', self.show):
            exit(1)
        if not bind('<ctrl>F7', self.decr):
            exit(1)
        if not bind('<ctrl>F8', self.incr):
            exit(1)

    def rate(self, n):
        rating = get_rating()
        set_rating(clamp(n))
        track = current_track()

        song = song_string(track)

        self.n.update(song, rating)
        self.n.change_stars(n)

    def decr(self):
        rating = get_rating()
        new_rating = clamp(rating - 1)

        set_rating(new_rating)
        
        song = song_string(current_track())

        self.n.update(song, rating)
        self.n.change_stars(new_rating)

    def incr(self):
        rating = get_rating()
        new_rating = clamp(rating + 1)

        set_rating(new_rating)
        
        song = song_string(current_track())

        self.n.update(song, rating)
        self.n.change_stars(new_rating)

    def show(self):
        rating = get_rating()
        song = song_string(current_track())

        self.n.update(song, rating)
        self.n.show()

if __name__ == '__main__':
    rate_song = RateSong()
    
    gtk.main()
