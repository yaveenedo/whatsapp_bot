import os
import datetime
from time import sleep

import pyautogui

from configs import path_log_file


def write_log_txt_file(message=' - None'):
    now = datetime.datetime.now()
    now_formatted = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(path_log_file, 'a') as file:
        file.write(f'{now_formatted} - {message}\n')


def wait_until_file_exist(path_file_to_wait: str, on_complete=lambda: None):
    while True:
        sleep(1)
        if os.path.isfile(path_file_to_wait):
            on_complete()
            sleep(2)
            break


def pyautogui_wait_until_object_visible(path_image_file_to_wait: str, confidence=.8, grayscale=False, on_complete=lambda: None):
    while True:
        sleep(1)
        object_to_wait = pyautogui.locateCenterOnScreen(path_image_file_to_wait, confidence=confidence, grayscale=grayscale)
        if object_to_wait is not None:
            on_complete()
            break


def pyautogui_reset_cursor_position():
    screen_width = pyautogui.size()[0]
    pyautogui.moveTo(screen_width / 2, 2)


if __name__ == "__main__":
    pyautogui_reset_cursor_position()
