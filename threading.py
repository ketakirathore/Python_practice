from threading import *

import threading 
#print(threading.active_count()) = 1 active threading
#print(threading.main_thread()) = main thread number

#syntax for creating thread
#t = threading.Thread(target,args)
#t.start()
#t.join()

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
t1 = hi()      
t1.start()      
t2 =hello()
t2.start()
t2.join()
t1.join()

