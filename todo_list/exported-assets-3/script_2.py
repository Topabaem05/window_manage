# Stage Manager 아키텍처의 주요 컴포넌트들과 그들의 책임을 정리
architecture_data = {
    '컴포넌트': [
        'WindowManager', 'EventHandler', 'ThumbnailRenderer', 
        'StageManager', 'LayoutEngine', 'AnimationSystem',
        'AppGroupManager', 'VirtualDesktopInterface', 'HookManager'
    ],
    '주요 책임': [
        '전체 창 관리 및 조정',
        '시스템 이벤트 처리 및 콜백',
        '창 미리보기 생성 및 관리',
        'Stage Manager 핵심 로직',
        '창 배치 및 레이아웃 계산',
        'UI 전환 애니메이션',
        '앱 그룹화 및 워크스페이스',
        '가상 데스크톱 연동',
        '시스템 훅 관리'
    ],
    '사용 API': [
        'EnumWindows, SetWindowPos',
        'SetWinEventHook, WinEventProc',
        'DwmRegisterThumbnail, GDI+',
        '모든 컴포넌트 통합',
        'GetWindowRect, SetWindowPos',
        'Direct2D, DirectComposition',
        'FindWindow, GetWindowText',
        'IVirtualDesktopManager',
        'SetWindowsHookEx'
    ],
    '상호작용': [
        'EventHandler, StageManager와 연동',
        'WindowManager에게 이벤트 전달',
        'StageManager에게 미리보기 제공',
        'LayoutEngine, AppGroupManager 조정',
        'WindowManager에게 배치 정보 제공',
        'ThumbnailRenderer와 협력',
        'StageManager와 데이터 교환',
        'StageManager와 통합',
        'EventHandler에게 이벤트 전달'
    ]
}

import pandas as pd
arch_df = pd.DataFrame(architecture_data)
print("Stage Manager 아키텍처 컴포넌트:")
print(arch_df.to_string(index=False))

# CSV로 저장
arch_df.to_csv('stage_manager_architecture.csv', index=False, encoding='utf-8-sig')
print("\n\n아키텍처 문서가 CSV로 저장되었습니다.")