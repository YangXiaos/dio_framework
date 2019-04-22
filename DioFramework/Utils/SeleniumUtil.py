# @Time         : 19-2-17 下午1:03
# @Author       : DioMryang
# @File         : SeleniumUtil.py
# @Description  :
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def getChromeDriver():
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument(("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like"
                              " Gecko) Chrome/72.0.3626.96 Mobile Safari/537.36"))
        options.add_argument('proxy-server=' + "http://127.0.0.1:8888")
        options.add_argument("--ignore-ssl-errors=true")
        driver = webdriver.Chrome(executable_path="/home/mryang/Temp/chromedriver", chrome_options=options)
        driver.get("https://main.m.taobao.com/mytaobao/index.html?spm=a215s.7406091.toolbar.i2")
        time.sleep(4)
        driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        driver.find_elements_by_css_selector("#username")[0].send_keys("13727504102")
        driver.find_elements_by_css_selector("#password")[0].send_keys("676592CCyok")
        time.sleep(3)
        driver.find_elements_by_css_selector("#btn-submit")[0].click()
        time.sleep(2)
        print(driver.get_cookies())
        # PC 端方案
        # driver.find_element_by_id("J_Quick2Static").click()
        # time.sleep(1)
        # driver.find_element_by_name("username").send_keys("13727504102")
        # driver.find_element_by_name("password").send_keys("676592CCyok")
        # # ActionChains(driver).drag_and_drop_by_offset(driver.find_element_by_id("nc_1_n1z"), 400, 0).perform()
        # driver.find_element_by_class_name("W_btn_g").click()
        # time.sleep(9)
        # driver.find_element_by_class_name("weibo-login").click()
        # time.sleep(3)
        # driver.find_element_by_class_name("W_btn_g").click()
        driver.current_url
    except Exception as e:
        pass
    finally:
        if driver is None:
            driver.close()
            driver.quit()


if __name__ == '__main__':
    getChromeDriver()
