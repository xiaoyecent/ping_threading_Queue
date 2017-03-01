'''
Created on 2017-2-27

@author: xiaoye
'''
#coding: utf-8
import thread
import time
from subprocess import Popen,PIPE

def scan_ip(ip):
    process = Popen('ping -c 2 ' + ip, stdin=PIPE, stdout=PIPE, shell=True)
    data = process.stdout.read()
    if 'ttl' in data:
        print '%s is live ,now time is %s' % (ip, time.strftime('%H:%M:%S'))
    
if __name__ == '__main__':
    #scan_ip('111.13.147.229')
    ips = raw_input()
    ip_header = '.'.join(ips.split('.')[:3])
    for i in range(1,255):
        ip = ip_header + '.' + str(i)
        #print ip
        thread.start_new_thread(scan_ip, (ip,))
        time.sleep(0.1)

