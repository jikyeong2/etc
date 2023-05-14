import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc 

#색상 선정 
cmaps_5 = ['#F66D44', '#FEAE65', '#E6F69D', '#AADEA7', '#64C2A6']
cmaps_6 = ['#F66D44', '#FEAE65', '#E6F69D', '#AADEA7', '#64C2A6', '#2D87BB']

#한글 폰트 깨짐
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("블랙보드만족도조사_학생_데이터분석공모전.xlsx")
data = pd.DataFrame(data)


#Q33,Q39,Q43
##q33
q33 = pd.DataFrame(data.iloc[:,37].value_counts().sort_index())
print(q33)
#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [2, 7, 37, 115, 59] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors= cmaps_5,
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.2,
       wedgeprops = {'linewidth': 3.0, 'edgecolor': 'white'},
       )

plt.legend(pie[0],labels) ## 범례
plt.title('33. 과제 제출 및 피드백 기능(턴잇인, SafeAssign)에 얼마나 만족하십니까?')
plt.show()

##q39
q39 = pd.DataFrame(data.iloc[:,43].value_counts().sort_index())
print(q39)
#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [6, 9, 59, 99, 47] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=cmaps_5,
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )

plt.legend(pie[0],labels) ## 범례
plt.title('39. 시험/락다운브라우저 기능에 만족하십니까?')
plt.show()

##q43
q43 = pd.DataFrame(data.iloc[:,47].value_counts().sort_index())
print(q43)
#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [3, 9, 32, 106, 70] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=cmaps_5,
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       autopct='%.1f%%', pctdistance=1.1
       )

plt.legend(pie[0],labels) ## 범례
plt.title('43. 성적 기능에 얼마나 만족하십니까?')
plt.show()