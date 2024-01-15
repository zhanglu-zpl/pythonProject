# 函数  统计字符串长度
# 函数 是已经组织好的，可重复使用，针对特定的功能，  注意：先定义后调用

str1 = "zhanglu"
str2 = "xuanjiawei"
str3 = "wangfengying"

def my_len(date):
    count = 0
    for i in date :
        count += 1
    print(f"字符串{date}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)

# 定义一个函数，输出相关信息
# 函数返回值 none  -类型为“Nonetype”的字面量，表示空，无实际意义，返回了空
# 在if判断中，None等同于 false
# none 用于生命无初始内容的变量

def say():
    print("什么都没有发生吗？")
r = say()
print(f"返回值内容是{r}，类型是{type(r)}")

# 定义一个函数，带有参数的函数

def hesuan(x,y):
    """
    函数说明
    :param x:第一个相加的数值
    :param y:第二个相加的数值
    :return:判断和是否大于37.3，判断范围给出通行结果
    """
    result = x+y
    if result <= 37.3 :
        return print(f"您的体温是{result}，体温正常可以通行")
    else:
        return print(f"您的体温是{result}，不能通行，需要治疗")

hesuan(3,56)
hesuan(12,23.5)



# 函数的嵌套 在一个函数中调用另一个函数
def fun_b():
    print("--1--")
def fun_a():
    print("--2--")
    fun_b()
    print('--3--')

fun_a()

# 变量作用域 局部变量（出了函数体，局部变量将无法使用）  全局变量

num = 200   #全局变量
def tesa():
     print(num)
def tesb():
    # global 关键字声明"a"是全局变量
    global num
    num = 500
    print(num)

tesa()
tesb()
print(num)

