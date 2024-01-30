# 列表的下标索引
# 正向 索引   （0,1,2,3,4,……）   反向索引（-n，……-3，-2，-1）
my_list = ["zhangsan","lisi","wanger","mazi"]
print(my_list[0])
print(my_list[2])
# 错误示范 ：不要超出取值范围
#print(my_list[5])

my_list2 = [[1,2,3,4],[9,5,6,7]]
print(my_list2[0][2])

# 在python中，如果将函数定义为class（类）的成员，那么函数称之为：方法

# ----------------------------------------------------------------------
# 列表的查询功能
alist = ["wo",'shi','zhang',['piao','liang']]
index = alist.index("wo") # 查询 wo 在列表中的索引值
#index2 = alist.index("7878") # 不在列中的元素，查询不到会报错ValueError
print(f'wo的索引值是{index}')

# index = alist.index("woq") # 查询的内容在列表中不存在

# 列表的修改
alist[0] = "ni"
print(f"列表中的元素被修改了{alist}")

# 列表的插入
alist.insert(1,'ye')
print(f"列表中的元素被添加了新的元素{alist}")

# 列表的追加

alist.append("ma")  # 只需要传一个参数，插入到列表的最后一位
print(f"列表中的元素被添加了新的元素{alist}")

# 列表追加多个元素
blist = ['?','?','?']
alist.extend(blist)
print(f"列表中的元素被添加了新的元素{alist}")

# 列表 删除元素
# 语法1： del列表下标
# 语法2： 列表.pop(下标)

del alist[-1]
element = blist.pop(0)
print(f"查看两个列表内容{alist},{blist}，取出的元素是‘{element}’")

# 删除某元素在列表中的 第一个匹配项   语法： 列表.remove（元素）
clist = [1,2,3,5,1,2,4,8,9,2]
clist.remove(2)
print(clist)

# 清空列表  语法： 列表.clear()
dlist = [5.6,98,321,88]
dlist.clear()
print(dlist)

# 统计列表中元素的数量 语法： 列表。count（数量）
shuliang= clist.count(2)
print(f'元素数量有{shuliang}')

shuliang2 = alist.count("wo")
print(f'a列表中wo元素有{shuliang2}个')

# 统计列表中全部元素数量  语法： len（列表）
quanbu = len(clist)
print(f'列表中总共有{quanbu}个元素')

# 查找元素xx 在列表中的下标位置
elist = [6,25,87,4,12,53,62,3]
chaxun = elist.index(12)
print(f'元素12在列表中的下标是{chaxun}')
