from glob import glob
import utils
import const

from datetime import datetime as dt

filelist = [f for f in glob("voice/*.wav")]
filelist.sort()
for f in filelist:
    print(f"\n{f}")
    test = utils.PlaySound(dt.now().strftime("%H:%M:%S"), f)
    test.playsound()
