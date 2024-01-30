# 将容器中的元素依次取出进行处理，称之为遍历

def list_while_func():
    '''
    使用while循环遍历喊出
    :return: none
    '''
    my_list = ["wo","shi","zhang","piao","liang"]
    # 循环控制变量通过下标索引来控制，默认为0  ； 每一次循环将下标索引变量+1  ；
    # 循环条件： 下标索引变量<列表元素数量

    # 定义一个变量用来标记列表的下标
    index = 0
    while index < len(my_list) :
        element = my_list[index]
        print(f"列表元素{element}")
        index += 1




def list_for_func():
    """
    使用for循环遍历列表 演示
    :return: none
    """
    my_list2 = [1,2,3,4,5,6,77,8,9]
    for elem in my_list2:
        print(f'列表元素有{elem}')



list_while_func()

list_for_func()

# 练习案例 取出列表中的偶数

def for_fun():
    '''
    使用for进行遍历列表
    :return:
    '''
    list1 = [1,2,3,4,5,6,7,8,9,10]
    new_list = []
    for oushu in list1:
        if oushu %2 == 0:
            new_list.append(oushu)
        print(f'当前新列表为{new_list}')

for_fun()