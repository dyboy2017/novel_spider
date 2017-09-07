# 名称：爬取小说内容
# 作者： DYBOY 小东
# 时间： 2017-09-07

'''
小说地址：http://www.quanshuwang.com/book/44/44683/
小说章节第一章：http://www.quanshuwang.com/book/44/44683/15379609.html
                http://www.quanshuwang.com/book/44/44683/15379610.html
                http://www.quanshuwang.com/book/44/44683/15380350.html

'''

import requests

from bs4 import BeautifulSoup
#以上作为基本引用

#返回小说详情页的标题+内容
def getContent(content_url):
    res = requests.get(content_url,timeout=10)
    res.encoding = 'gbk'
    soup = BeautifulSoup(res.text,'html.parser')
    title = soup.select('.jieqi_title')[0].text.lstrip('章 节目录 ')
    content = soup.select('#content')[0].text.lstrip('style5();').rstrip('style6();')
    both = title + content
    return both

def urlChange():
    i=0
    f = open("dldl.txt", 'w+',encoding='utf-8')
    url='http://www.quanshuwang.com/book/44/44683/153'
    for num in range(79609,80350):
        curl = url + str(num) + '.html'
        contents = getContent(curl)
        print(contents,file = f)
        i=i+1
        print(i)
    f.close()
    print('ok!!!')

#MAIN--
urlChange()
        
