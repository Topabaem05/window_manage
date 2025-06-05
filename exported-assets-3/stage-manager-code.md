# Windows Stage Manager 개발 - 핵심 코드 구조

## 1. 프로젝트 구조

```
WindowsStageManager/
├── src/
│   ├── core/
│   │   ├── WindowManager.h
│   │   ├── WindowManager.cpp
│   │   ├── StageManager.h
│   │   └── StageManager.cpp
│   ├── events/
│   │   ├── EventHandler.h
│   │   ├── EventHandler.cpp
│   │   └── HookManager.cpp
│   ├── ui/
│   │   ├── ThumbnailRenderer.h
│   │   ├── ThumbnailRenderer.cpp
│   │   ├── LayoutEngine.cpp
│   │   └── AnimationSystem.cpp
│   ├── utils/
│   │   ├── WindowUtils.h
│   │   └── WindowUtils.cpp
│   └── main.cpp
├── include/
│   └── StageManagerAPI.h
└── resources/
    └── icons/
```

## 2. 핵심 헤더 파일 (WindowManager.h)

```cpp
#pragma once
#include <windows.h>
#include <dwmapi.h>
#include <vector>
#include <memory>

class WindowManager {
private:
    HWINEVENTHOOK eventHook;
    std::vector<HWND> managedWindows;
    static WindowManager* instance;

public:
    static WindowManager* GetInstance();
    
    // 창 관리 핵심 함수들
    bool Initialize();
    void Cleanup();
    void EnumerateWindows();
    void ArrangeWindows();
    void SetWindowPosition(HWND hwnd, int x, int y, int width, int height);
    
    // 이벤트 처리
    static void CALLBACK WinEventProc(
        HWINEVENTHOOK hWinEventHook,
        DWORD event,
        HWND hwnd,
        LONG idObject,
        LONG idChild,
        DWORD dwEventThread,
        DWORD dwmsEventTime
    );
    
    // Stage Manager 전용 함수들
    void CreateAppGroup(const std::vector<HWND>& windows);
    void UpdateThumbnails();
    void ShowStageManager();
    void HideStageManager();
};
```

## 3. Stage Manager 핵심 클래스 (StageManager.h)

```cpp
#pragma once
#include "WindowManager.h"
#include "ThumbnailRenderer.h"
#include <map>

struct AppGroup {
    std::vector<HWND> windows;
    POINT position;
    SIZE size;
    bool isActive;
};

class StageManager {
private:
    std::map<int, AppGroup> appGroups;
    ThumbnailRenderer* thumbnailRenderer;
    HWND sidebarWindow;
    bool isActive;

public:
    StageManager();
    ~StageManager();
    
    // Stage Manager 기능
    void ActivateStageManager();
    void DeactivateStageManager();
    void CreateSidebar();
    void UpdateSidebar();
    void SwitchToGroup(int groupId);
    void AddWindowToGroup(HWND hwnd, int groupId);
    void RemoveWindowFromGroup(HWND hwnd);
    
    // 레이아웃 관리
    void ArrangeActiveGroup();
    void CalculateWindowPositions();
    void AnimateTransition();
};
```

## 4. 이벤트 처리 시스템 (EventHandler.cpp)

```cpp
#include "EventHandler.h"
#include "WindowManager.h"

void EventHandler::Initialize() {
    // 윈도우 이벤트 훅 설정
    eventHook = SetWinEventHook(
        EVENT_SYSTEM_FOREGROUND,  // 최소 이벤트
        EVENT_OBJECT_DESTROY,     // 최대 이벤트
        NULL,                     // DLL 핸들
        WindowManager::WinEventProc, // 콜백 함수
        0,                        // 프로세스 ID (0 = 모든 프로세스)
        0,                        // 스레드 ID (0 = 모든 스레드)
        WINEVENT_OUTOFCONTEXT | WINEVENT_SKIPOWNPROCESS
    );
}

// 윈도우 이벤트 콜백 함수
void CALLBACK WindowManager::WinEventProc(
    HWINEVENTHOOK hWinEventHook,
    DWORD event,
    HWND hwnd,
    LONG idObject,
    LONG idChild,
    DWORD dwEventThread,
    DWORD dwmsEventTime
) {
    if (idObject != OBJID_WINDOW) return;
    
    WindowManager* manager = WindowManager::GetInstance();
    
    switch (event) {
        case EVENT_SYSTEM_FOREGROUND:
            manager->OnWindowActivated(hwnd);
            break;
        case EVENT_OBJECT_CREATE:
            manager->OnWindowCreated(hwnd);
            break;
        case EVENT_OBJECT_DESTROY:
            manager->OnWindowDestroyed(hwnd);
            break;
    }
}
```

## 5. 썸네일 렌더링 (ThumbnailRenderer.h)

```cpp
#pragma once
#include <windows.h>
#include <dwmapi.h>

class ThumbnailRenderer {
private:
    HWND targetWindow;
    std::vector<HTHUMBNAIL> thumbnails;

public:
    ThumbnailRenderer(HWND target);
    ~ThumbnailRenderer();
    
    HTHUMBNAIL CreateThumbnail(HWND sourceWindow);
    void UpdateThumbnail(HTHUMBNAIL thumbnail, const RECT& dest);
    void SetThumbnailOpacity(HTHUMBNAIL thumbnail, BYTE opacity);
    void RemoveThumbnail(HTHUMBNAIL thumbnail);
    
    // Stage Manager 전용
    void RenderSidebarThumbnails();
    void UpdateThumbnailPositions();
};
```

## 6. 메인 함수 구조 (main.cpp)

```cpp
#include <windows.h>
#include "core/WindowManager.h"
#include "core/StageManager.h"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, 
                   LPSTR lpCmdLine, int nCmdShow) {
    
    // COM 초기화
    CoInitialize(NULL);
    
    // Window Manager 초기화
    WindowManager* windowManager = WindowManager::GetInstance();
    if (!windowManager->Initialize()) {
        return -1;
    }
    
    // Stage Manager 생성
    StageManager stageManager;
    
    // 메시지 루프
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    
    // 정리
    windowManager->Cleanup();
    CoUninitialize();
    
    return static_cast<int>(msg.wParam);
}
```

## 7. 주요 Windows API 호출 예시

```cpp
// 모든 창 열거
BOOL CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lParam) {
    if (IsWindowVisible(hwnd) && !IsIconic(hwnd)) {
        std::vector<HWND>* windows = 
            reinterpret_cast<std::vector<HWND>*>(lParam);
        windows->push_back(hwnd);
    }
    return TRUE;
}

void WindowManager::EnumerateWindows() {
    managedWindows.clear();
    EnumWindows(EnumWindowsProc, 
                reinterpret_cast<LPARAM>(&managedWindows));
}

// 창 위치 설정
void WindowManager::SetWindowPosition(HWND hwnd, int x, int y, 
                                     int width, int height) {
    SetWindowPos(hwnd, HWND_TOP, x, y, width, height,
                 SWP_NOZORDER | SWP_NOACTIVATE);
}

// 썸네일 생성
HTHUMBNAIL ThumbnailRenderer::CreateThumbnail(HWND sourceWindow) {
    HTHUMBNAIL thumbnail;
    HRESULT hr = DwmRegisterThumbnail(targetWindow, sourceWindow, &thumbnail);
    
    if (SUCCEEDED(hr)) {
        // 썸네일 속성 설정
        DWM_THUMBNAIL_PROPERTIES props = {};
        props.dwFlags = DWM_TNP_RECTDESTINATION | DWM_TNP_OPACITY;
        props.opacity = 200; // 투명도 설정
        // 위치는 나중에 설정
        
        DwmUpdateThumbnailProperties(thumbnail, &props);
        return thumbnail;
    }
    return NULL;
}
```

## 8. 빌드 설정

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.15)
project(WindowsStageManager)

set(CMAKE_CXX_STANDARD 17)

# Windows API 라이브러리 링크
target_link_libraries(WindowsStageManager 
    user32.lib
    dwmapi.lib
    gdi32.lib
    ole32.lib
    oleaut32.lib
)

# 컴파일 옵션
add_definitions(-DUNICODE -D_UNICODE)
```

이 코드 구조는 macOS Stage Manager의 핵심 기능을 Windows에서 구현하기 위한 기본 틀을 제공합니다.