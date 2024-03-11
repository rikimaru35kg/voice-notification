import time

import utils
import const


def main():
    # morning
    time_0630 = utils.PlaySound("06:30:00", const.WAV_0630_SMALL)
    food1 = utils.PlaySound("06:30:01", const.WAV_FOOD_SMALL)
    time_0655 = utils.PlaySound("06:55:00", const.WAV_0655_SMALL)
    time_wakeup = utils.PlaySound("06:55:00", const.WAV_WAKEUP_SMALL)
    time_0720 = utils.PlaySound("07:20:00", const.WAV_0720)
    time_ibokorori1 = utils.PlaySound("07:20:01", const.WAV_IBOKORORI)
    time_1130 = utils.PlaySound("11:30:00", const.WAV_1130, day=[5,6])
    time_ibokorori15 = utils.PlaySound("11:30:01", const.WAV_IBOKORORI, day=[5,6])
    # afternoon
    time_1200 = utils.PlaySound("12:00:00", const.WAV_1200)
    food2 = utils.PlaySound("12:00:01", const.WAV_FOOD)
    time_1435 = utils.PlaySound("14:35:00", const.WAV_1435, day=[2])
    pickup_ko = utils.PlaySound("14:35:01", const.WAV_PICKUPKO, day=[2])
    # evening
    time_1700= utils.PlaySound("17:00:00", const.WAV_1700)
    time_ibokorori2 = utils.PlaySound("17:00:01", const.WAV_IBOKORORI)
    time_1900 = utils.PlaySound("19:00:00", const.WAV_1900)
    food3 = utils.PlaySound("19:00:01", const.WAV_FOOD)
    tutoring_school = utils.PlaySound("18:15:00", const.WAV_TUTORING, day=[1,4])
    # night
    time_2000 = utils.PlaySound("20:00:00", const.WAV_2000)
    homework = utils.PlaySound("20:00:00", const.WAV_HOMEWORK)
    time_2100 = utils.PlaySound("21:00:00", const.WAV_2100)
    time_notification2 = utils.PlaySound("21:00:01", const.WAV_TIMENOTIFICATION, day=[1, 4, 5])
    cardboard = utils.PlaySound("21:00:01", const.WAV_CARDBOARD, day=[0])
    flammable = utils.PlaySound("21:00:01", const.WAV_FLAMMABLE, day=[2, 6])
    inflammable = utils.PlaySound("21:00:01", const.WAV_INFLAMMABLE, day=[3])
    time_2130 = utils.PlaySound("21:30:00", const.WAV_2130)
    time_ibokorori3 = utils.PlaySound("21:30:01", const.WAV_IBOKORORI)
    time_2200 = utils.PlaySound("22:00:00", const.WAV_2200_SMALL)
    sleep = utils.PlaySound("22:00:01", const.WAV_SLEEP_SMALL)

    while (True):
        # morning
        time_0630.playsound()
        food1.playsound()
        time_0655.playsound()
        time_wakeup.playsound()
        time_0720.playsound()
        time_ibokorori1.playsound()
        time_1130.playsound()
        time_ibokorori15.playsound()
        # afternoon
        time_1200.playsound()
        food2.playsound()
        time_1435.playsound()
        pickup_ko.playsound()
        # evening
        time_1700.playsound()
        time_ibokorori2.playsound()
        time_1900.playsound()
        food3.playsound()
        tutoring_school.playsound()
        # night
        time_2000.playsound()
        homework.playsound()
        time_2100.playsound()
        time_notification2.playsound()
        cardboard.playsound()
        flammable.playsound()
        inflammable.playsound()
        time_2130.playsound()
        time_ibokorori3.playsound()
        time_2200.playsound()
        sleep.playsound()

        time.sleep(0.5)


if __name__ == '__main__':
    main()
