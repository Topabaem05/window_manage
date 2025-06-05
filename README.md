# Windows Stage Manager

This project is an experimental window management tool inspired by macOS Stage Manager. It is written in C++ and uses Win32 and DWM APIs.
Recent work integrates ideas from the open source [Stage Manager for Windows](https://github.com/awaescher/StageManager) project. Windows are grouped and hidden when inactive to mimic macOS Stage Manager.

## Building with Visual Studio

1. Install **Visual Studio 2022** (or later) with the **Desktop development with C++** workload and the Windows 10/11 SDK.
2. In Visual Studio select **File > Open > CMake...** and choose the `WindowsStageManager` folder.
3. Visual Studio will configure the project automatically. You can also configure from the Developer PowerShell:

   ```
   cmake -S WindowsStageManager -B build
   ```

4. Build the `WindowsStageManager` target in your chosen configuration (Debug/Release).
5. Run the application from Visual Studio or from `build/WindowsStageManager.exe`.

## Project Structure

- **WindowsStageManager/** - CMake project containing the source
  - `src/core` - `WindowManager` and `StageManager` classes
  - `src/events` - event hooks
  - `src/ui` - thumbnail renderer and layout system
  - `src/utils` - helper utilities
  - `include` - public headers

The project links against `user32.lib`, `dwmapi.lib`, `gdi32.lib`, `ole32.lib`, and `oleaut32.lib` which are included with the Windows SDK.

