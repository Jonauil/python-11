#!/bin/env python
# -*- coding:utf-8 -*-

#����ģ��
import random,string


lst = []
length = 0
while length < 10 :
    #���������
    number = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    #������ɵ��������б��о�׷�ӽ�ȥ
    if number not in lst:
        lst.append(number)
        length += 1
    print(number)
