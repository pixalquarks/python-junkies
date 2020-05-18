#Author pixal-sama a.k.a Rakshat Kashyap
#created on 17-05-2020
#use this bot, that wishes birthdays of facebook and then mail you if there were birthdays or not, and also who had their birthday today, quite a handy and cool thing right

#Importing the required libraries, make sure to install them first also make sure to download the driver according to your browser,unless using firefox, I am using chrome here so I assume that you got chrome too,else any browser will work just download the correct driver
from selenium import webdriver
import time, credentials, bs4, re, smtplib # time, re and smtplib are preinstalled, still check all the required libraries before running the porgram
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


#help dealing with the facebook's show notification pop-up
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
#connecting the browser, make sure you have the driver downloaded according to your default broswer, and add the complete path of that exe file in executable_path
browser = webdriver.Chrome(options=option, executable_path='input the full path of the chrome driver you installed earlier')# use \\ on windows for path for e.x. C:\\downloads\\chromedriver
time.sleep(5)
# browser = webdriver.Chrome('C:\\Users\\pixalquarks\\Dattbayo\\chromedriver')
#getting the facebook home page
browser.get('https://www.facebook.com')
time.sleep(6)

#selecting email and password entry field
e_mail = browser.find_element_by_xpath('//*[@id="email"]')
pa_ss = browser.find_element_by_xpath('//*[@id="pass"]')

#pass
e_mail.send_keys('your facebook email here')
time.sleep(1)
pa_ss.send_keys('Your password here')
time.sleep(1)
pa_ss.send_keys(Keys.ENTER)
time.sleep(7)

# create a name searcher regex
searcher = re.compile(r'[A-Z]\w+\s[A-Z]\w+')
#this checks is there any birthday element, if yes then first get it and extract all names out of it, if no(error) then we just return an empty names string
try:
	birthday = browser.find_element_by_xpath('//*[@id="home_birthdays"]/div/div/div/div')#find the birthday element
	names = searcher.findall(birthday.text)
except:
	names = []
	print('no birthday today')



time.sleep(5)
#iterate over the names and wish them, then create a message about who had thier birthday today
if len(names):
	for name in names:
		chat = browser.find_element_by_css_selector('#fbDockChatBuddylistNub > a > div > span.label')
		chat.click()
		time.sleep(3)
		search_box = browser.find_element_by_css_selector('#chatsearch > div > span > label > input')
		search_box.send_keys(name)
		time.sleep(2)
		search_box.send_keys(Keys.ENTER)
		time.sleep(4)
		message_box = browser.find_element_by_class_name('_1mf')
		message_box.click()
		message_box.send_keys('Happy Birthday')
		message_box.send_keys(Keys.ENTER)
		time.sleep(5)
		browser.refresh()
		time.sleep(6)
	birthday_dudes = ' and '.join(names)
	message = 'Subject: Wished Birthdays today...\n\n' + birthday_dudes + 'have their birthdays today, I wished them properly\n\n' + '-BirthdayWisher Bot'
#If there were no birthdays i.e. names was empty then just create message that there were no birthday today
else:
	message = 'Subject: NO birthdays today...\n\nThere were no birthdays today\n\n-BirthdayWisher Bot'

time.sleep(4)
browser.quit()

#connect to gmail's smtp server
conn = smtplib.SMTP('smtp.gmail.com', 587)
time.sleep(10)
conn.ehlo()
#establish secure connection and login
time.sleep(5)
conn.starttls()
time.sleep(5)
conn.login('your gmail here','your app password here')#must first activate two step verification on your gmail account and then generate an app password to login through this method
time.sleep(8)
#send the mail
conn.sendmail('sender mail','reciever mail',message)#sender mail is same as the one you logged in with, and reciever one is usually the same,but you can have it different if you want
time.sleep(8)
conn.quit()
