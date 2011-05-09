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

import dbus

def bind():
    bus = dbus.SessionBus()
    banshee = bus.get_object('org.bansheeproject.Banshee',
                             '/org/bansheeproject/Banshee/PlayerEngine')

    return banshee

def set_rating(n, banshee=None):
    banshee = banshee or bind()

    if n < 0:
        n = 0
    elif n > 5:
        n = 5
        
    banshee.SetRating(dbus.Byte(n))

def get_rating(banshee=None):
    banshee = banshee or bind()
        
    return banshee.GetRating()

def inc_rating(banshee=None):
    banshee = banshee or bind()
        
    rating = int(banshee.GetRating()) + 1
    banshee.SetRating(dbus.Byte(rating))

    return rating

def dec_rating(banshee=None):
    banshee = banshee or bind()

    rating = int(banshee.GetRating()) - 1
    banshee.SetRating(dbus.Byte(rating))

    return rating

def current_track(banshee=None):
    banshee = banshee or bind()
        
    return banshee.GetCurrentTrack()
