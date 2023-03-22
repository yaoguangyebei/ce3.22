# count=0
# list1=['张三','李四','王五','赵六','七八','十又','青蛙']
# for name in list1:
#    if name=="王五":
         # break
#     continue
#    print(name)
#    print("*"*20)
#    count += 1
# print(count)
# print(len(list1))
#
# def good_job(s,b,c=300,*args,**kwargs):
#     # s=8000
#     # b=2000
#     # c=500
#     s1=s+b+c
#     for i in args:
#         s1 +=i
#     for j in kwargs:
#         s1 +=kwargs[j]
#     return s1
# result=good_job(8000,2000,800)
# if result>10000:
#     print("很好")
# else:
#     print("一般")
#
#
# print(result)
# # good_job()



# 任意整数序列相加
# 1.
# s=0
# num = int(input("input:"))
# for i in range(num):
#     s += i
#     print(s)
# add_fun(100)

# 2.
# def add_fun(n):
#     s=0
#     for i in range(n):
#         s+=i
#     print(s)
# add_fun(100)

# 定义函数，判断对象（列表，字典，字符串）长度是否大于5，若是输出True，否则False
def function_len(object):
     # if type(object)=dict or type(object)=list or type(object)=str:
    if isinstance(object,str) or isinstance(object,dict) or isinstance(object,list):
        leng=len(object)
        if leng>5:
            print("True")
        else:
            print("False")
    else:
        print("无法计算")
function_len('1,2,3')