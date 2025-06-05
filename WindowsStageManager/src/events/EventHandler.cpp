#include "EventHandler.h"
#include "../core/WindowManager.h"

void EventHandler::Initialize() {
    SetWinEventHook(
        EVENT_SYSTEM_FOREGROUND,
        EVENT_OBJECT_DESTROY,
        NULL,
        WindowManager::WinEventProc,
        0,
        0,
        WINEVENT_OUTOFCONTEXT | WINEVENT_SKIPOWNPROCESS);
}
