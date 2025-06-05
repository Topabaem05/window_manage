#include "WindowUtils.h"

namespace WindowUtils {
bool IsAltTabWindow(HWND hwnd) {
    if (!IsWindowVisible(hwnd)) return false;
    HWND hwndTry, hwndWalk = NULL;
    hwndTry = GetAncestor(hwnd, GA_ROOTOWNER);
    while (hwndTry != hwndWalk) {
        hwndWalk = hwndTry;
        hwndTry = GetLastActivePopup(hwndWalk);
        if (IsWindowVisible(hwndTry)) break;
    }
    return hwndWalk == hwnd;
}
}
