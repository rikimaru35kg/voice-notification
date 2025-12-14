import time

import utils
import const


def main():
    # morning
    time_0655 = utils.PlaySound("06:55:00", const.WAV_0655_SMALL)
    time_wakeup = utils.PlaySound("06:55:00", const.WAV_WAKEUP_SMALL)
    foodremainder1 = utils.PlaySound("07:00:00", const.WAV_FOODREMAINDER)
    # afternoon
    foodremainder2 = utils.PlaySound("13:00:00", const.WAV_FOODREMAINDER)
    # evening
    # night
    time_2000 = utils.PlaySound("20:00:00", const.WAV_2000)
    homework = utils.PlaySound("20:00:01", const.WAV_HOMEWORK)
    foodremainder3 = utils.PlaySound("20:00:02", const.WAV_FOODREMAINDER)
    time_2100 = utils.PlaySound("21:00:00", const.WAV_2100)
    time_notification2 = utils.PlaySound("21:00:01", const.WAV_TIMENOTIFICATION, day=[1, 4, 5])
    cardboard = utils.PlaySound("21:00:01", const.WAV_CARDBOARD, day=[0])
    flammable = utils.PlaySound("21:00:01", const.WAV_FLAMMABLE, day=[2, 6])
    inflammable = utils.PlaySound("21:00:01", const.WAV_INFLAMMABLE, day=[3])
    time_2200 = utils.PlaySound("22:00:00", const.WAV_2200_SMALL)
    sleep = utils.PlaySound("22:00:01", const.WAV_SLEEP_SMALL)

    while (True):
        # morning
        time_0655.playsound()
        time_wakeup.playsound()
        foodremainder1.playsound()
        # afternoon
        foodremainder2.playsound()
        # evening
        # night
        time_2000.playsound()
        homework.playsound()
        foodremainder3.playsound()
        time_2100.playsound()
        time_notification2.playsound()
        cardboard.playsound()
        flammable.playsound()
        inflammable.playsound()
        time_2200.playsound()
        sleep.playsound()

        time.sleep(0.5)


if __name__ == '__main__':
    main()
