from selenium import webdriver
from time import sleep

def getscreenshot():
    driver = webdriver.Firefox(executable_path=r'C:\Users\sabri\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe')
    driver.get('https://tan-janeczka-31.tiiny.site/')
    sleep(1)

    driver.get_screenshot_as_file("screenshot.png")
    driver.quit()
    print("end...")

getscreenshot()