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
#q16
#q16
q16 = pd.DataFrame(data.iloc[:,20].value_counts().sort_index())
print(q16)

#데이터 준비
labels = ['매우 만족','만족',' 보통','불만족','매우 불만족','영상 출석콘텐츠 수업 경험 없음']##라벨
frequency = [38, 126, 42, 8, 3, 3] ##빈도

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
pie = ax.pie(frequency, ## 파이차트 출력
       #labels=labels, ## 라벨 출력(표시하면 러벨 인자 생김)
       colors=cmaps_6,
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 반시계 방향으로 파이차트를 그린다.
       #autopct='%.1f%%', pctdistance=1.1
       )

 
plt.legend(pie[0], labels) ## 범례
plt.title('16. 실시간 화상강의(Zoom, Collaborate) 수업 방식에 대해 전반적으로 만족합니까?')
plt.show()