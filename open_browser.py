import os, random, sys, time
# from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get('https://www.linkedin.com/uas/login')
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]
time.sleep(2)
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
time.sleep(2)
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
time.sleep(2)
elementID.submit()
visitingProfileID = 'in/yasha-zakh-8a98991b5/'
time.sleep(2)
fullLink = "https://www.linkedin.com" + visitingProfileID
browser.get(fullLink)
visitedProfiles = []
prfilesQueued = []
