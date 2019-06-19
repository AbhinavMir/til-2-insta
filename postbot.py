import datetime
from selenium import webdriver
import time

#https://www.instagram.com/todayilearnedbot/

dt=datetime.datetime.today()
print(dt.weekday())

def main():
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login')
    username = driver.find_element_by_xpath('//*[@name="username"]')
    password = driver.find_element_by_xpath('//*[@name="password"]')
    login_btn = driver.find_element_by_xpath('//*[@class="_aj7mu _taytv _ki5uo _o0442"]')
    
    username.send_keys("username")
    password.send_keys("password!")

main()

#monday=0,wednesday=2,friday=4
count = 0
while(True):
    count = 0
    #print("while loop")
    if(dt.weekday()==0 or dt.weekday()==2 or dt.weekday()==4):
        nw=datetime.datetime.now()
        #print("1nfdkjdf")
        while(nw.hour == 14 and nw.minute == 57):
            #print("2xdfbdfbdfb")
            if(count<1):
                #print("3fdgdfgdg")
                main()
                count = count + 1


