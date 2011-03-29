#!/usr/bin/env python

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

# def update(bubble, num_stars, song):
#     bubble.update(song, stars(num_stars))

# def notify(num_stars, song):
#     n = pynotify.Notification(song, stars(num_stars))
#     n.show()

#     return n

if __name__ == '__main__':
    n = pynotify.Notification('title', 'message')
    n.show()
    time.sleep(.3)
    n.update('new message')
    n.show()
