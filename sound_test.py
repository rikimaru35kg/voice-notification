import utils
import const

from datetime import datetime as dt

test = utils.PlaySound(dt.now().strftime("%H:%M:%S"), const.WAV_FOOD)
test.playsound()
