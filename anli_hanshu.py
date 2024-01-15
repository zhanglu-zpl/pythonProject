# ========================================================================
# 案例： 用于记录银行卡余额

# 要求输入客户姓名
uid = input("请输入您的姓名:")
money = 5000000

# 定义一个查询余额的函数
def check_balance():
    return print(f"{uid}您当前卡内余额为{money}")


# 定义一个存款函数
def deposit():
    d = int(input("请输入您要存入的金额"))
    global money
    money += d
    print("--------存款--------")
    print(f"您存款{d}元，成功")

# 定义一个取款函数
def take_out():
    t = int(input("请输入您要取出的金额"))
    global money
    money -= t
    print("--------取款--------")
    print(f"您取款{t}元，成功")

# 用户下一步行为动作
def main() :
    print("------当前在主菜单-----")
    operate = int(input("请选择您需要的操作：1.查询余额；2.存款 3.取款 4.退出 "))
    return operate

while True:
    keyboard = main()
    if keyboard == 1:
        check_balance()
        continue # 通过 continue继续下一次循环
    elif keyboard == 2:
        deposit()
        continue
    elif keyboard == 3:
        take_out()
        continue
    else:
        print("程序退出了")
        break












