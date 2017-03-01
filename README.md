# ping_threading_Queue
threading   Queue
```
python ping_thread.py ip
```
自动扫描该ip所在c段内存活主机    thread模块   速度一般   稳定性一般

```
python ping_threading.py ip
```
自动扫描该ip所在c段内存活主机    threading模块(写了个继承threading.Thread的子类class实现多线程)+Queue实现多线程数据保护   速度较快   稳定性较强
