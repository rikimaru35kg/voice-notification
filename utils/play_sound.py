from datetime import datetime as dt
from datetime import time

from pydub import AudioSegment
from pydub.playback import play


def play_sound(playtime, playfile):
    while(True):
        if dt.now().time() < dt.time(dt.strptime(playtime, '%H:%M:%S')): continue
        sound = AudioSegment.from_wav(playfile)
        play(sound)
        break
