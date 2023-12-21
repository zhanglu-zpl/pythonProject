import random

# 用for循环，打印一个99乘法表
for i in range(1,10) :
    continue
    print("zhanglu")
    for j in range(1,i+1) :
        print(f"{i}*{j}={i*j} ", end="")

    print("")

# 循环中断和退出  continue= 中断本次循环
for i in range(1,10) :
    for j in range(1,i+1) :
        continue
        print("zhanglu")
        print(f"{i}*{j}={i*j} ", end="")
    print("")

# break 直接退出当前的所有循环
for i in range(1,10) :
    for j in range(1,i+1) :
        break
        print("zhanglu")
        print(f"{i}*{j}={i*j} ", end="")
    print("- -")

# 案例联系

gongzi = 10000
fafang = 0
for yuangongnum in range(1,21) :
    jixiao = random.randint(1, 10)
    if gongzi >= 1000 :
        if jixiao >= 5 :
            print(f"员工{yuangongnum}绩效为{jixiao},发工资1000")
            gongzi -= 1000
            fafang += 1
        else :
            print(f"员工{yuangongnum}绩效为{jixiao},不发工资")
            continue
    else :
        print(f"员工{yuangongnum}账户没有余额，下个月发放")
        break
print(f"本次向{fafang}员工发放工资，账户剩余{gongzi}")
