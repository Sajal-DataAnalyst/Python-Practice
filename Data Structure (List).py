# a=[2,3,4,5,6,7]

# # for i in range(len(a)):
# #     print(a[i])

# for i in a:
#     print(i)    


# l=[-15,8,17,0,-13,-78,-89]
# print('Positive elements are: ')
# for i in l:
#     if i>=0:
#         print(i)
# print('Negative elements are: ')

# for i in l:
#     if i<0:
#         print(i)

# l=[23,54,675,86,545,56,7]

# sum=0

# for i in l:
#     sum=sum+i
# print(f" The mean of your sum is {sum//len(l)} ")


# l=[23,54,675,86,545,56,7]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i] > largest:
#         largest=l[i]
#         index=i
# print(f'Your largest number is {largest} at {index}')      


# l=[12,16,13,19,17]
# largest=l[0]
# second_larg=l[0]

# for i in l:
#     if i > largest:
#         second_larg=largest
#         largest=i
#     elif i>second_larg:
#         second_larg=i


# print(largest,second_larg)

# a=[12,13,14,15,16,12]

# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted")
        
# a ={1,2,3,5}
# a.clear()
# print(a)

# a={1,2,3,4,5}
# b={6,7,8,9,0,5}
# print(a^b)

# d={10:100,20:200,30:300}
# d[50]=500 # update value
# d[10]=1000 #creating value
# del d[30]
# print([d])

# d={10:100,20:200,30:300}
# for i in d.values():
#     print(i)

# d1={10:100,20:200,30:300}
# d2={40:400,50:500,60:600}

# for i in d2:
#     d1[i]=d2[i]
# print(d1)      

# d1={10:100,20:200,30:300}
# sum=0
# for i in d1:
#     sum=sum+d1[i]
# print(sum) 
          

# a=[1,1,1,2,2,2,3,3,3,4,4,4]

# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)        

d1={10:100,20:200,30:300}
d2={30:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)