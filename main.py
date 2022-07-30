################################
#automatic steam key redeemer  #
#by: josh leckey               #
#date: 30/07/2022              #
#version: 1.0                  #
#license: GPLv3                #
################################

import threading
from random import randrange

from selenium import webdriver
import concurrent.futures
import ThreadPoolExecutorPlus
import urllib.request
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

from selenium.webdriver.firefox.options import Options


def logic(threads, keys, steam_id, steam_pass):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(executable_path='geckodriver.exe', options=options)
    try:
        driver.get("https://store.steampowered.com/login/")
        if(driver.current_url == "https://store.steampowered.com"):
            pass
        else:
            username = driver.find_element_by_id("input_username").send_keys(username)
            password = driver.find_element_by_id("input_password").send_keys(password)
            element = driver.find_element_by_xpath("//*[@text='Sign In']").click()
            auth = input("Please enter steam authcode sent to your email: ")
            authcode = driver.find_element_by_id("authcode").send_keys(auth)
            element = driver.find_element_by_xpath("//*[@text='Submit']").click()
            time.sleep(5)
            if(driver.current_url == "https://store.steampowered.com/"):
                pass
    except:
        pass
    try:
        driver.get(url)
    except:
        driver.close()
        return
    try:
        for(i in range(threads)):
            element = driver.find_element_by_id("product_key")
            element.send_keys(keys[i])
            checkbox = driver.find_element_by_id("accept_ssa")
            register = driver.find_element_by_id("register_btn")


capabilities = webdriver.DesiredCapabilities.CHROME
url = "https://store.steampowered.com/account/registerkey"
username = input("Enter your username: ")
password = input("Enter your password: ")
file = open(file, "r")
keys[] = file.read.splitlines()
file.close()
logic(keys.length, keys, username, password)


print ("Completed")

