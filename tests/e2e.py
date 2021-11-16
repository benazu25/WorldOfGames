from time import sleep
from selenium import webdriver
import sys


def test_scores_service(URL):
    driver = webdriver.Chrome(executable_path="tests/chromedriver.exe")
    driver.get(URL)
    sleep(1)
    text = driver.find_element("score").text
    if 0 <= int(text) <= 100:
        driver.close()
        return True
    else:
        driver.close()
        return False


def main_function():
    score = test_scores_service("http://localhost:8777")
    if score:
        print("Success: ")
        sys.exit(0)
    else :
        print("Failure")
        sys.exit(-1)


main_function()
