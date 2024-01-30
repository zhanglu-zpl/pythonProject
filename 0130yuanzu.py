# 列表是可以修改的  但是元组是只读的，不被篡改
kongyuanzu = tuple()

tuple1 = (1,"hello",True)

# 元组中如果只有一个数据，要加一个,
t4 = ("hello")
print(f"t4的类型是{type(t4)},内容是{t4}")

t5 = ("hello",)
print(f"t5的类型是{type(t5)},内容是{t5}")

# 元组可以嵌套
t6 =((1,2,3),(4,5,6))
print(f"t6的类型是{type(t6)},内容是{t6}")

# 取出下标索引内容
num = t6[1][2]
print(f'从嵌套元组中取出的数据是{num}')

# index 查找方法
t7  = ("wo","shi","zhang","lu",'lu','lu')
index = t7.index("shi")
print(f't7中查找shi的下标是{index}')
# count 统计方法
num1 = t7.count("lu")
print(f't7中lu的数量是{num1}')
# len 总数
num2 = len(t7)
print(f't7中元素的数量是{num2}')


#   ------------------------------------------分割-------------------------------

# 元组的遍历
index = 0
while index < len(t7):
    print(f"元组的元素有{t7[index]}")
    index += 1

for index1 in  t7 :
    print(f"元组的元素有{index1}")
