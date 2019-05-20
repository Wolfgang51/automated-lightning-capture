from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal
import os
import subprocess

shot_date = datetime.now().strftime("%Y-%m-%d")
print(shot_date)  # 2019-05-19


def capture_cmd():
    shot_time = datetime.now().strftime("%Y-%m-%d" "%H:%M:%S")
    triggerAndDownloadWithName = [
        "--capture-image-and-download", "--filename", shot_time]
    return triggerAndDownloadWithName


def createSaveFolder(save_location):
    try:
        os.chdir("/home/pi/Pictures")
        print("Creating folder to save images: ", save_location)
        os.makedirs(save_location)
        os.chdir(save_location)
        current_directory = os.getcwd()
        print("Current Directory: ", current_directory)
    except:
        print("failed to create the new directory.")


def captureImage():
    for x in range(0, 10):
        trigger_cmd = capture_cmd()
        gp(trigger_cmd)
        sleep(3)


createSaveFolder(shot_date)
captureImage()
