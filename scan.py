# coding=utf-8
import requests


class Scan(object):
    def __init__(self,st,end):
        self.st = st
        self.end =end
        pass
    def run(self,path):
        try:
            wd_list = open(path, 'r',encoding='utf8').readlines()
        except Exception:
            wd_list = open(path, 'r', encoding='gbk').readlines()
        for wd in wd_list:
            wd = self.st+ wd.replace('\n', '') + self.end
            url = 'http://whois.wang/whois/?domainName={}.%E5%95%86%E5%9F%8E'.format(wd)
            resp = requests.get(url)
            if 'The queried object does not exist' not in resp.content.decode():
                # 注册了
                print('whois注册了：',wd)
                try:
                    open('whois已注册.txt', 'a',encoding='uf8').write(wd+'\n')
                except Exception:
                    open('whois已注册.txt', 'a', encoding='gbk').write(wd + '\n')
                continue
            else:
                print('whois未注册:',wd)
                try:
                    open('whois未注册.txt','a',encoding='utf8').write(wd+'\n')
                except Exception:
                    open('whois未注册.txt', 'a', encoding='gbk').write(wd + '\n')


if __name__ == '__main__':
    st = input('开头：')
    end = input('结束：')
    s = Scan(st,end)
    path = input('输入字典文件名:')
    s.run('./{}.txt'.format(path))
