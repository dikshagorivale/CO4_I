# print("Hello World")      #simple python print 

# '''list=[1,2,3,'yes']        #how to pass comment and list
# a=9
# b=10.9
# c='str'
# print(type(list))     # how to get the type of datatype
# print(type(a))
# print(type(b))
# print(type(c))

# x={1,2,9,6,"asmi",8,5,10}   #set
# print(x)

# school = {                     #dict
#     'stud_name':'Asmi',
#     'stud_no': 114
# }
# print(type(school))


# a = 9              #arithmetic operators
# b = 7
# c=a+b
# d=a-b
# e=a*b
# f=a/b


# print("addition is",c,"subtraction is",d,"multiplication is",e,"division is ",f)     # print using coma

# print(f"add is {c} sub is {d} mul is {e} div is {f}")      #print using fetch {}

# a=9**73      #sqr /to get rasie to  value
# print(a)

# a=73//9                         # div 2 times
# print(a)

# a = 9     #not operator
# b = 3
# print(a!=b)
   
# x = 9              #or operator
# y = 19
# print(x or y)

# a=9                 #identity operator
# if a is 9 :
# print('a is 9')


# list=['asmi',1,2,4,5,'rohini']       #membership operator
# if 'asmi' in list :
# print("abc")'''

# '''a=68
# if 60>a>10:                   #if...else
#      print("a is > 10 and = 5")
# else:
#      print("a is greater than 60")'''

# '''str = int(input("enter val"))        #to pass arg or take arg from user
# print(type(str))'''

# '''a = int(input('enter value of a'))          #if...elif..else  ------calculator
# b = int(input('enter value of b'))
# c = int(input('enter value of c from 1-4'))
# if(c==1):
#     res=a+b 
#     print("addition is",res)
# elif (c==2):
#     res=a-b
#     print("subtraction is",res)
# elif (c==3):
#     res=a*b
#     print("mul is",res)
# elif (c==4):
#     res=a/b
#     print("div is",res)
# else :
#     print("invalid number")'''

# '''list=[1,9,3,2]             #to find median ,lengthof list,med 
# n=len(list)
# med=(n+1)/2
# a=int(med-1)
# median=list[a]
# print(median)'''
# '''sum=0
# for i in len(list):
#     sum= sum + list[i]         #sum=+list[i]
# print(sum)'''

# '''i=0
# passs = 123                  #to check password and unlock phone 
# user_input=int(input("enter password"))
# if ( passs == user_input) :              #condition 1
#     print("unlock")
# else :  
#     while (i<5):                         #condition 2
#         user_input=int(input("enter password"))
#         if ( passs == user_input):        #condition 1 in 2
#             print("unlock")
#             break
#         else :                            # condition else in 2 
#             print("phone lock")
#         i+=1'''


#methods
# '''list=[1,2,3]
# list.append(9)    #add to end
# print(list)
# b=list.copy()     #copy list
# print(b)'''
# '''
# list=[1,9,7]
# list.reverse()    #reverses the order of list 
# print(list)
# list=[1,9,7]
# list.sort()       #sort in asc 
# print(list)'''
# '''list=[1,9,7]
# list.sort(reverse=True)     #reverse the list first then sort it
# print(list)
# list=[1,9,7]
# list.remove(9)           #removes 9 from list
# print(list)
# list=[1,9,7]
# list.insert(4,8)         #insert 8 at 4 index
# print(list)'''
# '''a=4
# del a                 #delete 
# print(a)'''            #o/p will be empty
# '''list=list(set)         #type casting ----converting set into list
# list.copy()
# print(list)
# list.append(9)
# print(list)
# list.clear()              #clear list
# print(list)
# res=list.count('d')          #count how many d are there in list
# print(res)'''
        
# '''list=[1,9,7]
# list.pop(1)                #pop 1 from list
# print(list)'''          #o/p==9,7
# '''
# list=[1,9,7]
# list2=[1,4,7,6]
# list.extend(list2)   #[list1]+[list2]
# print(list2)'''

# '''list=[1,9,7]
# x=list.index(9)     #give index of 9
# print(x)'''


##-------------lecture 3(6/6/24)--------##
# a={1.0,"hello",(1,2,3)}
# print(a)
# print(type(a))
# list=list(a)
# print(list[0])
# print(type(list))

# a={"stu_name":"nimu",      #dic argument
#    "batch_no":"b3"}
# print(a)

# dict={"key":[1,2,3]}       #2d dic argument
# print(dict)

# def c():         #function declaration
#     print("hello")
# c()        #function call

# def c():
#     return("hello")   #return hello
# c()


# s={x:x**3 for x in range(11)}     # comprehension ---writing loop in one line
# print(s)

# x=8
# s={x:x**3 for i in range(1,11)}     # only cube part will be executed as i has been given value as 1 
# print(s)

# s={i:i**3 for i in range(1,11) if(i!=7)}     # comprehension ---writing loop in one line-- two loops(7 will not be executed bcuz of if condition)
# print(s.items())


# list=[x for x in range(2,9) if(x!=7)]    #comprehension with list
# print(list)


# y=5          #x*y using range 
# l=[x*y for x in range (101,121)]
# print(l)


# l=[x for x in range (1,10) if(x%2==0)]       #print even no,=. in given range --- if want sqr of x and also to print even no x*x will be used
# print(l)

# str=list(input("enter a no:"))        #input from user is shown in  list
# print(str)

# list=[]         #print user value by taking len
# n=int(input("enter the length of list:"))
# for i  in range (n):
#     u=int(input(f'{i+1} value'))
#     list.append(u)
# print(list)

# functions


# def green(name):  #print using ,
#     print("hello",name,". Good Morning")
# green("nimu")
    

# def s(x,y):
#     c=x*y
#     return c
#     c=x+y  #null after return
# p=s(2,3)
# print(p)

#add function with user input
# def add():
#     s=0
#     for i in range (0,5):
#         u=int(input(f'{i+1} value:'))
#         s+=u
#     print(s)
#     return s
#     print(s)
# add()

# def s(name,roll_no):           
#     print(f'{name} is roll_no {roll_no}')    #positional arg
# p=s(roll_no=56, name="nimu")                 #keyword arg
# print(p)

# def avg():                 # default argument
#     list=[]
#     n=int(input("enter no of student:"))
#     for i in range(n):
#         a=int(input('age:'))
#         list.append(a)
#         s=sum(list)
#         a=s/n
#         return a
# print(avg())

# def age(*b):      #arbitary argument it is used bcz we dk how many inputs will user give
#     print(b)
#     print(type(b))
# #age([2,3,4])   # answer comes as [2,3,4], as arbitary arg requires more than one value
# #age(2,3,4,5)  # answers comes as tuple (2,3,4,5) as no brackets are given and the bracket are given for the function age
# age([2,3,4],[23,45,6]) 

# def age(**b):      #arbitary keyword argument
#     print(b)
#     print(type(b))  
# age(a=2,b=3,c=4)  # keywords is used to give parameters so answer is in dict {'a': 2, 'b': 3, 'c': 4}

# def add(x,y):    #below code makes the function/operator in one line using lambda
#     c=x+y
#     print(c)
#     return c
# add(2,4)

#lambda                 #writing a function in one line
# add=lambda x,y:x+y   #function=lambda param1,param2: param1+param2     # 
# p=add(4,5)
# print(p)
# sub=lambda x,y:x-y   #function=lambda param1,param2: param1-param2 
# p=sub(4,5)
# print(p)
# mult=lambda x,y:x*y   #function=lambda param1,param2: param1*param2 
# p=mult(4,5)
# print(p)
# divi=lambda x,y:x/y   #function=lambda param1,param2: param1/param2 
# p=divi(4,5)
# print(p)

# def abs_no(num):
#     if num>0:
#         return num
#     else:
#         return -num
# #a=abs_no(4)
# a=abs_no(-2)
# print(a)


##-----------4th lecture(7/6/24)------------##

##list =(1,2,5,6,8)      #slicing method to take a desired part from the list
#list =[1,2,5,6,8]  
#print(list[:4])           #starting_value :(it is used to indicate starting to ending point) ending_value (if ending value is not given it will go till the last of the list same for starting_value)


#continue pass break

# list = [3,2,2,3]
# for i in range(len(list)):
#     print(list[i])
# for i in list:
#     pass     #when uh dont want to do anything just write pass 
#     print(i)

# for i in range(1,11):
#     if i!=7:
#         print(i)
#         break     #terminate the loop doesn't check if there is any instruction further
#     else:
#         continue           #skips the specific iteration


#list=[x for x in range(1,11) if x!=7]   #x(the value which we want to return) for loop second loop  #comprehension
#print(list)

# a="apple"           #example for continue
# for i in a:
#     if a=="p":     
#         continue     #over here p is skipped and further string is printed

#     else:
#         print(i)

# def sam():
#     pass
# sam()

# list=[1,2,3,4,5,6,7,8,9,10,11]
# for i in range(1,11):
#     if i in list:
#         pass
#     else:
#         list.append()

# list.sort()
# print(list)

# name=["asb","ewd","ffr","effe","eeg","err","efr"]
# def search(name):
#     for i in name:
#         if i=="err":
#             print("found")
#         else:
#             print("not found")
# search(name)

#recursive
# list=["asb","ewd","ffr","effe","eeg","err","efr"]
# def find(name,list,i=0):
#     i1=i
#     if list[i]==name:
#         print("found")
#     else:
#         i1=i1+1
#         find(name,list,i1)
        
# find("err",list,0)

###opp

# replace name
# class stu:      #creation of class
#     name="nimu"   #parameters of class
#     r_no=122
#     rank=1
#     def all(self):          #self--default parameter of object---takes the avaliable argument/parameter
#         print(f"{self.name}'s roll no. is {self.r_no} ")    #self access the aavaliable argument from class

# #a=stu()      #object creation
# # #print(a.name,a.r_no)   #object access the class and print it
# # a.name="diksha"        #using object diff value is given to parameters
# # a.r_no=159

# a.all()               #using object function is called
# p=stu()
# p.all()
# p.name="kavya"
# p.all()


##inheritance

# class bird:       #simple inheritance
#     def init_(self):
#         print("bird is ready")
# class penguin(bird):
#     def init_(self):
#         super().init_()
#         print("penguin is ready")
# p=penguin()

# nums=[1,2,3,4,5,6,7,8,9,10]    #to extract list without 6 cpomprehension is used 
# val=6
# list=[nums[i] for i in range (len(nums)) if nums[i] !=val] # checking for ith place of nums by using for loop to take len of nums then if loop is checked where if ith place of nums is not equal to  value to be removed ---loop is executed
# print(list)     # print  nums without 6
# res=[2,4]

