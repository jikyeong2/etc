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

#Q22
q22 = pd.DataFrame(data.iloc[:,26].value_counts().sort_index())
print(q22)
#데이터 준비
labels = np.char.array(['1','2','3','4','5'])##라벨
frequency = np.array([5, 18, 50, 114, 33]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(12,12))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_5, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('22. 블랙보드 홈페이지는 LMS를 사용하는데 필요한 정보를 손쉽게 찾고 관련 안내를 신속하게 전달할 수 있도록 구성되었습니다. 이 구성에 만족하십니까? ')
plt.show()

#Q46
q50 = pd.DataFrame(data.iloc[:,50].value_counts().sort_index())
print(q50)
#데이터 준비
labels = np.char.array(['상관없음','차세대 LMS 도입 희망','현재 LMS 유지'])##라벨
frequency = np.array([62, 59, 99]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(12,12))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
patches, texts = plt.pie(frequency, colors=['#F66D44', '#FEAE65', '#E6F69D'], startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('46. 차세대 학습관리시스템(LMS)를 도입하는 것에 대해 어떻게 생각하십니까?')
plt.show()

##q37
q37 = pd.DataFrame(data.iloc[:,41].value_counts().sort_index())
print(q37)

#데이터 준비
labels = np.char.array(['1','2','3','4','5'])##라벨
frequency = np.array([5, 18, 50, 114, 33]) ##빈도
percent = 100.*frequency/frequency.sum()

#데이터 준비
labels = np.char.array(['1','2','3','4','5'])##라벨
frequency = np.array([10, 6, 45, 95, 64]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_5, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)

plt.title('37.  영상 출결 콘텐츠  출석 현황 기능에 만족하십니까?')
plt.show()

#Q14
q14 = pd.DataFrame(data.iloc[:,18].value_counts().sort_index())
print(q14)
#데이터 준비
labels = np.char.array(['매우 만족','만족','보통','불만족','매우 불만족','영상 출석콘텐츠 수업 경험 없음'])##라벨
frequency = np.array([37, 102, 44, 12, 10, 15]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_6, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('14. 블랙보드 영상 출석콘텐츠 수업 방식에 대해 전반적으로 만족합니까?')
plt.show()

#q16
q16 = pd.DataFrame(data.iloc[:,20].value_counts().sort_index())
print(q16)

#데이터 준비
labels = np.char.array(['매우 만족','만족',' 보통','불만족','매우 불만족','영상 출석콘텐츠 수업 경험 없음'])##라벨
frequency = np.array([38, 126, 42, 8, 3, 3]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_6, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('16. 실시간 화상강의(Zoom, Collaborate) 수업 방식에 대해 전반적으로 만족합니까?')
plt.show()

#Q35

q35 = pd.DataFrame(data.iloc[:,39].value_counts().sort_index())
print(q35)
#데이터 준비
labels = np.char.array(['1','2','3','4','5'])##라벨
frequency = np.array([12, 18, 69, 90, 31]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_5, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('35. 그룹활동(토론, 블로그, 저널) 기능에 만족하십니까?')
plt.show()

#Q33
q33 = pd.DataFrame(data.iloc[:,37].value_counts().sort_index())
print(q33)
#데이터 준비
labels = np.char.array(['1','2','3','4','5'])##라벨
frequency = np.array([2, 7, 37, 115, 59]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_5, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('33. 과제 제출 및 피드백 기능(턴잇인, SafeAssign)에 얼마나 만족하십니까?')
plt.show()

##q39
q39 = pd.DataFrame(data.iloc[:,43].value_counts().sort_index())
print(q39)
#데이터 준비
labels = np.char.array(['1','2','3','4','5'])##라벨
frequency = np.array([6, 9, 59, 99, 47]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_5, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('39. 시험/락다운브라우저 기능에 만족하십니까?')
plt.show()

##q43
q43 = pd.DataFrame(data.iloc[:,47].value_counts().sort_index())
print(q43)
#데이터 준비
labels = np.char.array(['1','2','3','4','5'])##라벨
frequency = np.array([3, 9, 32, 106, 70]) ##빈도
percent = 100.*frequency/frequency.sum()

fig = plt.figure(figsize=(8,8))#캔버스 생성
fig.set_facecolor('white') ##캔버스 배경색을 하얀색으로 설정 
ax = fig.add_subplot()#프레임 생성

#파이 차트 출력
patches, texts = plt.pie(frequency, colors=cmaps_5, startangle=90, radius=1.2)
labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]

plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
plt.title('43. 성적 기능에 얼마나 만족하십니까?')
plt.show()
