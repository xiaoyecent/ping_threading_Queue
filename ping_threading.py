'''
Created on 2017-2-28

@author: xiaoye
'''
#coding: utf-8
import time
import sys
import threading
import Queue
from subprocess import Popen,PIPE


class Quethread(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self._que = que
    
    def run(self):
        while not self._que.empty():
            ip = self._que.get()
            process = Popen('ping -c 2 ' + ip, stdin=PIPE, stdout=PIPE, shell=True)
            data = process.stdout.read()
            if 'ttl' in data:
                sys.stdout.write('%s is live %s\n' % (ip, time.strftime('%H:%M:%S')))
    
    
def main():
    que = Queue.Queue()
    ips = raw_input()
    thread = []
    thread_count = 200
    ip_head = '.'.join(ips.split('.')[:3])
    #print ip_head
    for i in range(1, 255):
        que.put(ip_head + '.' + str(i))
    '''for i in range(1,255):
        print que.get()'''
    
    for i in range(thread_count):
        thread.append(Quethread(que))
        
    for i in thread:
        i.start()
        
    for i in thread:
        i.join()
        
    
if __name__ == '__main__':
    main()