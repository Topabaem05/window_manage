#include "StageManager.h"
#include <algorithm>

StageManager* StageManager::instance = nullptr;

StageManager::StageManager() {
    instance = this;
    thumbnailRenderer = new ThumbnailRenderer(nullptr);
}

StageManager::~StageManager() {
    if (sidebarWindow) {
        DestroyWindow(sidebarWindow);
        sidebarWindow = nullptr;
    }
    delete thumbnailRenderer;
}

void StageManager::ActivateStageManager() {
    if (isActive) return;
    isActive = true;

    WindowManager* wm = WindowManager::GetInstance();
    wm->EnumerateWindows();
    appGroups.clear();

    AppGroup group{};
    group.isActive = true;
    group.windows = wm->GetManagedWindows();
    appGroups[0] = group;

    CreateSidebar();
    UpdateSidebar();
    UpdateGroupVisibility();
}

void StageManager::DeactivateStageManager() {
    isActive = false;
    if (sidebarWindow) {
        DestroyWindow(sidebarWindow);
        sidebarWindow = nullptr;
    }
    WindowManager* wm = WindowManager::GetInstance();
    for (auto& [id, group] : appGroups) {
        for (HWND hwnd : group.windows) {
            wm->ShowWindowHandle(hwnd);
        }
    }
}

void StageManager::CreateSidebar() {
    if (sidebarWindow) return;

    WNDCLASS wc{};
    wc.lpfnWndProc = SidebarProc;
    wc.hInstance = GetModuleHandle(nullptr);
    wc.lpszClassName = L"StageManagerSidebar";
    RegisterClass(&wc);

    sidebarWindow = CreateWindowExW(WS_EX_TOPMOST | WS_EX_TOOLWINDOW,
                                   wc.lpszClassName,
                                   L"Stage Manager",
                                   WS_POPUP,
                                   0, 0, 200, GetSystemMetrics(SM_CYSCREEN),
                                   nullptr, nullptr, wc.hInstance, nullptr);
    ShowWindow(sidebarWindow, SW_SHOWNOACTIVATE);
}

void StageManager::UpdateSidebar() {
    if (!sidebarWindow) return;
    InvalidateRect(sidebarWindow, nullptr, TRUE);
}

void StageManager::SwitchToGroup(int groupId) {
    for (auto& [id, group] : appGroups) {
        group.isActive = (id == groupId);
    }
    ArrangeActiveGroup();
}

void StageManager::AddWindowToGroup(HWND hwnd, int groupId) {
    appGroups[groupId].windows.push_back(hwnd);
}

void StageManager::RemoveWindowFromGroup(HWND hwnd) {
    for (auto& [id, group] : appGroups) {
        auto it = std::find(group.windows.begin(), group.windows.end(), hwnd);
        if (it != group.windows.end()) {
            group.windows.erase(it);
            break;
        }
    }
}

void StageManager::ArrangeActiveGroup() {
    for (auto& [id, group] : appGroups) {
        if (!group.isActive) continue;
        int x = 220;
        int y = 0;
        int width = 800;
        int height = 600;
        WindowManager* wm = WindowManager::GetInstance();
        for (HWND hwnd : group.windows) {
            wm->SetWindowPosition(hwnd, x, y, width, height);
            x += 30; y += 30;
        }
        break;
    }

    UpdateGroupVisibility();
}

void StageManager::UpdateGroupVisibility() {
    WindowManager* wm = WindowManager::GetInstance();
    for (auto& [id, group] : appGroups) {
        for (HWND hwnd : group.windows) {
            if (group.isActive) {
                wm->ShowWindowHandle(hwnd);
            } else {
                wm->HideWindowHandle(hwnd);
            }
        }
    }
}

void StageManager::CalculateWindowPositions() {
    // Placeholder for future layout calculations
}

void StageManager::AnimateTransition() {
    // Placeholder for transition animations
}

LRESULT CALLBACK StageManager::SidebarProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg) {
        case WM_DESTROY:
            instance->sidebarWindow = nullptr;
            return 0;
        default:
            return DefWindowProc(hwnd, msg, wParam, lParam);
    }
}
