#coding:utf-8
import urllib2

htmldata=urllib2.urlopen('http://so.com').read()
print 'aaa'
print htmldata
print 'bbb'