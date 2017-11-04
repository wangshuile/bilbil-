#!encoding=utf-8
'''
注释:
由于bilbil没有提供视频批量下载的功能所以
本爬虫实现批量爬取bilbil个人空间发布的个人视频

'''
from selenium import webdriver
import time,os
from multiprocessing import Pool
def download__(alist):
    for i in alist:
        os.system("you-get -t 2 %s"%i)
video_list=[]
video_url=raw_input("请输入bilbil爬取个人空间网址:")
browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
browser.get(video_url)
page_info = browser.find_element_by_xpath('//span[@class="sp-pager-total"]')
page_text=page_info.text.split()
page_size=int(page_text[1])
for i in range(page_size):
    video_tmp=video_url+"&order=0&page="+str(i+1)
    print video_tmp
    browser.get(video_tmp)
    time.sleep(6)
    page_info = browser.find_elements_by_xpath('//a[@class="cover cover-normal"]')
    for i in page_info:
        j=str(i.get_attribute("href"))
        video_list.append(j)
    print len(video_list)
download__(video_list)



