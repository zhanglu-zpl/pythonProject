# 字符串的分割   字符串.split
my_str = "hello python zhanglu"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行分割，得到{my_str_list},类型是{type(my_str_list)}")

# 字符串的规整操作 （去前后空格）  字符串.strip（）
my_str = " qianhou kongge qudiao  "
my_str_1 = my_str.strip()
print(f"将字符串{my_str}前后所有空格去掉，得到{my_str_1}")

# 字符串.strip（“qi”） 去除字符串中的某个字符，
my_str_2 = my_str.strip('qi')
print(f"将字符串{my_str}去掉字符q和i，得到{my_str_2}")

# 统计字符串某字符出现的次数 字符串.conut
my_str_3 = my_str.count("q")
print(f"字符串中q出现的次数为{my_str_3}")

# 统计字符串的长度 len（字符串）
print(f"字符串{my_str}的长度是{len(my_str)}")

# 作业，用while 和 for 循环 遍历字符串



print(' qi i iq'.strip('qi'))