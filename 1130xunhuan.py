# 循环语句
# i = 0
# while i < 10 :
#     print('王嘉尔！你好帅!')
#     i += 1

# 求1-100的和
# i = 1
# sum = 0
# while i <= 100 :
#     sum = i + sum
#     i += 1
# print(sum)

# 循环案例 猜数字
# 定义一个1-100的随机数字
# import random
# num = random.randint(1,100)
# 定义一个变量接收猜测次数
# count = 0
# 定义进入循环的条件
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜测的数字:"))
#     count += 1
#     if guess_num == num :
#         print("猜对了")
#         flag = False
#     else:
#         if guess_num > num :
#             print("大了")
#         else:
#             print("小了")
#
# print(f"你总共猜了{count}次")

# 表白100天 每天送饺子
# i = 1
# while i <= 100 :
#     print(f"今天是第{i}天")
#     j = 1
#     while j <= 10 :
#         print(f"这是送你的第{j}盘饺子")
#         j += 1
#     print('岳云鹏，我喜欢听你说相声！')
#     i += 1
# print(f"坚持了{i-1}天，追星成功！")


# 打印99乘法表
i = 1
while i <= 9 :
    j = 1
    while j <= i  :
        print(f'{j}*{i}={j * i}\t', end='')
        j += 1
    i += 1
    print()

