# VSCode Window Transparency Script

This script automatically sets the transparency of your VSCode windows when they are opened. It works with multiple VSCode windows and applies the transparency only to those that are not already transparent.

## Script Overview

The script does the following:
1. **Identifies VSCode windows**:
   It uses the `wmctrl` command to get a list of open windows and selects those whose title contains "Visual Studio Code".
   
2. **Checks transparency**:
   For each window, it checks whether transparency is already applied by using the `xprop` command to retrieve the `_NET_WM_WINDOW_OPACITY` value.

3. **Applies transparency only if necessary**:
   If the window does not have transparency set, the script applies the transparency using `xprop`.

4. **Supports multiple windows**:
   The script can handle multiple VSCode windows running simultaneously.

## How to Use the Script

1. **Install the required utilities**:
   Make sure the `wmctrl` and `x11-utils` utilities are installed:
   ```bash
   sudo apt install wmctrl x11-utils

2. **Save the script: Save the script as set_vscode_opacity_multi.py.**

3. **Make the script executable:**
    ```bash
    chmod +x set_vscode_opacity_multi.py

4. **Run the script: Run the script before or after opening VSCode:**
    ```bash
    python3 set_vscode_opacity_multi.py

**Example Output:**
If two VSCode windows are open, you might see the following output:

    Waiting for VSCode windows...
    Found 2 VSCode windows.
    Setting opacity for window 0x00c00004...
    Opacity for window 0x00c00004 set to 0xBFFFFFFF.
    Window 0x00c0001a is already transparent.

## Automating the Script

If you want the script to run automatically whenever VSCode is launched, you can create a .desktop file for VSCode in ~/.local/share/applications/.

Create a .desktop file: Create or edit the .desktop file for VSCode, typically located at ~/.local/share/applications/code.desktop.

Modify the Exec line: In the Exec section, add the script call before launching VSCode:

    Exec=/bin/bash -c "python3 /path/to/set_vscode_opacity.py & code"

This will ensure that the script is executed every time you start VSCode, automatically applying the opacity without any additional steps.

## Solo code teminal 

   ```bash
   xprop -format _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY 0xCFFFFFFF
