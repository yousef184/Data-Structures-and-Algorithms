import time

def tik(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2= time.time()
        print(t2-t1)
    return(wrapper)