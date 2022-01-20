from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import pandas as pd
import numpy as np
def DirectionStrToCha(wd):
    wd_dict = {"N":"北风","E":"东风","S":"南风","W":"西风"}
    wd_dict1 = {"NE":"东北风","SE":"东南风","SW":"西南风","NW":"西北风"}
    if len(wd)==1:
       wd_str = wd_dict[wd]
    elif len(wd)==2:
        wd_str = wd_dict1[wd]
    elif len(wd)==3:
        for i in wd:
            if wd.count(i)==2:
                wd_str= "偏"+wd_dict[i]
    return wd_str
def SpeedToLevel(ws):
    ws = float(ws)
    if (ws<=.2)&(ws>=0):
        wslevel = "0级"
    elif (ws<=1.5)&(ws>=0.3):
        wslevel = "1级"
    elif (ws <= 3.3) & (ws >= 1.6):
        wslevel = "2级"
    elif (ws <= 5.4) & (ws >= 3.4):
        wslevel = "3级"
    elif (ws<=7.9)&(ws>=5.5):
        wslevel = "4级"
    elif (ws<=10.7)&(ws>=8.0):
        wslevel = "5级"
    elif (ws<=13.8)&(ws>=10.8):
        wslevel = "6级"
    elif (ws<=17.1)&(ws>=13.9):
        wslevel = "7级"
    elif (ws<=20.7)&(ws>=17.2):
        wslevel = "8级"
    elif (ws<=24.4)&(ws>=20.8):
        wslevel = "9级"
    elif (ws<=28.4)&(ws>=24.5):
        wslevel = "10级"
    elif (ws<=32.6)&(ws>=28.5):
        wslevel = "11级"
    elif (ws <= 36.9) & (ws >=32.7):
        wslevel = "12级"
    return wslevel
browser = webdriver.Chrome(executable_path="F:\webdriver\chromedriver_win32\chromedriver.exe")
browser.set_window_size(3000,2000)#设置窗口大小以保存
browser.get("http://10.127.192.120/index.php")

browser.find_element_by_xpath('/html/body/center/table[3]/tbody/tr[6]/td[1]/li[3]/a').click()
sleep(1)
station = Select(browser.find_element_by_name("tt"))
station.select_by_visible_text("镇江站")
# former_button = browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/center/table/tbody/tr/td[2]/form/input[1]")
date_series =  browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody")
cur_date_str = date_series.text.split(":")[-2].split(' ')[-1]
data_series = browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[last()-2]").text
wdirection =  data_series.split(' ')[11]
wspeed = data_series.split(' ')[12]
temp = data_series.split(' ')[1]
pressure = data_series.split(' ')[23]
humidity = data_series.split(' ')[6]
wd_str = DirectionStrToCha(wdirection)
ws_str = SpeedToLevel(wspeed)


# date.clear()
# date.send_keys("2021-08-09")
# browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/center/table/tbody/tr/td[2]/form/input[5]").click()
# # info = browser.find_element_by_xpath("//*[@id='Layer1']/table/tbody/tr[27]").text
# date = browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/center/table/tbody/tr/td[2]/form/input[4]")
# datestr = date.get_attribute("value")
# while datestr!="2021-10-23":
#     browser.find_element_by_xpath("//center/table/tbody/tr/td[2]/form/input[2]").click()
#     browser.find_element_by_xpath(
#         "//table/tbody/tr/td[2]/form/input[5]").click()
#     date = browser.find_element_by_xpath(
#         "//tr/td[2]/form/input[4]")
#     date_str = date.get_attribute("value")
#     print("正检索:", date_str)
#
#     info1 = browser.find_element_by_xpath("//*[@id='Layer1']/table/tbody/tr[27]").text
#     gw = float(info1.split(" ")[2])
#     dw = float(info1.split(" ")[4])
#     feng = float(info1.split(" ")[-2])
#     yu = float(info1.split(" ")[0])
#     # if gw>=35:
#     #     gaowen =np.r_[gaowen,np.array([date_str,gw]).reshape(1,2)]
#     # if dw<=0:
#     #     diwen=np.r_[diwen,np.array([date_str,dw]).reshape(1,2)]
#     # if feng>=8:
#     #     wind=np.r_[wind,np.array([date_str,feng]).reshape(1,2)]
#     if yu!=0:
#         weather1='有雨'
#     else:
#         weather1='无雨'
#     baoyu = np.r_[baoyu, np.array([date_str, yu, weather1]).reshape(1, 3)]
#
#     print("已检索:",date.get_attribute("value"))
#     datestr = date.get_attribute("value")
# # gaowen = pd.DataFrame(gaowen)
# # diwen = pd.DataFrame(diwen)
# # wind = pd.DataFrame(wind)
# baoyu = pd.DataFrame(baoyu)
# with pd.ExcelWriter(r"C:\Users\admin\Desktop\20211203.xls") as writer:
#     # gaowen.to_excel(writer,sheet_name="高温")
#     # diwen.to_excel(writer,sheet_name="低温")
#     baoyu.to_excel(writer,sheet_name="暴雨")
#     # wind.to_excel(writer,sheet_name="风")


# sleep(1)
# date.send_keys("2020-05-10")
# stations= browser.find_element_by_name("tt").find_elements_by_tag_name("option")
# station_list = []
# for station in  stations:
#     station_list.append(station.text)
# sleep(1)
# browser.save_screenshot(r"C:\Users\admin\Desktop\a.png")
