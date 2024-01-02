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

# 
