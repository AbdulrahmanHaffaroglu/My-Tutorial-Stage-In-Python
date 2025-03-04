import datetime
import time
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

def setAlarm():
    Alarm_Time = input("Set the Alarm (hours:minutes:seconds): ")
    print(f"Alarm set for {Alarm_Time}")
    print()
    return Alarm_Time


def Alarm():
    Alarm_time = setAlarm()
    sound_file = "PythonAlarm\\Wooden_Train_Whistle.mp3"
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"))

        if Alarm_time == datetime.datetime.now().strftime("%H:%M:%S"):
            print("Wake UP ⏰")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break
        
        time.sleep(1)



if __name__ == "__main__":
    Alarm()