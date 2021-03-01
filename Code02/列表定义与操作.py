#1. 定义列表
age = 9
name = ["tom","ming","jack",22,age]  #列表里面的参数叫元素  

#2. 取参数
print("01",name[0])    #取出tom  
print("02",name[-1])   #取出最后一个  
print("03",name[0:2])  #取出一部分，可以取出0对应的元素，不能取出2对应的元素  
print("04",name[-2:])  #不加结束，默认可以取到最后一个参数  
print("05",name[:3])   #or name[0:3] #取出前3个  

#3. 切片，一次取出多个值
print("06",name[:4][2:4][0])

#4. 修改
name[1] = "nom"  
print("07",name)

#5. 插入insert
name.insert(2,'hell')  
print("08",name)

#6. 追加append
name.append("mingming")  
print("09",name)

#7. 删除remove
name.remove("hell")
print("10",name)
#（1）一次性删除多个元素
del name[2:4]  #del是从内存中删除  
print("11",name)
#（2）步长
name[0:-1:2] 
name[::2] #后面的2是步长，跨过2个元素，往下取（默认迈一步） 

#8. 扩展extend
b = [1,2,3]  
name.extend(b)  #将b列表加入names列表
print("12",name)

#9. 拷贝copy
name_copy = name.copy()  
print("13",name_copy)

#10. 统计count
name.count("2")  #统计2出现的次数
print("14",name)

#11. 排序sort和反转reverse
#（1）排序列表  
names = [11,8,12,22,1]
names.sort()
print("15",names)
#（2）反转列表顺序
name.reverse()
print("16",name)