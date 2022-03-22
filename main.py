from love_robot import LoveRobot
from getpass import getpass

# Gets IG username
username = input("Username: ")

# Gets IG password secretly
password = getpass()

# Gets tag or person URL (Example: https://www.instagram.com/explore/tags/likeforlike/)
url = input("URL: ")

# Choose if wants only to like, only to follow or both
option = int(input("Like (1) | Follow (2) | Both (3): "))

# How many posts wants to like or follow the person
num = int(input("How many posts? "))

# Specified path for webdriver
path = '/usr/bin/chromedriver'

# Robot start
meu_robo = LoveRobot(username, password, url, option, num, path)
meu_robo.start_robot()