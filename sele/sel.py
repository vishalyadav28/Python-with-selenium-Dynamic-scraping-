# import PIL
# from PIL import Image
# import pytesseract
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH='/home/mobcoder/Desktop/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.maximize_window()



# def login():
#     driver.get("https://bvincap.skyexchange.com/exchange/member/gameHall.jsp")


#     driver.save_screenshot("captcha.jpg")

#     im = Image.open('/home/mobcoder/Desktop/sele/captcha.jpg')
#     left = 1650
#     top = 15
#     right = 1710
#     bottom = 50
    
#     # # Cropped image of above dimension
#     # # (It will not change original image)
#     im1 = im.crop((left, top, right, bottom))
#     # im1.show()
#     # ===============>
#     verify_code = pytesseract.image_to_string(im1, config='--psm 6')
#     # time.sleep(1)

#     print('verify_code ==== ',verify_code)
#     # time.sleep(1)
#     new_verify_code=''.join(e for e in verify_code if e.isnumeric())
#     # time.sleep(1)

#     print('++++++++++++++++++++++')
#     print(new_verify_code)
#     print('++++++++++++++++++++++')




#     driver.find_element_by_id("loginName").send_keys('demosob1')
#     driver.find_element_by_id("password").send_keys('Abcd1234')
#     # time.sleep(2)

#     driver.find_element_by_id("validCode").send_keys(new_verify_code)
#     driver.find_element_by_id("loginBtn").click()
#     time.sleep(5)
#     driver.close()
    


# login()
def temp():
    driver.get('https://transparency-in-coverage.uhc.com/')
    time.sleep(20)
    driver.close