# -*- codeing = utf-8 -*-
# Zhe

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import xlwt
from selenium.webdriver.chrome.options import Options
import math

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
wd = webdriver.Chrome(options=chrome_options)



wd.implicitly_wait(1)
print(wd.title)


# print('开始')
# sleep(1)
# #点击sign in
# SignIn = wd.find_element(By.XPATH,'//div[@class="d-none d-lg-block"]/button[@class="d-flex align-items-center justify-content-center p-0 m-0 HeaderStyles__signInButton"]')
# SignIn.click()
# #登录模块
# sleep(5)
# username = wd.find_element(By.XPATH,'//input[@id="modalUserEmail"]')
# password = wd.find_element(By.XPATH,'//input[@id="modalUserPassword"]')
# inbott = wd.find_element(By.XPATH,'//form[@name="emailSignInForm"]//button[@type="submit"]')
# sleep(1)
# username.send_keys('850059929@qq.com')
# sleep(1)
# password.send_keys('Diandian213zz')
# sleep(1)
# inbott.click()
# sleep(1)
# coo = wd.get_cookies()
# print(coo)
#
# print('登陆完成')


#创建一个excel表
print('创建表格')
Book = xlwt.Workbook(encoding='utf-8',style_compression=0)
WorkSheet = Book.add_sheet(sheetname='招聘信息',cell_overwrite_ok=True)
col = ('Time','Title','SubTitle','Declined Offer','Neutral Experience','Average Interview','Application','Interview','InterviewQuestions')
for i in range(0,9):
    WorkSheet.write(0,(i+1),col[i])

#全局变量，表格序号
orderNum = 1

#开始获取数据



#判定总共多少页
    #先捕捉总评论数
ViewingNum = wd.find_element(By.XPATH,'//div[@class="paginationFooter"]')
ViewingNum = ViewingNum.text
ViewingNum = str(ViewingNum)
ViewingNum = ViewingNum.replace(',','')
n = ViewingNum.find('of')
m = ViewingNum.find('In')
ViewingNum = ViewingNum[n+3:m-1]
ViewingNum = int(ViewingNum)
print('开始爬取')
#求出需要的总页数
PageNum = (ViewingNum / 10)
PageNum = math.ceil(PageNum) - 1
#print(PageNum)
flag = 1


try:
        #总共循环PageNum页
    for i in range(0,PageNum):
        sleep(2)
        #获取一页的数据
        cells = wd.find_elements(By.CSS_SELECTOR,".css-jp00ku > .mt-0")
        print('开始获取第%d页'%(i+1))
        for cell in cells:
            #print(cell)
            #print('******************')
            #print(cell.text)
            print('输出第%d个元素'%orderNum)
            Data = []
            Time = cell.find_elements(By.CSS_SELECTOR,'.mt-0 >time')
            Title = cell.find_element(By.CSS_SELECTOR,'.row >.col-12 h2 >a')
            SubTitle = cell.find_element(By.CSS_SELECTOR,'.row >.col-12 > p')
            Application = cell.find_element(By.CSS_SELECTOR,'.row >.col-12 div:nth-child(4) p')
            Interview = cell.find_element(By.CSS_SELECTOR,'.row >.col-12 div:nth-child(4) > p')
            InterviewQuestions = cell.find_elements(By.CSS_SELECTOR,'.row >.col-12 div:nth-child(4)  li.mb-std > span')
            if len(Time)==0:
                Data.append('none')
            else:
                Data.append(Time[0].text)
            Data.append(Title.text)
            Data.append(SubTitle.text)
            Review_1 = cell.find_elements(By.CSS_SELECTOR,'.d-block:nth-child(1) >.d-flex >span')
            Review_2 = cell.find_elements(By.CSS_SELECTOR,'.d-block:nth-child(2) >.d-flex >span')
            Review_3 = cell.find_elements(By.CSS_SELECTOR,'.d-block:nth-child(3) >.d-flex >span')
            #判断好、中、差 好是'hcqxoa'   差是'1kiw93k'   中是'1h93d4v'
            if len(Review_1)==0:
                Data.append('none')
            else:
                star_1 = Review_1[0].get_attribute('class')
                if 'hcqxoa' in star_1:
                    Data.append('good')
                elif '1h93d4v' in star_1:
                    Data.append('neutral')
                else:
                    Data.append('bad')
            if len(Review_2)==0:
                Data.append('none')
            else:
                star_2 = Review_2[0].get_attribute('class')
                if 'hcqxoa' in star_2:
                    Data.append('good')
                elif '1h93d4v' in star_2:
                    Data.append('neutral')
                else:
                    Data.append('bad')
            if len(Review_3)==0:
                Data.append('none')
            else:
                star_3 = Review_3[0].get_attribute('class')
                if 'hcqxoa' in star_3:
                    Data.append('good')
                elif '1h93d4v' in star_3:
                    Data.append('neutral')
                else:
                    Data.append('bad')



            Data.append(Application.text)
            Data.append(Interview.text)
            #面试问题有时没有，所以要判定
            if len(InterviewQuestions) == 0:
                Data.append('None')
            else:
                Data.append(InterviewQuestions[0].text)
            #开始存入excel表格
            for j in range(0,len(Data)):
                WorkSheet.write(orderNum, 0, orderNum)
                WorkSheet.write(orderNum, (j + 1), Data[j])
                # Book.save(filename_or_stream='信息.xls')
            orderNum = orderNum + 1
        #点击下一页
        print('成功输出第%d'%(i+1))
        sleep(1)
        # 判定是否最后一页
        selected = wd.find_element(By.CSS_SELECTOR, '.gdGrid .selected')
        if str(PageNum + 1) == selected.text:
            print('是最后一页，完成')
            break
        else:
            # 点击下一页
            Button = wd.find_elements(By.XPATH, '//*[@class="SVGInline-svg navIcon-svg css-g9i05x-svg e13qs2073-svg"]')
            NextButton = Button[1]
            NextButton.click()

except:
    #A = '招聘'
    #B = '信息.xls'
    #C = A + str(flag) + B
    Book.save(filename_or_stream='招聘信息.xls')
    #if i!=10


Book.save(filename_or_stream='招聘信息.xls')