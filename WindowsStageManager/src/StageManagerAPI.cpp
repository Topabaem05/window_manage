#include "core/StageManager.h"
#include "../include/StageManagerAPI.h"

static StageManager g_stageManager;

namespace StageManagerAPI {
void Show() {
    g_stageManager.ActivateStageManager();
}

void Hide() {
    g_stageManager.DeactivateStageManager();
}
}
