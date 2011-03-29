#!/usr/bin/env python

import dbus

bus = dbus.SessionBus()
banshee = bus.get_object('org.bansheeproject.Banshee',
                         '/org/bansheeproject/Banshee/PlayerEngine')

def set_rating(n):
    if n < 0:
        n = 0
    elif n > 5:
        n = 5
        
    banshee.SetRating(dbus.Byte(n))

def get_rating():
    return banshee.GetRating()

def inc_rating():
    rating = int(banshee.GetRating()) + 1
    banshee.SetRating(dbus.Byte(rating))

    return rating

def dec_rating():
    rating = int(banshee.GetRating()) - 1
    banshee.SetRating(dbus.Byte(rating))

    return rating
