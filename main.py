from selenium import webdriver
import time


def clickAll():
    driver.find_element_by_id("11_1").click()
    driver.find_element_by_id("12_1").click()
    driver.find_element_by_id("13_1").click()
    driver.find_element_by_id("14_1").click()
    driver.find_element_by_id("15_1").click()
    driver.find_element_by_id("16_1").click()

    driver.find_element_by_id("21_1").click()
    driver.find_element_by_id("22_1").click()
    driver.find_element_by_id("23_1").click()
    driver.find_element_by_id("24_1").click()

    driver.find_element_by_id("31_5").click()
    driver.find_element_by_id("32_5").click()
    driver.find_element_by_id("33_5").click()

    driver.find_element_by_id("41_5").click()
    driver.find_element_by_id("42_5").click()
    driver.find_element_by_id("43_5").click()

    driver.find_element_by_id("51_5").click()
    driver.find_element_by_id("52_5").click()
    driver.find_element_by_id("53_5").click()

    driver.find_element_by_id("61_5").click()
    driver.find_element_by_id("62_5").click()
    driver.find_element_by_id("63_5").click()

    driver.find_element_by_id("71_5").click()

    driver.find_element_by_xpath("/html/body/div/div/section[1]/form/div/button").click()


url = "https://ceq.nkust.edu.tw/"
user = input("studentID: ")
passWord = input("password: ")
option = webdriver.ChromeOptions()  # 不要出現自動化工具
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(chrome_options=option)
driver.get(url)
driver.find_element_by_id("UserAccount").send_keys(user)
time.sleep(2)
driver.find_element_by_id("Password").send_keys(passWord)
time.sleep(2)
driver.find_element_by_id("Login").click()
time.sleep(2)
driver.find_element_by_class_name("pull-right-container").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[2]/ul/li/a/span[2]").click()  # click期末問卷調查
time.sleep(2)
allSubject = driver.find_elements_by_xpath("//td/a[@href]")  # find how many subject you have
print(len(allSubject))
time.sleep(2)
for i in range(1, len(allSubject) + 1):
    driver.find_element_by_xpath("/html/body/div/div/section[2]/div[3]/div/div/div[2]/table/tbody/tr[" + str(int(i)) + "]/td[4]/a").click()
    clickAll()
    time.sleep(2)
driver.quit()