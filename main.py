import tool
def main():
    while True:
        tool.screen_show()

        action_str = int(input("请选择希望执行的操作："))

        print("您执行的操作是[%d]"%action_str)

        if action_str==1:
            #TODO 填写页数
            root = r"%s"%input("请输入目标文件夹：")
            tool.screen_downloader()
            slect = int(input("\n请输入数字："))
            if slect == 0:
                continue
            elif slect == 1:
                for i in range(int(input("起始页：")), int(input("终止页:")) + 1):
                    url = 'http://174.127.195.166/forum/forumdisplay.php?fid=31&filter=type&typeid=653&page='+'%d'%i
                    list_url = tool.get_every_novel_url(url)
                    for novel_url in list_url:
                        tool.download_txt(novel_url,root)
            elif slect == 2:
                for i in range(int(input("起始页：")), int(input("终止页")) + 1):
                    url = 'http://174.127.195.16/forum/forumdisplay.php?fid=31&filter=type&typeid=358&page=' + '%d'%i
                    list_url = tool.get_every_novel_url(url)
                    for novel_url in list_url:
                        tool.download_txt(novel_url,root)
            elif slect == 3:
                for i in range(int(input("起始页：")), int(input("终止页")) + 1):
                    url = 'http://174.127.195.16/forum/forumdisplay.php?fid=31&filter=type&typeid=167&page=' + '%d' % i
                    list_url = tool.get_every_novel_url(url)
                    for novel_url in list_url:
                        tool.download_txt(novel_url, root)
            elif slect == 4:
                for i in range(int(input("起始页：")), int(input("终止页")) + 1):
                    url = 'http://174.127.195.16/forum/forumdisplay.php?fid=31&filter=type&typeid=463&page=' + '%d' % i
                    list_url = tool.get_every_novel_url(url)
                    for novel_url in list_url:
                        tool.download_txt(novel_url, root)
            elif slect == 5:
                for i in range(int(input("起始页：")), int(input("终止页")) + 1):
                    url = 'http://174.127.195.16/forum/forumdisplay.php?fid=31&filter=type&typeid=357&page=' + '%d' % i
                    list_url = tool.get_every_novel_url(url)
                    for novel_url in list_url:
                        tool.download_txt(novel_url, root)
            elif slect== 6:
                for i in range(int(input("起始页：")), int(input("终止页")) + 1):
                    url = 'http://174.127.195.16/forum/forumdisplay.php?fid=31&filter=type&typeid=46&page=' + '%d' % i
                    list_url = tool.get_every_novel_url(url)
                    for novel_url in list_url:
                        tool.download_txt(novel_url, root)
            else:
                print("输入错误")

        elif action_str==0:
            print("欢迎再次使用[sis爬取小说系统] V 1.1")
            break
if __name__ == "__main__":
    main()