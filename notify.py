#!/usr/bin/env python

import pynotify

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

def notify(num_stars, song):
    pynotify.init('Test')
    n = pynotify.Notification(stars(num_stars),song)
    n.show()
