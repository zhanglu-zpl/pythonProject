# 集合 不支持重复的元素,集合是无序的，不支持下标索引访问，允许修改

my_set = {"xuanjiawei" , "zhanglu" , "zhanglu" , "sunxiuhong" , "xuanyuerong"}
my_set_empty = set()  # 定义了一个空集合
print(my_set)

# 给集合添加元素 .add()
my_set.add("python")
print(f"添加元素后 {my_set}")

# 移出元素 .remove()
my_set.remove("python")
print(f"去除元素后 {my_set}")

# 随机取出一个元素.pop（）
element = my_set.pop()
print(f"集合被取出1个元素{element}，取出后集合为{my_set}")

# 清空集合 .clear（）
my_set.clear()
print(f"集合清空后 {my_set}")

# 集合1。different（集合2） 取2个集合的差集，，取出集合1和集合2的差集（集合1 有 而 集合2 没有）
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.difference(set2)

# 消除交集

