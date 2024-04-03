import schedule
import time

#time for the evening
def main_bulb_turned_on():
    print("Turned on!, Good evening..")

#time for the morning
def main_bulb_turned_off():
    print("Turned off! Wake upppp....")

schedule.every().day.at("22:54").do(main_bulb_turned_on)
schedule.every().day.at("07:00").do(main_bulb_turned_off)

while True:
    schedule.run_pending()
    time.sleep(1)
