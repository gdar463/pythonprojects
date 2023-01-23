from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import selenium.common.exceptions as selExpect
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Special:Random")

prev = ""
count = 0
listUrls = []

f = open("wikiLinks.txt","w")
f.write(str(driver.current_url) + "\n")
f.close()

while True:
    try:
        if driver.current_url != str(listUrls[-1]):
            driver.close()
            while True:
                print(str("You are done!\nYour count is: ") + str(count) + str("\nThe list was: ") + str(listUrls))
                time.sleep(1)
        if prev != driver.current_url:
            f = open("wikiLinks.txt","a")
            f.write(str(driver.current_url) + "\n")
            f.close()
            count = count + 1
            prev = driver.current_url
        f = open("wikiLinks.txt","r")
        listUrls = f.read().splitlines()
        f.close()
    except selExpect.NoSuchWindowException or selExpect.WebDriverException:
        print(str(listUrls) + "\n" + str(count))