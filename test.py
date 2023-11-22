"""
多行注释
多行注释
"""

# 单行注释

print('零基础')
print('学python')
print('月薪过万')
print(12.13)

# 变量 程序运行时，记录数据用的
money = 50
print("余额还有:",money)
money = money - 10
print('买了冰淇淋花了10元,还剩余：',money)

# 验证数据类型
print(type(12.13))
print(type(1213))
print(type('1213'))

# 使用变量存储type 语句的执行结果
string_type = type('1213')
int_type = type(1213)
float_type = type(12.13)
print(string_type,int_type,float_type)

# 查看变量中存储的数据类型
name = "1213"
print(type(name))

# 将数字转化成字符串
num_str = str(1213)
print(type(num_str),num_str)

# 将字符串转换成数字
int_num = int('1213')
print(type(int_num),int_num)

# 整数转换成浮点数
float_num = float(1213)
print(type(float_num),float_num)

# 浮点数转化为整数, 会缺少精度
num = int(12.13)
print(type(num),num)