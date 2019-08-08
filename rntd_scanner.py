# coding=utf-8
import json
import time
import requests


class Scan(object):
    def __init__(self, st, end):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'pd.rntd.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        self.st = st
        self.end = end

    def run(self, path):
        try:
            wd_list = open(path, 'r', encoding='utf8').readlines()
        except Exception:
            wd_list = open(path, 'r', encoding='gbk').readlines()
        for wd in wd_list:
            wd = self.st + wd.replace('\n', '') + self.end
            url = 'http://pd.rntd.cn/interface/search/SearchDomian.php?callback=addCouponCallback&sDomain={}.%E6%89%8B%E6%9C%BA&Flag=true'.format(
                wd)
            resp = requests.get(url, headers=self.headers)
            json_data = json.loads(resp.content.decode().replace('addCouponCallback(', '')[:-1])
            while 'LIMIT' in json_data['data']:
                time.sleep(10)
                try:
                    self.headers['Cookie'] = resp.headers['Set-Cookie'].split(';')[0]
                except Exception:
                    pass
                resp = requests.get(url, self.headers)
                json_data = json.loads(resp.content.decode().replace('addCouponCallback(', '')[:-1])
            if 'NOT FOUND' not in json_data['data']:
                print('rntd保留或者注册了：', wd)
                try:
                    open('rntd注册了.txt', 'a', encoding='utf8').write(wd + '\n')
                except Exception:
                    open('rntd注册了.txt', 'a', encoding='gbk').write(wd + '\n')
                # 注册了
                continue
            else:
                print('rntd未注册', wd)
                try:
                    open('rntd未注册.txt', 'a', encoding='utf8').write(wd + '\n')
                except Exception:
                    open('rntd注册了.txt', 'a', encoding='gbk').write(wd + '\n')


if __name__ == '__main__':
    st = input('开头：')
    end = input('结束：')
    s = Scan(st, end)
    path = input('输入字典文件名:')
    s.run('./{}.txt'.format(path))
