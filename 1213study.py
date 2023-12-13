# for in 语句 本质是遍历：序列类型
name = "zhangluxuanjiawei"
count = 0
for x in name :
    if x == "a" :
        count += 1
print(count)

# range 语句 数字序列
# range（num）   获取一个从0开始到num的序列，不含num
# range（num1，num2）   获取一个从num1-num2的序列，不含num2
# range（num1，num2,step）  获取一个从num1-num2，间隔为step的序列，不含num2

for p in range(1,20,3) :
    print(p)

# 计算1-100范围内有多少个偶数
num = 0
for y in range(1,100) :
    if y%2 == 0 :
        num +=1
print(num)




# 用for循环，