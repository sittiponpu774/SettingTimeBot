from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
import time, pygame

username = input("Enter in your username: ")
password = getpass("Enter your password: ")

pygame.init()
clock = pygame.time.Clock()
while True:
    clock.tick(1)
    theTime=time.strftime("%H:%M:%S", time.localtime())
    # print(theTime)

    if username != "" and password != "" and theTime == "22:32:00":
        driver = webdriver.Chrome("C:\\Users\\HP\\Desktop\\botnet\\chromedriver.exe")
        driver.get("http://10.0.0.1/login.php")

        username_textbox = driver.find_element_by_name("username")
        username_textbox.send_keys(username)

        password_textbox = driver.find_element_by_name("password")
        password_textbox.send_keys(password)

        login_button = driver.find_element_by_name("submit").send_keys(Keys.ENTER)
        