from selenium import webdriver
import time, re
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup

class login(object):
    def __init__(self, ID=None, user_name=None, ID_card = None):
        self.ID = ID
        self.user_name = user_name
        self.id_card = ID_card
        self.filename = '1.jpg'
        self.url = "http://fpkf.gxi.gov.cn:7017/gxfpw/portal/loginAction!toFindJdlk.front"
    def vcode(self):
        threshold = 140
        table = []
        for i in range(256):  # 图像降噪算法，像素点0，1添加
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        im = Image.open(self.filename)
        width, height = im.size
        box = (590, 359, width - 345, height - 306)
        region = im.crop(box)
        region.save('code.jpg', 'JPEG')
        image = Image.open('code.jpg')
        imgry = image.convert('L')  # 灰化图片
        out = imgry.point(table, '1')  # 图像降噪
        vcode = pytesseract.image_to_string(out)
        return vcode
    def string(self, code):
        code = code.replace(' ', '')
        return code
    def main(self):
        driver = webdriver.PhantomJS()
        driver.get(url=self.url)
        print("等待2秒")
        time.sleep(2)
        driver.get_screenshot_as_file(self.filename)
        code = self.vcode()
        code = self.string(code)
        driver.find_element_by_name('user.vcode').send_keys(str(code))  # 验证码输入框
        driver.find_element_by_name('user.realName').send_keys(str(self.user_name))# 姓名登录框
        driver.find_element_by_name('user.idcard').send_keys(str(self.id_card))# 身份证号输入框
        driver.find_element_by_class_name("btn_cx").click()
        print("等待3秒")
        time.sleep(3)
        content = driver.page_source
        soup = BeautifulSoup(content, 'lxml')
        s1 = soup.find_all('div', class_='messager-body panel-body panel-body-noborder window-body')
        text = re.findall('(?<=<div>).*?(?=</div>)', str(s1[0]))
        driver.get_screenshot_as_file('screen_file/'+str(self.ID)+'.jpg')
        if len(text[0]) == 8:
            print(text[0])
            print("验证码错误，重新递归验证")
            driver.close()
            a = self.main()
            return a
        elif len(text[0]) < 16:
            print(text[0])
            return text[0]
        elif len(text[0]) > 20:
            print(text[0])
            stri = str(text[0]).split("，", 1)
            return stri[0]



