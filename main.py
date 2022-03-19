from love_robot import LoveRobot
from getpass import getpass

username = input("Username: ")

password = getpass()

url = input("URL: ")
# Example: https://www.instagram.com/explore/tags/likeforlike/

option = int(input("Like (1) | Follow (2) | Both (3): "))

num = int(input("How many posts? "))

meu_robo = LoveRobot(username, password, url, option, num)
meu_robo.start_robot()