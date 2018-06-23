# 名称：爬取小说内容 V1.2
# 作者： DYBOY 小东
# 时间： 2018-06-21
# 博客： https://blog.dyboy.cn
# 说明： 1.在1.1版本的基础上增加了异常抛出，更加稳定；2.去掉标题重复抓取的BUG；3.非递归调用，优化程序运行效率，占用内存极小；4.速度明显提升。


'''
小说地址：http://www.quanshuwang.com/book/44/44683/
小说章节第一章：http://www.quanshuwang.com/book/44/44683/15379609.html
                http://www.quanshuwang.com/book/44/44683/15380350.html

'''


import requests
import re
from bs4 import BeautifulSoup
#以上作为基本引用


#全局变量
start_url = "http://www.quanshuwang.com/book/164/164748/45975148.html" #小说第一章对应的URL 例如：http://www.quanshuwang.com/book/44/44683/15379609.html

file_name = "csffsy.txt"  #设置保存的文件名字 建议数字或者英文名字，例如 重生于非凡岁月 可设置为 csffsy.txt

#使用的时候只需要更改上面两个变量的值即可



header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
count = 0 # 计数器 计数章节数


# function： 获取每章节的小说文字并写入文件中
def getContent(content_url):

    global count
    count = count +1 #计数器增加
    
    res = requests.get(content_url,headers = header,timeout = 10)
    res.encoding = 'gbk'
    
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.select('.jieqi_title')[0].text.lstrip('章 节目录 ') #获取章节题目
    content = soup.select('#content')[0].text.lstrip('style5();').rstrip('style6();') #获取章节内容
    both = title + content

    print(both,file = f) #写入文件
    print("已下载 第"+str(count)+"章") #输出到屏幕提示 状态
    
    next_url = soup.select('.next')[0]['href']  #获取下个章节URL
    
    if(next_url.split('/')[3] != 'book'):
        return False
    return getContent(next_url)



#MAIN
if __name__ == '__main__':
    f = open(file_name, 'a+',encoding='utf-8')
    getContent(start_url)
    f.close()
    print('小说下载完成!')
