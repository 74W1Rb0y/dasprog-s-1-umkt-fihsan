a =["naga",2,3]
print(list(a))
#deklarasi dan format list 
#format list bisa di isi data string atau integer
list0 = [1,2,3,4,5]
a = len(list0)
print(a)
b = min(list0)
print(b)
c = max(list0)
print(c)

#extend  metode
list1 = [1,2,3,4,5]
list1.extend([7,9])
print(list1)

#insert
list2 = [1,2,3,4,5]
list2.insert(3,"peler")
print(list2)

#pop
list3 = [1,2,3,4,5]
list3.pop()
print