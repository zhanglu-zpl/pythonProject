# 算术运算符
print('1+1=',1+1)
print('2-1=',2-1)
print('4 / 3=',4 / 3)
print('2**9=',2**9)

# 赋值运算符
num = 1 + 2 * 3
num += 1
num -= 1
num *= 2
num /= 2

# 字符串
# 单引号定义
nume = 'zhanglu'
# 双引号定义
name = "zhanglu1"
# 三引号定义
name3 = """
zhanglu
zhanglu1
zhanglu2
"""
print(type(nume),type(name),type(name3))
# 使用转义字符\，解除引号的效用
name4 = "\"zhanglu"
print(name4)

# 字符串之间的拼接
print("zhang"+'lu')
address = "longaotian"
tel = 1111111
print('woshi ' + name+',woyeshi '+address )
# 字符串拼接不适用于和其他类型拼接
# print('woshi ' + name+',woyeshi '+address + 'wode dianhua '+tel )
# can only concatenate str (not "int") to str

# 通过占位，完成拼接
guxiang = 'neimenggu'
nianling = 29
message = "wo lai zi %s , jinnian %s " % (guxiang,nianling)
print(message)

# 精度控制  m.n  %5d，%5.2f

# 字符串格式化方式 f “内容 {变量}”
name5 = "张璐"
nianling = 1994
tizhong = 66.4
print(f"我是{name5}，我出生于：{nianling}年，我今天体重是：{tizhong}")
# 不会理会类型 不做精度控制

# 对表达式进行格式化

# 
