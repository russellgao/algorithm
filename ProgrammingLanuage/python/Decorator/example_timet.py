#!/usr/bin/env python
import functools
import time
from datetime import datetime


def timet(*args, **kwargs) :
    print("装饰器参数 =====")
    for item_a in args :
        print(item_a)
    for item_k ,item_v in kwargs.items() :
        print(item_k,item_v)
    print("装饰器参数------")

    def outter(func) :
        print("otter=====")
        @functools.wraps(func)
        def inner(*args, **kwargs) :
            start_time = datetime.now()
            print("inner====")
            func(*args, **kwargs)
            end_time = datetime.now()
            print("total cost {}".format(end_time - start_time))
        return inner
    return outter

@timet("p1","p2",p3="oirei",p4="uryhd")
def p_p1(a1,a2,a3 = "pkfjf") :
    print("=====")
    print(a1)
    print(a2)
    print(a3)
    print("======")
    time.sleep(4)

p_p1("a1111111","a22222")

print()
