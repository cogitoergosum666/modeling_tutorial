import csv
import numpy as np

def Str1(waiting):#第一个决策函数
    '''
    你需要填写你的决策函数
    '''
    choice = np.argmin(waiting)
    return choice 

def q1(data1):
    waiting_data = np.array(data1[1:])#去除表头
    waiting_data = np.delete(waiting_data,np.array([0,4,5,6]),axis = 1)#去除除三部电梯排队人数外的数据
    #print(waiting_data)
    answer = []
    for i in range(len(waiting_data)):
        answer.append(Str1(waiting_data[i]))
    return answer
def check_q1(uranswer):   
    with open('data1.csv',newline='') as data1:
        reader = csv.reader(data1)
        answer = np.array(q1(list(reader)))
        if np.array_equal(answer,uranswer):
            print("答案正确！")
        else:
            print("答案错误！")

def Str2(data):
    def function(input):#
        '''
        该函数应该计算出综合了当前排队人数与电梯当前楼层后的预期时间
        input应该是一个元组，描述该电梯的当前等待人数与当前楼层
        '''

        stopped_floor = 8 #上行过程中停靠的楼层数
        expect_time_cost = (int(input[0])//10) * stopped_floor * 2 + int(input[1]) * 3
        return expect_time_cost
    answer_time = []
    input_tuple = []
    for i in range(len(data)):
        
        input_tuple.append([(data[i][1],data[i][4]),
                            (data[i][2],data[i][5]),
                            (data[i][3],data[i][6])])

        #print(input_tuple)
        answer_time.append((function(input_tuple[i][0]),function(input_tuple[i][1]),function(input_tuple[i][2])))
        #print(answer_time)
    #print(answer_time)
    answer_lift = np.array(np.argmin(answer_time,axis=1))
    return answer_lift


def q2(data1):
    data  = np.array(data1[1:])#去除表头
    return Str2(data)

def check_q2(uranswer):
    with open('data1.csv',newline='') as data1:
        reader = csv.reader(data1)

        answer = q2(list(reader))

        if np.array_equal(answer,uranswer):
            print("答案正确！")
        else:
            print("答案错误！")