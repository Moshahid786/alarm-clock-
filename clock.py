import datetime
from playsound import playsound
hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
second = int(input("Enter second: "))
am_pm = input("am/pm: ")

if am_pm == "pm":
    hour =hour+12
else:
    hour =hour-12

while True:
    if hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute and second == datetime.datetime.now().second:
        print("Alarm ON!")
        playsound("C:\\Users\\Raz\\Downloads\\arabic-background.mp3")
        break


