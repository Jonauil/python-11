#!/bin/env python
# -*- coding:utf-8 -*-
#쳲���������

first_number = 0
second_number = 1
sum_number = 0

print(first_number,second_number,end=' ')

while sum_number <= 100:
    #�ӵ�3������ʼ����ǰ��ֵ�ĺ�    
    sum_number = first_number + second_number
    
    if sum_number <= 100:
        print(sum_number,end=' ')
    
    #����ֵ
    first_number = second_number
    second_number = sum_number
