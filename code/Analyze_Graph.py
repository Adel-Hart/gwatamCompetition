from re import X
import Analyze
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import platform
from sklearn.linear_model import LinearRegression #선형 회귀 살장

###########################구역 내 전역 함수 part#############################
global dir #dir 전역 함수
if platform.system() =='Windows': #윈도우 환경이
    dir = os.getcwd().replace("/", "\\") #dir은 절대경로 대용으로 쓰임
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='Malgun Gothic')
    pass

plt.rcParams['axes.unicode_minus'] = False

global wifi_
wifi_ = []
leaner = LinearRegression()


def read_data(clas):
    if platform.system() == 'Windows':
        final_dir = "{0}\\code\\file\\wifi_{1}.csv".format(dir, clas)
    else:
        final_dir - "{0}/code/file/wifi_{1}.csv".format(dir, clas)
    dat = pd.read_csv(final_dir, sep = ",", dtype='unicode') #전체 데이터 불러오기
    dat = dat.dropna() #공백 제거 c.f) 이놈 때문에 아래 정렬에서 애를 먹었다, 결측치(NaN)이 형식이 float이라 .join이 안되 문법 오류를 일으키는데 3일 만에 찾았다 ...

    a = dat['wifi_name_1']
    print(a)

    global df1
    global df2
    global df3
    global df4 #데이터 담을 변수들 전역 형으로 선언
    
    df1_n = dat[['channel_1', 'wifi_name_1', 'speed_1']] #앞문 데이터만 추출
    df1 = df1_n.to_dict('records') #리스트 형식으로 변환
    
    df2_n = dat[['channel_2', 'wifi_name_2', 'speed_2']] #티비 앞 데이터만 추출
    df2 = df2_n.to_dict('records') #리스트 형식으로 변환

    df3_n = dat[['channel_3', 'wifi_name_3', 'speed_3']] #창가 사물함 데이터만 추출
    df3 = df3_n.to_dict('records') #리스트 형식으로 변환

    df4_n = dat[['channel_4', 'wifi_name_4', 'speed_4']] #뒷 문 데이터만 추출
    df4 = df4_n.to_dict('records') #리스트 형식으로 변환

    transfer(df1)
    transfer(df2)
    transfer(df3)
    transfer(df4) #자료 정리 함수 요청 >> df1,2,3,4 에는 이상적인 최종 형태의 자료가 정리 됨.

    gather()


def transfer(tango):#자료 정리 함수 target 은 자료값 (df1, 2 ,3 ,4)
        for i in range(len(tango)): 
            if tango == df1:
            
                temp1 = tango[i]['wifi_name_1'] #swap 을 위한 임시 값
                temp1 = str(temp1) #temp 분리를 위한 문자열 화
                tango[i]['wifi_name_1'] = temp1.split() #, 를 기준으로 분리하여 리스트로 바꾸기
                
                    #메모리 BOF 방지

                temp2 = tango[i]['channel_1']
                temp2 = str(temp2)
                tango[i]['channel_1'] = temp2.split()

                

                temp3 = tango[i]['speed_1']
                temp3 = str(temp3)
                tango[i]['speed_1'] = temp3.split()

                

                #c.f) 여기서 6시간 걸림 많은 오류와 많은 이상한 것으로 고생함
            elif tango == df2:

                temp1 = tango[i]['wifi_name_2']
                str(temp1)
                tango[i]['wifi_name_2'] = temp1.split()

                

                temp2 = tango[i]['channel_2']
                str(temp2)
                tango[i]['channel_2'] = temp2.split()

                

                temp3 = tango[i]['speed_2']
                str(temp3)  
                tango[i]['speed_2'] = temp3.split()

                

            elif tango == df3:

                temp1 = tango[i]['wifi_name_3']
                str(temp1)
                tango[i]['wifi_name_3'] = temp1.split()

                

                temp2 = tango[i]['channel_3']
                str(temp2)
                tango[i]['channel_3'] = temp2.split()

                

                temp3 = tango[i]['speed_3']
                str(temp3)
                tango[i]['speed_3'] = temp3.split()

                

            elif tango == df4:

                temp1 = tango[i]['wifi_name_4']
                str(temp1)
                tango[i]['wifi_name_4'] = temp1.split()

                

                temp2 = tango[i]['channel_4']
                str(temp2)
                tango[i]['channel_4'] = temp2.split()

                

                temp3 = tango[i]['speed_4']
                str(temp3)
                tango[i]['speed_4'] = temp3.split()


def gather():
    for i in df1:
        if i['wifi_name_1'][0] != 'Null': #와이파이 리스트내용이 비지않을때만
            if len(i['wifi_name_1']) > 1: #와이파이 리스트가 두개 이상 일때
                for k in range(len(i['wifi_name_1'])):
                    temp = i['wifi_name_1'][k].split('(~')[1].replace('m)', '')
                    wifi_.append({temp : i['speed_1'][k]})
            else: #와이파이 리스트 내용이 하나일때
                temp = i['wifi_name_1'][0].split('(~')[1].replace('m)', '')
                wifi_.append({temp : i['speed_1'][0]})

    for i in df2:
        if i['wifi_name_2'][0] != 'Null': #와이파이 리스트내용이 비지않을때만
            if len(i['wifi_name_2']) > 1: #와이파이 리스트가 두개 이상 일때
                for k in range(len(i['wifi_name_2'])):
                    temp = i['wifi_name_2'][k].split('(~')[1].replace('m)', '')
                    wifi_.append({temp : i['speed_2'][k]})
            else: #와이파이 리스트 내용이 하나일때
                temp = i['wifi_name_2'][0].split('(~')[1].replace('m)', '')
                wifi_.append({temp : i['speed_2'][0]})

    for i in df3:
        if i['wifi_name_3'][0] != 'Null': #와이파이 리스트내용이 비지않을때만
            if len(i['wifi_name_3']) > 1: #와이파이 리스트가 두개 이상 일때
                for k in range(len(i['wifi_name_3'])):
                    temp = i['wifi_name_3'][k].split('(~')[1].replace('m)', '')
                    wifi_.append({temp : i['speed_3'][k]})
            else: #와이파이 리스트 내용이 하나일때
                temp = i['wifi_name_3'][0].split('(~')[1].replace('m)', '')
                wifi_.append({temp : i['speed_3'][0]})

    for i in df4:
        if i['wifi_name_4'][0] != 'Null': #와이파이 리스트내용이 비지않을때만
            if len(i['wifi_name_4']) > 1: #와이파이 리스트가 두개 이상 일때
                for k in range(len(i['wifi_name_4'])):
                    temp = i['wifi_name_4'][k].split('(~')[1].replace('m)', '')
                    wifi_.append({temp : i['speed_4'][k]})
            else: #와이파이 리스트 내용이 하나일때
                temp = i['wifi_name_4'][0].split('(~')[1].replace('m)', '')
                wifi_.append({temp : i['speed_4'][0]})



def Graph():
    x = []
    y = []
    for i in wifi_:
        x.append(int(list(i.keys())[0]))
        y.append(int(list(i.values())[0]))

    x += np.array(x)
    y += np.array(y)
    print(x)
    print(y)

    leaner.fit(x.reshape(-1, 1), y)

    
    plt.plot(x, y, 'o')
    plt.plot(x, leaner.predict(x.reshape(-1, 1)), label = '선형 계수 그래프 (거리가 작을 수록 속도가 올라가는 기울기를 나타냄)')
    plt.xlabel('와이파이의 거리', loc='right')
    plt.ylabel('와이파이와의 속도', loc='top')
    plt.legend()
    plt.savefig('test.png')




read_data(1)
read_data(2)
read_data(3)
read_data(4)
read_data(5)
read_data(6)
read_data(7)
read_data(8)

Graph()
