import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from configs import windows_username, path_project_folder
from utils import write_log_txt_file, pyautogui_reset_cursor_position, wait_until_file_exist, pyautogui_wait_until_object_visible



def download_and_open_chromedriver(logger=lambda: None):
    write_log = lambda message=' - None': logger(f'.{download_and_open_chromedriver.__name__}{message}')

    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument(f'user-data-dir=C:\\Users\\{windows_username}\\AppData\\Local\\Google\\Chrome\\User Data') # ? use "Google Chrome" "User Data"
    path_user_data = os.path.join(path_project_folder, 'User Data')
    chrome_options.add_argument(f'user-data-dir={path_user_data}') # ? use "Google Chrome" "User Data"
    chrome_options.add_argument("--profile-directory=Default")
    # chrome_options.add_argument('--profile-directory=Profile 1')
    # path_chrome_driver = 'chromedriver.exe'  # ? use local "chromedriver"
    path_chrome_driver = ChromeDriverManager().install()  # ? download and use downloaded "chromedriver" everytime
    
    wait_until_file_exist(path_file_to_wait=path_chrome_driver, on_complete=lambda: write_log(' - download "chromedriver" done'))
    
    chrome_service = ChromeService(executable_path=path_chrome_driver)

    chromedriver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    pyautogui_wait_until_object_visible(path_image_file_to_wait='images/chromedriver_opened_indicator.jpg', on_complete=lambda: write_log(' - wait until "chromedriver" opened done'))
    
    chromedriver.maximize_window()
    write_log(' - maximize "chromedriver" window done')
    sleep(2)

    return chromedriver

def open_whatsapp_web_in_chromedriver(chromedriver, logger=lambda: None):
    write_log = lambda message=' - None': logger(f'.{open_whatsapp_web_in_chromedriver.__name__}{message}')
    
    url_whatsapp_web = 'https://web.whatsapp.com/'
    chromedriver.get(url_whatsapp_web)
    
    WebDriverWait(chromedriver, timeout=60, poll_frequency=1).until(EC.url_matches(url_whatsapp_web))
    
    xpath_new_message_indicator = '//span[@data-testid="icon-unread-count"]'
    
    new_message_indicator = WebDriverWait(chromedriver, timeout=60, poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH, xpath_new_message_indicator)))
    write_log(' - find "new_message_indicator" done')
    
    new_message_indicator.click()
    write_log(' - click "new_message_indicator" done')
    
    xpath_messages = '//span[contains(@class,"selectable-text")]/span'
    
    messages = WebDriverWait(chromedriver, timeout=60, poll_frequency=1).until(EC.visibility_of_all_elements_located((By.XPATH, xpath_messages)))
    new_message = messages[-1].text.lower()
    
    xpath_message_box = '//div[@data-testid="conversation-compose-box-input"]'
    
    if new_message == 'halo':
        message_box = WebDriverWait(chromedriver, timeout=60, poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH, xpath_message_box)))
        write_log(' - find "message_box" done')
        
        message_box.send_keys('wassup!')
        write_log(' - fill "message_box" done')
        sleep(2)

        message_box.send_keys(Keys.ENTER)
        write_log(' - send message done')
        sleep(2)
        return

    if new_message == 'hai':
        message_box = WebDriverWait(chromedriver, timeout=60, poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH, xpath_message_box)))
        write_log(' - find "message_box" done')
        
        message_box.send_keys('dheremah cak!')
        write_log(' - fill "message_box" done')
        sleep(2)

        message_box.send_keys(Keys.ENTER)
        write_log(' - send message done')
        sleep(2)
        return

    if new_message == 'oi':
        message_box = WebDriverWait(chromedriver, timeout=60, poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH, xpath_message_box)))
        write_log(' - find "message_box" done')
        
        message_box.send_keys('oit!')
        write_log(' - fill "message_box" done')
        sleep(2)

        message_box.send_keys(Keys.ENTER)
        write_log(' - send message done')
        sleep(2)
        return
    

def whatsapp_bot():
    """
    Whatsapp bot v1
    """

    write_log = lambda message=' - None': write_log_txt_file(f'@{whatsapp_bot.__name__}{message}')
    
    pyautogui_reset_cursor_position()

    write_log(f' - {whatsapp_bot.__name__} started')

    chromedriver = download_and_open_chromedriver(logger=write_log)
    
    open_whatsapp_web_in_chromedriver(chromedriver=chromedriver, logger=write_log)

def main():
    whatsapp_bot()


if __name__ == "__main__":
    main()
