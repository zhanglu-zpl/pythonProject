# age = int(input("请问你的年龄是多大？"))
# if age >= 18 :
#     print("您已成年，需要补票10元")
# else:
#     print("您未成年，可以免费游玩")
# print("祝您游玩愉快")

# height = int(input("请输入您的身高(cm)："))
# if height >= 120 :
#     print("您的身高超出120cm，游玩需要补票10元")
# else:
#     print("您的身高不足120cm，可以免费游玩")
# print("祝您游玩愉快")


# if elif else  判断
# print("欢迎来到动物园")
# height = int(input("请输入您的身高："))
# vip_level = int(input("请输入您的会员等级（1-5）："))
# if  height < 120 :
#     print("您可以免费游玩")
# elif vip_level > 3 :
#     print("您也可以免费游玩")
# elif int(input("今天是几号？")) == 1 :
#     print("您可以免费游玩")
# else :
#     print("您需要补票")


# 猜数字游戏
# heart_num = 7
# if int(input("请输入第一次猜想的数字：")) == heart_num :
#     print('yes,you win')
# elif int(input("不对，再猜一次：")) == heart_num:
#     print('yes,you win')
# elif int(input("不对，再猜最后一次：")) == heart_num:
#     print('yes,you win')
# else :
#     print(f'sorry 全猜错了，我心里想的是：{heart_num}')


# 判断语句的嵌套
import random
num = random.randint(1,10)
guess_num = int(input("请输入你要猜测的数字："))
if guess_num == num :
    print('yes，你竟然猜对了')
else:
    if guess_num > num:
        print('你猜的数字大了')
    else:
        print("你猜的数字小了")
    guess_num = int(input("请再次输入你要猜测的数字："))
    if guess_num == num :
        print('yes，第二次你猜中了')
    else:
        if guess_num > num:
            print('你猜的数字大了')
        else:
            print("你猜的数字小了")

        guess_num = int(input("请输入你最后要猜测的数字："))
        if guess_num == num :
            print('yes，第三次你猜中了')
        else:
            print(f'机会用完了，你没猜对！结果是{num}')