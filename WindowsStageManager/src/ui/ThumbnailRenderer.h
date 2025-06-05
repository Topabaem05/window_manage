#pragma once
#include <windows.h>
#include <dwmapi.h>
#include <vector>

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

    void RenderSidebarThumbnails();
    void UpdateThumbnailPositions();
};
