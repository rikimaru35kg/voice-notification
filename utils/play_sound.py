from datetime import datetime as dt
from datetime import date
from datetime import timedelta as td

from pydub import AudioSegment
from pydub.playback import play

import const


class PlaySound:
    waiting = True
    playtime = None; playfile = None
    day = []
    def __init__(self, playtime, playfile, day=[]):
        """Initialize PlaySound class
        Args:
            playtime (str): e.g. "06:55:00"
            playfile (str): filename of wav file
            day (list[int]): 0(Mon),1(Tue),...,6(Sun), eg) [0, 3, 6]
        """
        self.playtime = playtime
        self.playfile = playfile
        self.day = day
    def playsound(self):
        """Play sound if the conditions are met"""
        dt_now = dt.now()
        t_notify = dt.time(dt.strptime(self.playtime, '%H:%M:%S'))
        dt_notify = dt.combine(date.today(), t_notify)
        dt_notify_buf = dt_notify + td(seconds=const.TIME_BUFFER)

        day = dt_now.weekday()
        if (len(self.day)>0 and day not in self.day): return

        if (self.waiting):
            if (dt_now < dt_notify): return
            if (dt_now > dt_notify_buf): return
            # play sound if not returned
        else:
            if (dt_now > dt_notify + td(seconds=const.TIME_BUFFER)):
                self.waiting = True
            return

        sound = AudioSegment.from_wav(self.playfile)
        play(sound)
        self.waiting = False
