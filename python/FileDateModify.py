#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,time
from stat import *
filename='/Users/lane/Desktop/untitled'
#指定期望修改后的时间
TimeForChange = '2107-01-10 07:51:21'
#转换时间格式为long型
ConverTime = time.mktime(time.strptime( TimeForChange,'%Y-%m-%d %H:%M:%S') )
print TimeForChange+' 转换后：'+str(ConverTime)

print '-------------修改前----------------'
#创建时间
print '创建时间  '+time.ctime(os.path.getctime(filename))
#最后修改时间
print '修改时间  '+time.ctime(os.path.getmtime(filename))
#访问时间
print '访问时间  '+time.ctime(os.path.getatime(filename))

#修改文件时间戳
times=(ConverTime,ConverTime)
#进行修改
os.utime(filename, times)

print '-------------修改后----------------'
#创建时间
print '创建时间  '+time.ctime(os.path.getctime(filename))
#最后修改时间
print '修改时间  '+time.ctime(os.path.getmtime(filename))
#访问时间
print '访问时间  '+time.ctime(os.path.getatime(filename))


