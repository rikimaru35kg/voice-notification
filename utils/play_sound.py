from datetime import datetime as dt
from datetime import date
from datetime import timedelta as td

from pydub import AudioSegment
from pydub.playback import play

import const


class PlaySound:
    waiting = True
    playtime = None; playfile = None
    def __init__(self, playtime, playfile):
        self.playtime = playtime
        self.playfile = playfile
    def playsound(self):
        dt_now = dt.now()
        t_notify = dt.time(dt.strptime(self.playtime, '%H:%M:%S'))
        dt_notify = dt.combine(date.today(), t_notify)
        dt_notify_buf = dt_notify + td(seconds=const.TIME_BUFFER)

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
