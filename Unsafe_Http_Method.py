import requests
import json
header={'Host': 'cn.made-in-china.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Referer': 'https://www.baidu.com/link?url=W9OZPLxn3EW1k38J5b5FeRLyeRnsLq6M2uRzSaePPdpLzGF_MUHDriQv57jJ7evc&wd=&eqid=80b9a9f500218737000000065d526331',
'Connection': 'close',
'Cookie': 'pid=TguMjQwLjI2LjIwMzIwMTkwODEzMTQ0OTM1NzgxNzE0MzIwNzYN; Hm_lvt_dcd77103e55fb7327c5d9c24690a3d89=1565678977; _visit_times_=YAHVj+jfk12B5uh5HjQ37A==; sf_img=AM; __utma=144487465.1418075219.1565678996.1565678996.1565678996.1; __utmb=144487465.3.10.1565678996; __utmz=144487465.1565678996.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; se=TguMjQwLjI2LjIwMzIwMTkwODEzMTUxNDAyOTc1OTA5NjMxNzgN',
'Upgrade-Insecure-Requests': '1',
'If-Modified-Since': 'Tue, 13 Aug 2019 06:54:15 GMT',
'If-None-Match': 'GUDknC'
}
url='https://cn.made-in-china.com/'

#向服务器发送option报文以
response=requests.options(url=url,headers=header)
a=response.headers
#print (a)
b = []
i = 1
#循环遍历回复报文的http头
for key in a:
    if 'Allow' in key:
        b = []
        b = a[key]
#如果报头中存在delete说明存在危险的http方法
        if 'DELETE' in b:
            print ('存在危险的http方法')
        else :
            print ('不存在危险的http方法')
    else:
        print ('不存在危险的http方法')