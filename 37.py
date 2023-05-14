import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rc

#한글 폰트 깨짐
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("블랙보드만족도조사_학생_데이터분석공모전.xlsx")
data = pd.DataFrame(data)

#Q37
##q37
q37 = pd.DataFrame(data.iloc[:,41].value_counts().sort_index())
print(q37)

#데이터 준비
labels = ['1','2','3','4','5']##라벨
frequency = [10, 6, 45, 95, 64] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=['skyblue', 'pink', 'grey', 'lightgreen', 'yellow','green'],
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       #autopct='%.1f%%', pctdistance=1.1
       )

plt.legend(pie[0],labels) ## 범례
plt.title('37.  영상 출결 콘텐츠  출석 현황 기능에 만족하십니까?')
plt.show()