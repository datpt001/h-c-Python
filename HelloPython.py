''' 
Chú thích đầu file, ghi gì thì gi!
'''

#HelloWorld
print ( " Hello World")
print ( "Hello Python")
print ( "This is a traingal")
print ("    /\ ")
print ("   /  \ ")
print ("  /    \ "  )
print (" /      \  ")
print ("/________\ ")

#Variable

#Personal Information
my_name = " Pham Thanh Dat"
age = "16"
iq = " infinity"
print("Name: " + my_name)
print("Age: " + age)
print( "iq: " + iq)

#type of variable
print ( type (my_name))
print ( type (age))
print ( type (iq))

#Kieu Du Lieu so trong python
a = 9.6 # float
print (a)
print (type(a))
b = 10 #interger
print (b)
print (type(b))
c = 1.34342343534534534534543535453453555555555555553453453453453534 #Python chỉ hiển thị chính xác 15 chũ số thập phân
print(c)

#Use Decimal mode, import decimal
from decimal import * # '*' is everything in Decimal library
getcontext().prec = 30 # lấy tối đa 30 chữ số thập phân, Remember this command
e = Decimal(10)/Decimal(3) #Remember to capitalize on letter ' D ' in 'Decimal', 'Decimal (number)' is required
print ( e)
#Decimal divide to a float or interger is Decimal
f = Decimal(10)/3
print(f)
print(type (f))
#Create a fraction
#Import fraction lib
from fractions import *
frac1 = Fraction(17,8)
frac2 = Fraction(5,9)
print ( frac1)
print ( frac2+frac1)

#complex (số phức)





#range, loop, for ..... in
a = range(10)
for i in a:      
    print (i)
#print more in 1 line
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:   #bắt buộc có dấu ':' trong dòng for .... in
    print ("Hello World")
#hoặc có thể viết là
for i in [-10, 10, 2,5]:   #[start, stop, step]
    print("Phạm Thành Đạt")
#phía dưới dòng for in có cách thì thuộc dòng này còn xóa đi dấu cách thì độc lập và không thuộc dòng này
for chao in "HelloWorld":
    print(chao) #in từng chữ trong 'Hello World'

#While loop
#while <condition>:
#         <statements>
number = 0
while number < 10:  #bắt buộc ':'
    print (number)
    number +=2
#break and continue
number = range (998797987987)
for i in number:
    if i > 10:
        break # dừng lại ngay khi lớn hơn 1000
    print (i)
# Program to show the use of continue statement inside loops
#bỏ qua 6
number = range(8)
for i  in number :
    if i == 6:
        continue
    print(i)

#String in python
#nháy đơn ' '
#nháy kép " "
#Moreover, ''' ''' and """ """
#tại sao lại có nháy khác nhau?
# -Vì có thể trong string có dấu nháy không dùng trùng được với dấu nháy của code.
#Ví dụ

print( "I'm a beginner ")
str_của_tôi=''' 
I'm a beginner
I'm a mess
I'm a loser
I'm a hater '''
print(str_của_tôi)
#bản chất của nó là 1 dấu enter bằng \n xuống dòng (escape sequence "\")

#CHUỖI TRẦN
print(r'haizz, \neu hom nay khong phải làm bài tập') #thêm r đằng trước
#không thêm thì
print('haizz, \neu hom nay khong phải làm bài tập')

print('\a') # kêu tiếng beep
print('pham thanh dat\b') #backspace
print('Pham Dat \nThanh') #newline
print('pham thành abc \tđạt hahahaa') #print a horizontal tab

#Toán tử cộng trong string
strA = "Pham Thanh "
strB = "Dat"
strC = strA + strB
print (strC)

#Toán tử nhân
strE = "AI \n"
strD = strE*10
print ( strD)

#True False in string
strF = "fsdlfsdfhsdlfhsdhkldghdfgdfghcklhbkcvhHKJHKHHFIUSHFSDUIFHSDUIFH"
strZ = "a"
strX = strZ in strF
print (strX)

#lấy chữ ở 1 vị trí
strF = "fsdlfsdfhsdlfhsdhkldghdfgdfghcklhbkcvhHKJHKHHFIUSHFSDUIFHSDUIFH"
strZ = strF[8]
print (strZ)

strB = strF[len(strF) - 1] #len() dùng để hiểu thị số kí tự trong string
print(strB)
print(len(strF))