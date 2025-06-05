#include "ThumbnailRenderer.h"

ThumbnailRenderer::ThumbnailRenderer(HWND target) : targetWindow(target) {}

ThumbnailRenderer::~ThumbnailRenderer() {
    for (auto thumb : thumbnails) {
        DwmUnregisterThumbnail(thumb);
    }
}

HTHUMBNAIL ThumbnailRenderer::CreateThumbnail(HWND sourceWindow) {
    HTHUMBNAIL thumb{};
    if (SUCCEEDED(DwmRegisterThumbnail(targetWindow, sourceWindow, &thumb))) {
        thumbnails.push_back(thumb);
    }
    return thumb;
}

void ThumbnailRenderer::UpdateThumbnail(HTHUMBNAIL thumbnail, const RECT& dest) {
    DWM_THUMBNAIL_PROPERTIES props{};
    props.dwFlags = DWM_TNP_RECTDESTINATION;
    props.rcDestination = dest;
    DwmUpdateThumbnailProperties(thumbnail, &props);
}

void ThumbnailRenderer::SetThumbnailOpacity(HTHUMBNAIL thumbnail, BYTE opacity) {
    DWM_THUMBNAIL_PROPERTIES props{};
    props.dwFlags = DWM_TNP_OPACITY;
    props.opacity = opacity;
    DwmUpdateThumbnailProperties(thumbnail, &props);
}

void ThumbnailRenderer::RemoveThumbnail(HTHUMBNAIL thumbnail) {
    DwmUnregisterThumbnail(thumbnail);
    thumbnails.erase(std::remove(thumbnails.begin(), thumbnails.end(), thumbnail), thumbnails.end());
}

void ThumbnailRenderer::RenderSidebarThumbnails() {
    // TODO: render thumbnails in sidebar
}

void ThumbnailRenderer::UpdateThumbnailPositions() {
    // TODO: update sidebar layout
}
