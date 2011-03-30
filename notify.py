#!/usr/bin/env python

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

import pynotify, time

pynotify.init('rate song')


def stars(n, max_stars=5):
    if n > max_stars:
        n = max_stars
    elif n < 0:
        n = 0

    msg = ''
    for i in range(n):
        msg += u'\u2605'

    for i in range(max_stars - n):
        msg += u'\u2606'

    return msg

class Notify(object):
    def __init__(self):
        self.song = None
        self.stars = None
        self.n = None

    def update(self, song, num_stars):
        self.song = song
        self.stars = stars(num_stars)

        if self.n is None:
            # creating pynotify.Notification is done here, because we,
            # apparently, cannot create it with
            # self.song=self.stars=''
            self.n = pynotify.Notification(self.song, self.stars)

    def change_stars(self, new_num_stars):
        '''Show the old stars for 300ms and then update the bubble
        to the new number of stars.'''
        new_stars = stars(new_num_stars)
        self.n.show()
        time.sleep(0.300)
        self.n.update(self.song, new_stars)
        self.n.show()
        self.stars = new_stars

    def show(self):
        self.n.show()

if __name__ == '__main__':
    n = pynotify.Notification('title', 'message')
    n.show()
    time.sleep(.3)
    n.update('new message')
    n.show()
