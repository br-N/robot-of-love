from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as e
from time import sleep
from random import randint

class LoveRobot:

    def __init__ (self, my_username, my_password, my_url, my_option, my_num):
        self.username = my_username
        self.password = my_password
        self.url = my_url
        self.option = my_option
        self.num = my_num

    def driver_init (self):
        # Maybe need to use the specified path for webdriver
        driver_options = webdriver.ChromeOptions() # Suppressing init errors (Bluetooth and GPU)
        driver_options.add_experimental_option("excludeSwitches", ['enable-logging'])

        self.driver = webdriver.Chrome(options=driver_options)
        self.driver.get("https://www.instagram.com/")
        sleep(randint(2,4))

        u = self.driver.find_element_by_name("username")
        u.send_keys(self.username)
        sleep(randint(2,4))

        p = self.driver.find_element_by_name("password")
        p.send_keys(self.password)
        sleep(randint(2,4))

        p.send_keys(Keys.ENTER)
        sleep(randint(2,4))

        try:
            self.driver.find_element_by_xpath("//*[@data-testid='login-error-message']")
            print("OUTPUT: (ERROR) Invalid Username or Password")
            self.driver.close()
        except:
            pass
        sleep(randint(2,4))

        self.driver.find_element_by_class_name("yWX7d").click() # Don't save info button
        sleep(randint(2,4))

        self.driver.find_element_by_class_name("HoLwm").click() # Don't turn on notifications 
        sleep(randint(2,4))

        self.driver.get(self.url)
        sleep(randint(2,4))

    def like_photo (self):
        try:
            # Must change 'Descurtir' to your language (ex: Dislike)
            self.driver.find_element_by_xpath("//*[@aria-label='Descurtir']")
        except:
            try:
                self.driver.find_element_by_class_name("fr66n").click()
            except:
                pass
            pass
        sleep(randint(1,4))

    def follow_person (self):
        try:
            # Must change 'Seguir' to your language (ex: Follow)
            self.driver.find_elements_by_xpath("//button/div[contains(., 'Seguir')]")[0].click()
        except:
            pass
        sleep(randint(1,4))

    def next_photo (self):
        try:
            return self.driver.find_element_by_class_name("l8mY4")
        except e.NoSuchElementException:
            print("(OUTPUT) Reached the end")
            return 0

    def like_forever (self):
        counter = 0
        # Goes to the first image
        self.driver.find_element_by_class_name("_9AhH0").click()
        sleep(randint(1,4))

        # Likes picture and goes to next one
        while(True):
            self.like_photo() 

            counter+=1
            print("Post counter:", counter)
            next = self.next_photo()
            if(next and counter<self.num):
                next.click()
                sleep(randint(1,4))
            else:
                break
    
    def follow_forever (self):
        counter = 0
        # Goes to the first image
        self.driver.find_element_by_class_name("_9AhH0").click()
        sleep(randint(1,4))

        # Likes picture and goes to next one
        while(True):
            self.follow_person()

            counter+=1
            print("Post counter:", counter)
            next = self.next_photo()
            if(next and counter<self.num):
                next.click()
                sleep(randint(1,4))
            else:
                break

    def follow_like_forever (self):
        counter = 0
        # Goes to the first image
        self.driver.find_element_by_class_name("_9AhH0").click()
        sleep(randint(1,4))

        # Likes picture and goes to next one
        while(True):
            self.follow_person()
            self.like_photo() 

            counter+=1
            print("Post counter:", counter)
            next = self.next_photo()
            if(next and counter<self.num):
                next.click()
                sleep(randint(1,4))
            else:
                break
                
    def start_robot (self):
        self.driver_init()
        if self.option==1:
            self.like_forever()
        elif self.option==2:
            self.follow_forever()
        elif self.option==3:
            self.follow_like_forever()
        else:
            pass
        self.driver.close()
