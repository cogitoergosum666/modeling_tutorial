import random
import csv
#定义一个列表，用于储存数据条数
id = []
#定义三个列表，用于储存1,2,3号电梯排队人数
waiting_1 = []
waiting_2 = []
waiting_3 = []
#定义三个列表，用于储存1,2,3号电梯当前楼层
floor_1 = []
floor_2 = []
floor_3 = []



def gen1():
    id_number = 100001
    for i in range(100):
        id.append(id_number)
        id_number += 1

        waiting_random = [random.randrange(15) for k in range(3)]
        waiting_1.append(waiting_random[0])
        waiting_2.append(waiting_random[1])
        waiting_3.append(waiting_random[2])


        floor_random = [random.randrange(17) for k in range(3)]
        floor_1.append(floor_random[0])
        floor_2.append(floor_random[1])
        floor_3.append(floor_random[2])
    data = (id,waiting_1,waiting_2,waiting_3,floor_1,floor_2,floor_3)
    return data

def main():
    data1 = gen1()
    print(data1)
    with open(r'data1.csv','w+',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Waiting_1', 'Waiting_2', 'Waiting_3', 'Floor_1', 'Floor_2', 'Floor_3'])
        writer.writerows(zip(*data1))


if __name__ == '__main__':
    main()