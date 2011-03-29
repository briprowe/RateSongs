import keybinder, gtk

from banshee import current_track, get_rating, set_rating
from notify import Notify


def song_string(track):
    msg = str(track['name'])
    msg += ' on ' + str(track['album'])
    msg += ' by ' + str(track['artist'])

    return msg

class RateSong(object):
    def __init__(self):
        self.n = Notify()

        for x in range(1,6):
            key = '<ctrl>F' + str(x)
            keybinder.bind(key, lambda y=x: self.rate(y))

    def rate(self, n):
        rating = get_rating()
        set_rating(n)
        track = current_track()

        song = song_string(track)

        self.n.update(song, rating)
        self.n.change_stars(n)

if __name__ == '__main__':
    rate_song = RateSong()
    
    gtk.main()
