#!/bin/env python
# -*- coding:utf-8 -*-

#쳲���������
first_number = 0
second_number = 1

print(first_number,second_number,end=' ')

for i in range(1,11):
    #�ӵ�3������ʼ����ǰ��ֵ�ĺ�
    sum_number = first_number + second_number
    print(sum_number,end=' ')
    
    #����ֵ
    first_number,second_number = second_number,sum_number
