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
MAX_RETRY_LIMIT = 10

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

    # get all the chapters
    items = driver.find_elements(By.CLASS_NAME, "card")

    for i in items:
        print(i.text.splitlines()[0])

    for i in items:
        print("clicking itmes: ", i.text.splitlines()[0])
        driver.implicitly_wait(30)
        i.click()
        time.sleep(1)

        # sub section in the chapters
        course_body = i.find_elements(By.CSS_SELECTOR, ".card-body > .d-flex")

        for chap in course_body:
            print("chap: ", chap.text.splitlines()[0])
            # driver.implicitly_wait(30)
            # chap.click()
            # time.sleep(1)
            # find if already done. if done skip
            # if chap.find_element(By.CSS_SELECTOR, ".checkboxDiv input").get_attribute("checked") != 'true':

            chk = chap.find_element(
                By.CSS_SELECTOR, ".checkboxDiv input").get_attribute("checked")
            print("Flag: ", chk)

            if chk:
                continue

            if not chk:
                link = chap.find_element(
                    By.CSS_SELECTOR, ".course-video-title")
                print("link:", link.text)

                driver.implicitly_wait(30)
                link.click()
                time.sleep(1)
                # link.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)

    return True


if __name__ == "__main__":

    login()
    # debug()
    # clicker()

    while True:
        print("Enter save, click, q: ", end="")
        inp = input()

        if inp == "click":
            retry_attempt = 0
            while (retry_attempt < MAX_RETRY_LIMIT):
                try:
                    flag = clicker()
                    if flag:
                        break
                except:
                    print("retrying...")
                    retry_attempt += 1

        if inp == 'q':
            break
