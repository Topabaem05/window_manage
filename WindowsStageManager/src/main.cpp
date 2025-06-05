#include <windows.h>
#include "core/WindowManager.h"
#include "core/StageManager.h"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
                   LPSTR lpCmdLine, int nCmdShow) {
    CoInitialize(NULL);

    WindowManager* windowManager = WindowManager::GetInstance();
    if (!windowManager->Initialize()) {
        return -1;
    }

    StageManager stageManager;

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    windowManager->Cleanup();
    CoUninitialize();
    return static_cast<int>(msg.wParam);
}
