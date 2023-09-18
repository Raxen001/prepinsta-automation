import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# TODO
#
# add phone number input
# add otp input
#
# list courses and click select
# increase speed
#
# close feedback
# close ad pop ups
#
# answer quiz

PHONENUMBER = ""
BASE_URL = "https://prepinstaprime.com/"

driver = webdriver.Firefox()
driver.get(BASE_URL)


def login():

    login_button = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/header/nav/div[3]/div[2]/a[2]")
    login_button.click()

    phone_number_enter = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div/div/form/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/input")
    phone_number_enter.click()
    phone_number_enter.send_keys(PHONENUMBER)

    get_otp = driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div/div/div/form/div/div[2]/div/div[2]/div/div[3]/div/button")
    get_otp.click()


def nav_to_course():

    course_button = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[3]/div[1]/div[3]/button"
    )
    course_button.click()


def clicker():

    ele = driver.find_elements(By.CLASS_NAME, "card")
    for i in ele:
        i.click()
        links = i.find_elements(By.CLASS_NAME, "course-video-title")
        time.sleep(1)
        for j in links:
            j.click()
            j.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)
            time.sleep(2)
        j.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)


if __name__ == "__main__":

    login()
    # debug()
    # clicker()

    while True:
        print("Enter save, click, q: ", end="")
        inp = input()

        if inp == "click":
            try:
                clicker()
            except:
                print("something went wrong...")

        if inp == 'q':
            break
