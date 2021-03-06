from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

class Skcx():
    def __init__(self):
        self.Inpage()
    def DirectionStrToCha(self,wd):
        wd_dict = {"N":"北风","E":"东风","S":"南风","W":"西风",'-':'-'}
        wd_dict1 = {"NE":"东北风","SE":"东南风","SW":"西南风","NW":"西北风"}
        if len(wd)==1:
           wd_str = wd_dict[wd]
        elif len(wd)==2:
            wd_str = wd_dict1[wd]
        elif len(wd)==3:
            for i in wd:
                if wd.count(i)==2:
                   wd_str= "偏"+wd_dict[i]
        self.wd_str = wd_str
        return self.wd_str
    def SpeedToLevel(self,ws):
        if ws=="-":
            wslevel="-"
        else:
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
        self.wslevel = wslevel
        return self.wslevel

    def Inpage(self):
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe")
        self.browser.set_window_size(3000,2000)#设置窗口大小以保存
        self.browser.get("http://10.127.192.120/index.php")
        self.browser.refresh()
        self.browser.find_element_by_xpath('/html/body/center/table[3]/tbody/tr[6]/td[1]/li[3]/a').click()
        sleep(2)
        station = Select(self.browser.find_element_by_name("tt"))
        station.select_by_visible_text("镇江站")
# former_button = browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/center/table/tbody/tr/td[2]/form/input[1]")
    def Zdsk(self):
        date_series =  self.browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody")
        cur_date_str = date_series.text.split(":")[-2].split(' ')[-1]
        self.data_series = self.browser.find_element_by_xpath("/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[last()-2]").text
        wdirection =  self.data_series .split(' ')[11]
        wspeed =self.data_series .split(' ')[12]
        temp = self.data_series .split(' ')[1]
        pressure = self.data_series .split(' ')[23]
        humidity = self.data_series .split(' ')[6]
        wd_str = self.DirectionStrToCha(wdirection)
        ws_str = self.SpeedToLevel(wspeed)
        self.string_now = "#整点实况# 今日{}时，【天气】，{}{}，气温{}℃，气压{}hpa，相对湿度{}%"\
            .format(cur_date_str,wd_str,ws_str,temp,pressure,humidity)
        return self.string_now
    def Jrsk(self):
        data = self.browser.find_element_by_xpath(
            "/html/body/center/table[3]/tbody/tr[1]/td[2]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[last()-1]").text
        htemp = data.split(' ')[2]
        ltemp = data.split(' ')[4]
        self.string_today='#今日实况# 我市今天【天气说明】，早晨最低气温{}℃，白天最高气温{}℃。'.format(ltemp,htemp)
        return self.string_today

if __name__=="__main__":
    a = Skcx()
    SK_today = a.Jrsk()
    SK_hour = a.Zdsk()


