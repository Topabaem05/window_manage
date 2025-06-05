#pragma once
#include "WindowManager.h"
#include "../ui/ThumbnailRenderer.h"
#include <map>
#include <vector>

struct AppGroup {
    std::vector<HWND> windows;
    POINT position{};
    SIZE size{};
    bool isActive{false};
};

class StageManager {
private:
    std::map<int, AppGroup> appGroups;
    ThumbnailRenderer* thumbnailRenderer{nullptr};
    HWND sidebarWindow{nullptr};
    bool isActive{false};
    static StageManager* instance;
    static LRESULT CALLBACK SidebarProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam);

public:
    StageManager();
    ~StageManager();

    void ActivateStageManager();
    void DeactivateStageManager();
    void CreateSidebar();
    void UpdateSidebar();
    void SwitchToGroup(int groupId);
    void AddWindowToGroup(HWND hwnd, int groupId);
    void RemoveWindowFromGroup(HWND hwnd);

    void ArrangeActiveGroup();
    void UpdateGroupVisibility();
    void CalculateWindowPositions();
    void AnimateTransition();
};
