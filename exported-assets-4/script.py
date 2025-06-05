import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 창 그룹화와 배치 API 타입 정의
api_types = ['Win32 API', 'COM Interface', '.NET/WPF', '자동화 라이브러리', 'DirectComposition', '서드파티 도구']

# 각 타입별 중요 API/라이브러리 정의
api_libs = {
    'Win32 API': ['SetWindowPos', 'FindWindow', 'EnumWindows', 'GetWindowRect', 'SetWinEventHook'],
    'COM Interface': ['ITaskbarList', 'IThumbnailProvider', 'IShellItemImageFactory', 'IVirtualDesktopManager'],
    '.NET/WPF': ['System.Windows.Window', 'WindowsUIAutomation', 'WPF Window Manager'],
    '자동화 라이브러리': ['UIAutomation', 'UIAComWrapper', 'Python-UIAutomation-for-Windows'],
    'DirectComposition': ['DwmRegisterThumbnail', 'DwmUpdateThumbnailProperties', 'DirectComposition API'],
    '서드파티 도구': ['PowerToys FancyZones', 'Window Layout Manager', 'Groupy by Stardock']
}

# 난이도와 기능성 점수 (1-10)
api_complexity = {
    'Win32 API': 8, 
    'COM Interface': 9, 
    '.NET/WPF': 6, 
    '자동화 라이브러리': 5, 
    'DirectComposition': 7,
    '서드파티 도구': 2
}

api_functionality = {
    'Win32 API': 7, 
    'COM Interface': 8, 
    '.NET/WPF': 7, 
    '자동화 라이브러리': 9, 
    'DirectComposition': 8,
    '서드파티 도구': 6
}

# API 개수 시각화
plt.figure(figsize=(12, 6))
plt.bar(api_types, [len(api_libs[t]) for t in api_types], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('창 그룹화와 배치 자동화를 위한 API/라이브러리 유형별 개수')
plt.ylabel('API/라이브러리 개수')
plt.tight_layout()
plt.savefig('api_count_chart.png')
plt.close()

# 난이도와 기능성 비교 차트
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(api_types))
width = 0.35

complexity = ax.bar(x - width/2, [api_complexity[t] for t in api_types], width, label='구현 난이도', color='salmon')
functionality = ax.bar(x + width/2, [api_functionality[t] for t in api_types], width, label='기능성', color='lightgreen')

ax.set_ylabel('점수 (1-10)')
ax.set_title('API/라이브러리 유형별 구현 난이도와 기능성 비교')
ax.set_xticks(x)
ax.set_xticklabels(api_types, rotation=45, ha='right')
ax.legend()

ax.bar_label(complexity, padding=3)
ax.bar_label(functionality, padding=3)

fig.tight_layout()
plt.savefig('api_complexity_functionality.png')
plt.close()

# API 종류와 기능별 데이터 프레임 생성
data = []
for api_type in api_types:
    for api in api_libs[api_type]:
        data.append({
            'API/라이브러리': api,
            '유형': api_type
        })

df = pd.DataFrame(data)
print("API/라이브러리 목록:")
print(df)

# CSV로 저장
df.to_csv('window_management_apis.csv', index=False)
print("\nCSV 파일로 저장되었습니다: window_management_apis.csv")

# API 유형별 구현 난이도와 기능성 데이터 프레임 생성
comparison_data = []
for api_type in api_types:
    comparison_data.append({
        'API/라이브러리 유형': api_type,
        '구현 난이도 (1-10)': api_complexity[api_type],
        '기능성 (1-10)': api_functionality[api_type],
        '포함된 API/라이브러리 수': len(api_libs[api_type])
    })

comparison_df = pd.DataFrame(comparison_data)
print("\nAPI/라이브러리 유형별 비교:")
print(comparison_df)

# CSV로 저장
comparison_df.to_csv('api_comparison.csv', index=False)
print("\nCSV 파일로 저장되었습니다: api_comparison.csv")