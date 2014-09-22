shoplist = ['a', 'b', 'c', 'd', 'e']
print shoplist
for i in shoplist:
    print i
shoplist.append('g')
print shoplist
shoplist.append('f')
shoplist.sort(cmp=None, key=None, reverse=False)
print shoplist
del shoplist[0]
print shoplist[0]

zoo=('1','4','2')
print zoo
print 'len zoo',len(zoo)
print 'zoo 0 is  ',zoo[0]

dic={
     'a':'a value',
     'b':'b value'
     
     }
print 'dic:',dic

print 'dic value for key:',dic['a']
for iten in dic:
     print 'iten:',iten,'value :',dic[iten]
mydic=dic
del dic['a']
print 'mydic',mydic
print 'dic',dic