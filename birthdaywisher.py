#Author pixal-sama a.k.a Rakshat Kashyap
#created on 17-05-2020
#use this bot, that wishes birthdays of facebook and then mail you if there were birthdays or not, and also who had their birthday today, quite a handy and cool thing right



#Importing the required libraries, make sure to install them first also make sure to download the driver according to your browser,unless using firefox, I am using chrome here so I assume that you got chrome too,else any browser will work just download the correct driver
from selenium import webdriver
from datetime import datetime
import os, time, credentials, bs4, re, smtplib # os, time, re and smtplib are preinstalled, still check all the required libraries before running the porgram
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from webdriver_manager.chrome import ChromeDriverManager

fromMail = "" # enter your mail here
toMail = "" # enter to mail, usually same as fromMail
appPass = "" # enter your app password provied by gmail

# NOTE: make sure you have two-step verification activated on your gmail account, then create app password, check out on support.google.com and know how to do that
# If you don't do the above method, you won't be able to login to your mail



#help dealing with the facebook's show notification pop-up
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument('headless')
option.add_argument('window-size=1920x1080') # makes window headless, mostbrowsers support it, still check if your browser does it or not.

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
#connecting the browser, make sure you have the driver downloaded according to your default broswer, and add the complete path of that exe file in executable_path
browser = webdriver.Chrome(ChromeDriverManager().install(),options=option) # Use your broswer specific command, this one only works for chrome
time.sleep(5)
# browser = webdriver.Chrome('C:\\Users\\pixalquarks\\Dattbayo\\chromedriver')
#getting the facebook home page
browser.get('https://www.facebook.com')
print('opened successfully')
time.sleep(6)

#selecting email and password entry field
e_mail = browser.find_element_by_xpath('//*[@id="email"]')
pa_ss = browser.find_element_by_xpath('//*[@id="pass"]')

#pass
e_mail.send_keys('rakkas0302@gmail.com')
time.sleep(1)
pa_ss.send_keys('wrtlightandenergy')
time.sleep(1)
pa_ss.send_keys(Keys.ENTER)
time.sleep(7)
birthday_xpath = "/html[@id='facebook']/body[@class='_6s5d _71pn _-kb segoe']/div[@id='mount_0_0']/div/div/div[@class='rq0escxv l9j0dhe7 du4w35lb']/div[@class='du4w35lb l9j0dhe7 cbu4d94t j83agx80']/div[@class='j83agx80 cbu4d94t jgljxmt5 l9j0dhe7 be9z9djy']/div[@class='j83agx80 cbu4d94t d6urw2fd dp1hu0rb l9j0dhe7 du4w35lb']/div[@class='cuepibvl ka73uehy dp1hu0rb j83agx80']/div[@class='ahb00how o9ndlxrr fer614ym dp1hu0rb pzfvarvs buofh1pr ftbm7790']/div[@class='iyyx5f41 czl6b2yu poy2od1o dhp61c6y dp1hu0rb owwhemhu pad24vr5 cbu4d94t n7fi1qx3 j83agx80']/div[@class='q5bimw55 ofs802cu dkue75c7 mb9wzai9 o8kakjsu rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos buofh1pr l56l04vs r57mb794 l9j0dhe7 kh7kg01d c3g1iek1 k4xni2cv']/div[@class='a8s20v7p k5wvi7nf buofh1pr pfnyh3mw l9j0dhe7 du4w35lb']/div[@class='cxgpxx05']/div[1]/div[@class='l9j0dhe7']/div[@class='cxgpxx05 sj5x9vvc']/div/div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi']/div[@class='ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 nnctdnn4 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr']"
# create a name searcher regex
searcher = re.compile(r'[A-Z]\w+\s[A-Z]\w+')
#this checks is there any birthday element, if yes then first get it and extract all names out of it, if no(error) then we just return an empty names string
screenshots = []
try:
	birthday = browser.find_element_by_xpath(birthday_xpath)#find the birthday element
	names = searcher.findall(birthday.text)
except:
	names = []
	print('no birthday today')
	date = str(datetime.now().date())
	paths = 'fullpath' + date + 'extention' # replace fullpath with the path on your pc where you store your images, replace extention with the image extention (usually .png)
	browser.get_screenshot_as_file(paths)
	screenshots.append(paths)



time.sleep(3)


#iterate over the names and wish them, then create a message about who had thier birthday today
if len(names):
	for name in names:
		message_icon = browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[2]/div[4]/div[1]/div[3]/span/div/div[1]')
		message_icon.click()
		time.sleep(1.5)
		search_box = browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/label/input')
		search_box.click()
		search_box.send_keys(name)
		time.sleep(1)
		search_box.send_keys(Keys.DOWN)
		time.sleep(1)
		search_box.send_keys(Keys.ENTER)
		time.sleep(3)
		message_box = browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[5]/div[1]/div[1]/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')
		message_box.click()
		message_box.send_keys('Happy Birthday Bro')
		message_box.send_keys(Keys.ENTER)
		time.sleep(1)
		name = name.replace(' ', '_')
		pathe = 'fullpath' + name + 'birthdayWishScreenshot' + 'extention' # make sure to replace fullpath and extention
		browser.get_screenshot_as_file(pathe)
		screenshots.append(pathe)
		time.sleep(2)
		browser.refresh()
		time.sleep(6)
	birthday_dudes = ' and '.join(names)
	message = 'Subject: Wished Birthdays today...\n\n' + birthday_dudes + 'have their birthdays today, I wished them properly\n\n' + '-BirthdayWisher Bot'
#If there were no birthdays i.e. names was empty then just create message that there were no birthday today
else:
	message = 'Subject: NO birthdays today...\n\nThere were no birthdays today\n\n-BirthdayWisher Bot'

time.sleep(4)
browser.quit()

# This piece of code attach image, to address, from address, subject, and main text to the email to be sent
img_data = open(screenshots[0], 'rb').read()
msg = MIMEMultipart()
msg['Subject'] = 'Birthday Wishes'
msg['From'] = fromMail
msg['To'] = toMail

text = MIMEText(message)
msg.attach(text)
image = MIMEImage(img_data, name=os.path.basename(screenshots[0]))
msg.attach(image)


#connect to gmail's smtp server
conn = smtplib.SMTP('smtp.gmail.com', 587)
time.sleep(10)
conn.ehlo()
#establish secure connection and login
time.sleep(5)
conn.starttls()
time.sleep(5)
conn.login(fromMail,appPass)
print('mail connected successfully')
time.sleep(8)
#send the mail
conn.sendmail(msg['From'],msg['To'],msg.as_string())
time.sleep(8)
conn.quit()


