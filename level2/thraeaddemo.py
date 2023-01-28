from threading import *
import time
def demo_thread():
    time.sleep(3) #after 2 milli seconds it will be print
    print("hello")
demo_thread()
t1=Thread(target=demo_thread())
t1.start()

"""
import threading
print(threading.current_thread().getName())
"""