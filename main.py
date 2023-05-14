import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc


#한글 폰트 깨짐
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("블랙보드만족도조사_학생_데이터분석공모전.xlsx")
data = pd.DataFrame(data) 

#색상 선정 
cmaps_5 = ['#F66D44', '#FEAE65', '#E6F69D', '#AADEA7', '#64C2A6']
cmaps_6 = ['#F66D44', '#FEAE65', '#E6F69D', '#AADEA7', '#64C2A6', '#2D87BB']
 
#Q1
q1 = pd.DataFrame(data.iloc[:,5].value_counts().sort_index())
print(q1)

#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [4, 16, 21, 143, 36] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=cmaps_5,
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       #autopct='%.1f%%', pctdistance=1.1
       )
plt.legend(labels) ## 범례
plt.title('1. 블랙보드 시스템에 전반적으로 만족하십니까?')
plt.show()

#Q41
q41 = pd.DataFrame(data.iloc[:,45].value_counts().sort_index())
print(q41)

#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [1, 6, 23, 123, 67] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=cmaps_5,
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       )

plt.legend(labels) ## 범례
plt.title('41. 실시간 강의 도구(ZOOM, Collaborate) 기능에 만족하십니까?')
plt.show()

