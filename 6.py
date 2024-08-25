import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 사용할 데이터의 헤더를 정의합니다. (Time, Sensor1, Sensor6 제외)
header = ['Temperature', 'Humidity', 'RPM', 'Vibrations', 'Pressure', 'Sensor2', 'Sensor3', 'Sensor4', 'Sensor5', 'Status']

# 엑셀 파일에서 데이터를 불러옵니다.
data = pd.read_excel('./data/2.elevator_failure_prediction.xlsx', names = header)

# 피어슨 상관계수를 사용하여 상관관계 행렬을 계산합니다.
corr = data.corr(method='pearson')

# Figure와 Subplot을 생성합니다.
fig, ax = plt.subplots(figsize=(10, 8))

# 상관관계 행렬을 colormap을 사용하여 시각화합니다.
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)

# Figure에 color bar를 추가합니다.
fig.colorbar(cax)

# 축에 tick과 label을 설정합니다.
ticks = np.arange(len(header))
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(header, rotation=90)  # x축 레이블을 세로로 회전하여 가독성을 높입니다.
ax.set_yticklabels(header)

# X축 레이블을 하단으로 이동시킵니다.
ax.xaxis.set_ticks_position('bottom')
ax.xaxis.set_label_position('bottom')

# 상단에 'Correlation' 제목을 진한 글씨체로 추가합니다.
ax.set_title('Correlation', pad=20, fontweight='bold')

# 플롯을 화면에 표시합니다.
plt.show()

# 결과 이미지를 파일로 저장합니다.
plt.savefig('./result/corr.png')