import requests
import os
import lxml,re
from bs4 import BeautifulSoup

def screen_show():
        """显示菜单"""
        print("*" * 50)
        print("欢迎使用[sis爬取小说系统] V 1.2")
        print("")
        print("1.爬取小说")
        print("")
        print("0.退出系统")
        print("*" * 50)

def screen_downloader():
    #选择后爬取的内容
    print("+" * 50)
    print("欢迎使用[sis-另类区小说系统] V 1.2")
    print("")
    print("1.gl小说")
    print("2.冰恋小说")
    print("3.futa小说")
    print("4.恋物小说")
    print("5.秀色小说")
    print("6.其他小说")
    print("")
    print("0.返回上级菜单")
    print("+" * 50)

def get_every_novel_url(url):
    try:
        kvs={
            'user-agent':'Chrome/10.0'
        }
        r = requests.get(url,headers=kvs)
        r.status_code
        r.encoding = 'gb18030'
        soup = BeautifulSoup(r.text,'lxml')
        i = []
        #print(soup.select('span > a')) 这个可以用于搜索span下面的a标签
        for p in soup.find_all('span',id=re.compile("thread_")):
            i.append('http://174.127.195.166/forum/'+p.contents[0]['href'])
        return i
    except:
        print("获取当前页面失败")

def download_txt(url,root):
    try:
        kv = {
            'user-agent': 'Chrome/10.0'
        }
        r = requests.get(url, headers=kv,timeout=10)
        r.status_code
        r.encoding = 'gb18030'
        soup = BeautifulSoup(r.text, 'lxml')
        text_beat = soup.find_all('div', 't_msgfont')
        text = BeautifulSoup(str(text_beat), 'lxml')
        print(soup.title.string)
        path = root + soup.title.string + '.txt'
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                for each in text.div.text.replace('\xa0', ''):
                    f.write(each)
                f.close()
            print("文件已保存")
        else :
            print('文件已存在')
    except:
        print("小说下载失败")


