cmake_minimum_required(VERSION 3.15)
project(WindowsStageManager)

set(CMAKE_CXX_STANDARD 17)

file(GLOB CORE_SRC "src/core/*.cpp")
file(GLOB EVENTS_SRC "src/events/*.cpp")
file(GLOB UI_SRC "src/ui/*.cpp")
file(GLOB UTILS_SRC "src/utils/*.cpp")
set(API_SRC src/StageManagerAPI.cpp)

add_executable(WindowsStageManager
    ${CORE_SRC}
    ${EVENTS_SRC}
    ${UI_SRC}
    ${UTILS_SRC}
    ${API_SRC}
    src/main.cpp)

target_include_directories(WindowsStageManager PRIVATE src include)

target_link_libraries(WindowsStageManager
    user32
    dwmapi
    gdi32
    ole32
    oleaut32)

add_definitions(-DUNICODE -D_UNICODE)
