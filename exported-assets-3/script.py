# Stage Manager 개발에 필요한 주요 Windows API와 기능들을 CSV로 정리
import pandas as pd

# 주요 Windows API와 기능 매핑 표 생성
api_data = {
    '카테고리': [
        '창 관리', '창 관리', '창 관리', '창 관리',
        '이벤트 처리', '이벤트 처리', '이벤트 처리',
        '데스크톱 컴포지션', '데스크톱 컴포지션', '데스크톱 컴포지션',
        '가상 데스크톱', '가상 데스크톱',
        '그래픽', '그래픽', '그래픽'
    ],
    'API/기능': [
        'EnumWindows', 'SetWindowPos', 'GetWindowRect', 'FindWindow',
        'SetWinEventHook', 'SetWindowsHookEx', 'WinEventProc',
        'DWM (Desktop Window Manager)', 'DwmRegisterThumbnail', 'DwmUpdateThumbnailProperties',
        'VirtualDesktopAPI', 'IVirtualDesktopManager',
        'GDI+', 'Direct2D', 'DirectComposition'
    ],
    '설명': [
        '모든 활성 창을 열거하여 목록 생성',
        '창의 위치, 크기, Z-order 변경',
        '창의 현재 위치와 크기 정보 획득',
        '특정 창 핸들 찾기',
        '시스템 이벤트 (창 생성/삭제/포커스) 모니터링',
        '키보드/마우스 입력 이벤트 후킹',
        '이벤트 콜백 함수 처리',
        'Windows 창 컴포지션 시스템',
        '창의 썸네일 미리보기 생성',
        '썸네일 속성 (크기, 투명도) 업데이트',
        'Windows 10+ 가상 데스크톱 기능',
        '가상 데스크톱 관리 인터페이스',
        '2D 그래픽 렌더링',
        '하드웨어 가속 2D 그래픽',
        '고성능 합성 API'
    ],
    'Stage Manager 기능': [
        '활성 앱 목록 관리',
        '창 배치 및 그룹화',
        '창 위치 추적',
        '특정 앱 창 식별',
        '앱 상태 변화 감지',
        '사용자 입력 처리',
        '실시간 이벤트 반응',
        '창 효과 및 애니메이션',
        '왼쪽 사이드바 미리보기',
        '썸네일 시각화',
        '다중 데스크톱 지원',
        '데스크톱 간 앱 이동',
        '사용자 인터페이스 렌더링',
        '부드러운 애니메이션',
        '레이어 합성'
    ]
}

df = pd.DataFrame(api_data)
df.to_csv('stage_manager_apis.csv', index=False, encoding='utf-8-sig')
print("Stage Manager 개발용 Windows API 매핑표가 생성되었습니다.")
print(df.to_string(index=False))