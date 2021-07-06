from appium import webdriver
import time




server = "http://localhost:4723/wd/hub"
param = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver = webdriver.Remote(server,param)

time.sleep(3)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()

time.sleep(1)
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
time.sleep(1)
el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el3.click()
time.sleep(1)
for i in range(20):
# while True:
    # TouchAction(driver).press(x=497, y=1161).move_to(x=497, y=427).release().perform()
    driver.swipe(458, 1168, 465, 410, 306)
    time.sleep(10)

    # currenttime = datetime.datetime.now()

    # if (str(currenttime))[:-7] >= '2021-07-05 16:51:10':
    #     break


driver.quit()