from ast import Num
from itertools import count
from re import X
import string
from time import sleep
import pandas as pd
import matplotlib
import numpy as np
import os
from collections import Counter
import platform

'''
NAME : WIFI Analyze
PROJECT : Vene, Vidi, Vici
Author : ADEL

made from 2022-08-03

=====info=====

1 : 앞 문
2 : 티비 앞
3 : 창문 쪽 사물함
4 : 뒷 문

'''

#전역함수#
global channel_
channel_ = [] #모든반의 상위 채널

global wifi_
wifi_ = {} #모든 반의 상위 와이파이 이름



def Analyze(clas):
    ###########################구역 내 전역 함수 part#############################
    global dir #dir 전역 함수
    if platform.system() =='Windows': #윈도우 환경이
        dir = os.getcwd().replace("/", "\\") #dir은 절대경로 대용으로 쓰임
    else:
        pass
    # print(os.getcwd()+"\a") #디버깅
    # print(dir) #디버깅
    global dat #와이파이 데이터를 오버 라이딩 해야 해서 전역 변수로 만듬
    global wifi_k
    global channel_k
    global ANGEL #마지막마지막 그다음 값 저장
    global DEUS #마지마지막 최고 값 저장
    global LUX #마지막마지막 최고 널널 채널 저장
    wifi_k = {} #가장 빠른 와이파이들 목록 (기준 : 와이파이의 속도)
    channel_k = [] #가장 최적한 채널들 목록 (기준 : 채널에 있는 와이파이수)
    DEUS = {}
    ANGEL = {}
    LUX = []

    ############################################################

    test = {
        '1~3' : {'name' : ['wi_gen', 'adfad'], 'speed' : [14, 51]},
        '4~5' : {'name' : ['Latta'], 'speed' : [15]},
        '124' : {'adfa' : ['1']}
        } #디버그


    def read_data(clas):
        if platform.system() == 'Windows':
            final_dir = "{0}\\code\\file\\wifi_{1}.csv".format(dir, clas)
        else:
            final_dir - "{0}/code/file/wifi_{1}.csv".format(dir, clas)
        dat = pd.read_csv(final_dir, sep = ",", dtype='unicode') #전체 데이터 불러오기
        dat = dat.dropna() #공백 제거 c.f) 이놈 때문에 아래 정렬에서 애를 먹었다, 결측치(NaN)이 형식이 float이라 .join이 안되 문법 오류를 일으키는데 3일 만에 찾았다 ...
        classify(dat) #정렬 함수 요청

    def classify(data):
        global df1
        global df2
        global df3
        global df4 #데이터 담을 변수들 전역 형으로 선언
        
        df1_n = data[['channel_1', 'wifi_name_1', 'speed_1']] #앞문 데이터만 추출
        df1 = df1_n.to_dict('records') #리스트 형식으로 변환
        
        df2_n = data[['channel_2', 'wifi_name_2', 'speed_2']] #티비 앞 데이터만 추출
        df2 = df2_n.to_dict('records') #리스트 형식으로 변환

        df3_n = data[['channel_3', 'wifi_name_3', 'speed_3']] #창가 사물함 데이터만 추출
        df3 = df3_n.to_dict('records') #리스트 형식으로 변환

        df4_n = data[['channel_4', 'wifi_name_4', 'speed_4']] #뒷 문 데이터만 추출
        df4 = df4_n.to_dict('records') #리스트 형식으로 변환


        transfer(df1)
        transfer(df2)
        transfer(df3)
        transfer(df4) #자료 정리 함수 요청 >> df1,2,3,4 에는 이상적인 최종 형태의 자료가 정리 됨.
        name(df1)
        name(df2)
        name(df3)
        name(df4) #결과 정리 함수 요청
        channel(df1)
        channel(df2)
        channel(df3)
        channel(df4) #채널 정리 함수 요청

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


    def number(fir, sec): #정수 사이 간격 길이 구하는 함수
        for i in range(fir, sec):
            return i
    def Most2(mode, obj): #입력은 딕셔너리로 받음, 2번째로 큰 값 구하는 함수v
        buffer = list(obj.values()) #파라미터로 받은 딕셔너리 값 모음을 리스트로
        res = sorted(buffer, reverse=True) #리스트를 큰 순으로 정렬
        if mode == 1: #모드 1일때, 문자열로 출력
            if len(res) > 1: #최댓값을 비교할 수 있을만큼 자료가 있을때(2개 이상 존재)
                for i in range(len(res)-1):
                    if res[i+1] == res[0]:
                        pass
                    elif res[i+1] < res[0]: #맨 처음값을 지웠는데 맨 처음 값과 같은 값이 있으면 건너 뛰고 다음 값을 찾는다.(최종적으로 처음 값보다 바로 다음으로 작은 값 구함)
                        temp = [k for k, v in obj.items()  if v == res[i+1] and not max(wifi_k, key=wifi_k.get).split('(')[0] in k] #해당 값(두번째로 큰 값)을 가진 와이파이 이름을 리스트 형태로 반환. <이때 최상 값과 같으면 무시>
                        final ='' #최종값
                        for j in range(len(temp)):
                            final += 'SEC_NAME : ' + temp[j] + '    SEC_SPEED : ' + obj[temp[j]] + '\n'
                        return final
                return
            else:
                return
        else:
            if len(res) > 1: #최댓값을 비교할 수 있을만큼 자료가 있을때(2개 이상 존재)
                for i in range(len(res)-1):
                    if res[i+1] == res[0]:
                        pass
                    elif res[i+1] < res[0]: #맨 처음값을 지웠는데 맨 처음 값과 같은 값이 있으면 건너 뛰고 다음 값을 찾는다.(최종적으로 처음 값보다 바로 다음으로 작은 값 구함)
                        temp = [k for k, v in obj.items()  if v == res[i+1] and not max(wifi_k, key=wifi_k.get).split('(')[0] in k] #해당 값(두번째로 큰 값)을 가진 와이파이 이름을 리스트 형태로 반환. <이때 최상 값과 같으면 무시>
                        if len(temp) != 0: #해당값 리스트 개수가 0이 아니면
                            if temp[0].split('(')[0] in [k.split('(')[0] for k in ANGEL.keys()]: #같은 키가 존재 하면
                                if temp[0] > [k for k in ANGEL if temp[0].split('(')[0] in k][0]: #값을 비교하고 값이 클때만
                                    ANGEL[temp[0]] = obj[temp[0]] #ANGEL에 저장
                                    return temp[0]

                            else: #같은 키가 없으면
                                ANGEL[temp[0]] = obj[temp[0]] #ANGEL에 저장
                                return temp[0]
                return
            else:
                return

    def name(target): #와이파이의 최선 값 도출 함수  
        global df1_top
        global df2_top
        global df3_top
        global df4_top

        global df1_2top
        global df2_2top
        global df3_2top
        global df4_2top   

    ######가장 빠른 와이파이를 계산######

        if target == df1:
            for i in range(len(target)):
                
                king = [k for k in range(len(target[i]['speed_1'])) if max(target[i]['speed_1']) in target[i]['speed_1'][k]] #와이파이 속도 리스트 중 빠른 친구의 위치 저장
                if len(king) > 1 :
                    for g in range(len(king)) : 
                        if target[i]['wifi_name_1'][king[g]] in wifi_k.keys():
                            if wifi_k[target[i]['wifi_name_1'][king[g]]] >= max(wifi_k.values()):
                                wifi_k[target[i]['wifi_name_1'][king[g]]] = target[i]['speed_1'][king[g]]
                            else:
                                pass
                        else: wifi_k[target[i]['wifi_name_1'][king[g]]] = target[i]['speed_1'][king[g]] #속도와 구한 위치로 이름과 맵핑 시켜, ready_k에 저장

                else:
                    if target[i]['wifi_name_1'][king[0]] in wifi_k.keys():
                        if wifi_k[target[i]['wifi_name_1'][king[0]]] >= max(wifi_k.values()):
                            wifi_k[target[i]['wifi_name_1'][king[0]]] = target[i]['speed_1'][king[0]]
                        else:
                            pass
                    else:
                        wifi_k[target[i]['wifi_name_1'][king[0]]] = target[i]['speed_1'][king[0]] #  "(같은거)

            wifi_k.pop("Null") #결측치 제거
            df1_2top = Most2(0, wifi_k) #차선책 값
            df1_top = 'NAME : ' + max(wifi_k, key=wifi_k.get) + '   SPEED : ' + wifi_k[max(wifi_k, key=wifi_k.get)] #최대값
            if max(wifi_k, key=wifi_k.get).split('(')[0] in [k.split('(')[0] for k in DEUS.keys()]: #DEUS에 같은 값이 존재하면
                if max(wifi_k, key=wifi_k.get).split('(')[0] > [k for k in DEUS if max(wifi_k, key=wifi_k.get).split('(')[0] in k][0]: #값을 비교하고 값이 클때만
                    DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]
            else:
                DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]
            

        if target == df2:
            for i in range(len(target)):
                king = [k for k in range(len(target[i]['speed_2'])) if max(target[i]['speed_2']) in target[i]['speed_2'][k]] #와이파이 속도 리스트 중 빠른 친구의 위치 저장
                
                if len(king) > 1 :
                    for g in range(len(king)) : 
                        if target[i]['wifi_name_2'][king[g]] in wifi_k.keys():
                            if wifi_k[target[i]['wifi_name_2'][king[g]]] >= max(wifi_k.values()):
                                wifi_k[target[i]['wifi_name_2'][king[g]]] = target[i]['speed_2'][king[g]]
                            else:
                                pass
                        else: wifi_k[target[i]['wifi_name_2'][king[g]]] = target[i]['speed_2'][king[g]] #속도와 구한 위치로 이름과 맵핑 시켜, ready_k에 저장

                else:
                    # print(king[0])
                    # print(target[i])
                    if target[i]['wifi_name_2'][king[0]] in wifi_k.keys():
                        
                        if wifi_k[target[i]['wifi_name_2'][king[0]]] >= max(wifi_k.values()):
                            wifi_k[target[i]['wifi_name_2'][king[0]]] = target[i]['speed_2'][king[0]]
                        else:
                            pass
                    else:
                        wifi_k[target[i]['wifi_name_2'][king[0]]] = target[i]['speed_2'][king[0]] #  "(같은거)
        
            wifi_k.pop("Null") #결측치 제거
            df2_2top = Most2(0, wifi_k) #차선책 값
            df2_top = 'NAME : ' + max(wifi_k, key=wifi_k.get) + '   SPEED : ' + wifi_k[max(wifi_k, key=wifi_k.get)]
            if max(wifi_k, key=wifi_k.get).split('(')[0] in [k.split('(')[0] for k in DEUS.keys()]: #DEUS에 같은 값이 존재하면
                if max(wifi_k, key=wifi_k.get).split('(')[0] > [k for k in DEUS if max(wifi_k, key=wifi_k.get).split('(')[0] in k][0]: #값을 비교하고 값이 클때만
                    DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]
            else:
                DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]

        if target == df3:
            for i in range(len(target)):
                king = [k for k in range(len(target[i]['speed_3'])) if max(target[i]['speed_3']) in target[i]['speed_3'][k]] #와이파이 속도 리스트 중 빠른 친구의 위치 저장
                if len(king) > 1 :
                    for g in range(len(king)) : 
                        if target[i]['wifi_name_3'][king[g]] in wifi_k.keys():
                            if wifi_k[target[i]['wifi_name_3'][king[g]]] >= max(wifi_k.values()):
                                wifi_k[target[i]['wifi_name_3'][king[g]]] = target[i]['speed_3'][king[g]]
                            else:
                                pass
                        else: wifi_k[target[i]['wifi_name_3'][king[g]]] = target[i]['speed_3'][king[g]] #속도와 구한 위치로 이름과 맵핑 시켜, ready_k에 저장

                else:
                    if target[i]['wifi_name_3'][king[0]] in wifi_k.keys():
                        if wifi_k[target[i]['wifi_name_3'][king[0]]] >= max(wifi_k.values()):
                            wifi_k[target[i]['wifi_name_3'][king[0]]] = target[i]['speed_3'][king[0]]
                        else:
                            pass
                    else:
                        wifi_k[target[i]['wifi_name_3'][king[0]]] = target[i]['speed_3'][king[0]] #  "(같은거)
        
            wifi_k.pop("Null") #결측치 제거
            df3_2top = Most2(0, wifi_k) #차선책 값
            df3_top = 'NAME : ' + max(wifi_k, key=wifi_k.get) + ' SPEED : ' + wifi_k[max(wifi_k, key=wifi_k.get)]

            if max(wifi_k, key=wifi_k.get).split('(')[0] in [k.split('(')[0] for k in DEUS.keys()]: #DEUS에 같은 값이 존재하면
                if max(wifi_k, key=wifi_k.get).split('(')[0] > [k for k in DEUS if max(wifi_k, key=wifi_k.get).split('(')[0] in k][0]: #값을 비교하고 값이 클때만
                    DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]
            else:
                DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]

        if target == df4:
            for i in range(len(target)):
                king = [k for k in range(len(target[i]['speed_4'])) if max(target[i]['speed_4']) in target[i]['speed_4'][k]] #와이파이 속도 리스트 중 빠른 친구의 위치 저장
                if len(king) > 1 :
                    for g in range(len(king)) : 
                        if target[i]['wifi_name_4'][king[g]] in wifi_k.keys():
                            if wifi_k[target[i]['wifi_name_4'][king[g]]] >= max(wifi_k.values()):
                                wifi_k[target[i]['wifi_name_4'][king[g]]] = target[i]['speed_4'][king[g]]
                            else:
                                pass
                        else: wifi_k[target[i]['wifi_name_4'][king[g]]] = target[i]['speed_4'][king[g]] #속도와 구한 위치로 이름과 맵핑 시켜, ready_k에 저장

                else:
                    if target[i]['wifi_name_4'][king[0]] in wifi_k.keys():
                        if wifi_k[target[i]['wifi_name_4'][king[0]]] >= max(wifi_k.values()):
                            wifi_k[target[i]['wifi_name_4'][king[0]]] = target[i]['speed_4'][king[0]]
                        else:
                            pass
                    else:
                        wifi_k[target[i]['wifi_name_4'][king[0]]] = target[i]['speed_4'][king[0]] #  "(같은거)
        
            wifi_k.pop("Null") #결측치 제거
            df4_2top = Most2(0, wifi_k) #차선책 값
            df4_top = 'NAME : ' + max(wifi_k, key=wifi_k.get) + '   SPEED : ' + wifi_k[max(wifi_k, key=wifi_k.get)]

            if max(wifi_k, key=wifi_k.get).split('(')[0] in [k.split('(')[0] for k in DEUS.keys()]: #DEUS에 같은 값이 존재하면
                if max(wifi_k, key=wifi_k.get).split('(')[0] > [k for k in DEUS if max(wifi_k, key=wifi_k.get).split('(')[0] in k][0]: #값을 비교하고 값이 클때만
                    DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]
            else:
                DEUS[max(wifi_k, key=wifi_k.get)] = wifi_k[max(wifi_k, key=wifi_k.get)]

    def channel(target): 
        
        #최적한 채널 도출 함수
        ######가장 최적한 채널을 계산########
        # print(target)

        if target == df1:
            for i in range(len(target)):
                if target[i]['wifi_name_1'] == ['Null']:
                    channel_k.append(target[i]['channel_1'][0])
        if target == df2:

            for i in range(len(target)):
                if target[i]['wifi_name_2'] == ['Null']:
                    channel_k.append(target[i]['channel_2'][0])
        if target == df3:

            for i in range(len(target)):
                if target[i]['wifi_name_3'] == ['Null']:
                    channel_k.append(target[i]['channel_3'][0])
        if target == df4:

            for i in range(len(target)):
                if target[i]['wifi_name_4'] == ['Null']:
                    channel_k.append(target[i]['channel_4'][0])

        for i in channel_k:
            if len(LUX) != 0: #LUX개수 0개가 아니면
                if len(channel_) != 0: #channel 개수 0개가 아니면
                    if number(int(i.split('~')[0]), int(i.split('~')[1])) > number(int(LUX[0].split('~')[0]), int(LUX[0].split('~')[1])): #LUX중 가장 크면
                        for k in channel_: 
                            if set(range(int(i.split('~')[0]), int(i.split('~')[1]))) & set(k) == {}:
                                LUX[0] = i #전체 반에서 중복되지 않는 채널 선ㄴ택
                                channel_.append(range(int(i.split('~')[0]), int(i.split('~')[1])))
                else:
                    channel_.append(range(int(i.split('~')[0]), int(i.split('~')[1])))
                    LUX[0] = i
            else:
                LUX.append(i)

    #메뉴 등 실행 코드

    read_data(clas)
    print("""
    ======{clas}반의 결과======
    앞문 > 최고 - {df1}
        > 차선책 - {df1_2}
    티비 앞 > 최고 - {df2}
            > 차선책 - {df2_2}
    사물함 앞 > 최고 - {df3}
            > 차선책 - {df3_2}
    뒷문 > 최고 - {df4}
        > 차선책 - {df4_2}
    ===========================
    """.format(clas = clas, df1 = df1_top, df1_2 = df1_2top, df2 = df2_top, df2_2 = df2_2top, df3 = df3_top, df3_2 = df3_2top, df4 = df4_top, df4_2 = df4_2top)) #결과 출력

    temp = [k for k, v in DEUS.items() if v == max(DEUS.values())]
    if len(wifi_) != 0:
        if temp[0].split('(')[0] in [j.split('(')[0] for j in wifi_]:
            if DEUS[temp[0]] > [v for k, v in wifi_.items()   if temp[0].split('(')[0] in k][0]:
                wifi_[temp[0]] = DEUS[temp[0]]
                return clas, '반 : ', temp[0], '를', LUX[0], '로'
            elif DEUS[temp[0]] == [v for k, v in wifi_.items()   if temp[0].split('(')[0] in k][0]:
                ko = [k for k, v in ANGEL.items()  if v == max(ANGEL.values())]
                # print(ko)
                wifi_[ko[0]] = ANGEL[ko[0]]
                return clas, '반 : ', temp[0], '를', LUX[0], '로'
        else:
            wifi_[temp[0]] = DEUS[temp[0]]
        # print(temp)
        return clas, '반 : ', temp[0], '를', LUX[0], '로'
    else:
        wifi_[temp[0]] = DEUS[temp[0]]
        return clas, '반 : ', temp[0], '를', LUX[0], '로'


    # if len(wifi_) != 0:
    #     for k in DEUS.keys():
    #         if not k.split('(')[0] in [j.split('(')[0] for j in wifi_.keys()] and not ANGEL[0].split('(')[0] in [j.split('(')[0] for j in wifi_.keys()]:
    #             res_wifi = [x for x, v in DEUS.items() if v == max(DEUS.values())][0]
    #             wifi_[res_wifi] = DEUS[res_wifi]
    #             return res_wifi, '를 ', LUX[0] + '로'
    #         elif not k.split('(')[0] in [j.split('(')[0] for j in wifi_.keys()] and ANGEL[0].split('(')[0] in [j.split('(')[0] for j in wifi_.keys()]:
    #             res_wifi = [x for x, v in DEUS.items() if v == max(DEUS.values())][0]
    #             wifi_[res_wifi] = DEUS[res_wifi]
    #             return res_wifi, '를 ', LUX[0] + '로'

    #         elif k.split('(')[0] in [j.split('(')[0] for j in wifi_.keys()] and not ANGEL[0].split('(')[0] in [j.split('(')[0] for j in wifi_.keys()]:
    #             res_wifi = ANGEL[0]
    #             wifi_[res_wifi] = ANGEL[0]
    #             return res_wifi, '를 ', LUX[0] + '로'
    #         else:
    #             res_wifi = [x for x, v in DEUS.items() if v == max(DEUS.values())][0]
    #             wifi_[res_wifi] = DEUS[res_wifi]
    #             return res_wifi, '를 ', LUX[0] + '로'
    # else:
    #     res_wifi = [x for x, v in DEUS.items() if v == max(DEUS.values())][0]
    #     wifi_[res_wifi] = DEUS[res_wifi]
    #     return res_wifi, '를 ', LUX[0] + '로'




print(Analyze(1))
print(Analyze(2))
print(Analyze(3))
print(Analyze(4))
print(Analyze(5))
print(Analyze(6))
print(Analyze(7))
print(Analyze(8))


