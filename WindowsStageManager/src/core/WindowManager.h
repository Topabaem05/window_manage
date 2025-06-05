#pragma once
#include <windows.h>
#include <dwmapi.h>
#include <vector>

class WindowManager {
private:
    HWINEVENTHOOK eventHook{};
    std::vector<HWND> managedWindows;
    static WindowManager* instance;

    WindowManager() = default;

public:
    static WindowManager* GetInstance();
    bool Initialize();
    void Cleanup();
    void EnumerateWindows();
    void ArrangeWindows();
    void SetWindowPosition(HWND hwnd, int x, int y, int width, int height);
    void ShowWindowHandle(HWND hwnd);
    void HideWindowHandle(HWND hwnd);
    const std::vector<HWND>& GetManagedWindows() const { return managedWindows; }

    static void CALLBACK WinEventProc(HWINEVENTHOOK hWinEventHook,
                                      DWORD event,
                                      HWND hwnd,
                                      LONG idObject,
                                      LONG idChild,
                                      DWORD dwEventThread,
                                      DWORD dwmsEventTime);

    void CreateAppGroup(const std::vector<HWND>& windows);
    void UpdateThumbnails();
    void ShowStageManager();
    void HideStageManager();
};
