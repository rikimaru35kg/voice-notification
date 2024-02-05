import utils
import const


def main():
    time_0630 = utils.PlaySound("06:30:00", const.WAV_0630)
    food1 = utils.PlaySound("06:30:01", const.WAV_FOOD)
    time_0655_wakeup = utils.PlaySound("06:55:00", const.WAV_0655)
    time_1130 = utils.PlaySound("11:30:00", const.WAV_1130)
    food2 = utils.PlaySound("11:30:01", const.WAV_FOOD)
    time_1200 = utils.PlaySound("12:00:00", const.WAV_1200)
    time_notification1 = utils.PlaySound("12:00:01", const.WAV_TIMENOTIFICATION)
    time_1800 = utils.PlaySound("18:00:00", const.WAV_1800)
    food3 = utils.PlaySound("18:00:01", const.WAV_FOOD)
    time_2000 = utils.PlaySound("20:00:00", const.WAV_2000)
    homework = utils.PlaySound("20:00:00", const.WAV_HOMEWORK)
    time_2100 = utils.PlaySound("21:00:00", const.WAV_2100)
    time_notification2 = utils.PlaySound("21:00:01", const.WAV_TIMENOTIFICATION)
    time_2200 = utils.PlaySound("22:00:00", const.WAV_2200)
    sleep = utils.PlaySound("22:00:00", const.WAV_SLEEP)
    while (True):
        time_0630.playsound()
        food1.playsound()
        time_0655_wakeup.playsound()
        time_1130.playsound()
        food2.playsound()
        time_notification1.playsound()
        time_1200.playsound()
        time_1800.playsound()
        food3.playsound()
        time_2000.playsound()
        homework.playsound()
        time_notification2.playsound()
        time_2100.playsound()
        time_2200.playsound()
        sleep.playsound()

if __name__ == '__main__':
    main()
