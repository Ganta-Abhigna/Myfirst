import time
#import threading

def cal_square(l):
    print("Calc square")
    for i in range(len(l)):
        time.sleep(0.2)
        print(i*i)
def cal_cube(l):
    print("Calc cube")
    for i in range(len(l)):
        time.sleep(0.2)
        print(i*i*i)
t=time.time()
l=[1,2,3,4,5]
cal_square(l)
cal_cube(l)
print(time.time()-t)