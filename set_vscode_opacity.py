import subprocess
import time

def is_window_transparent(window_id):
    """
    Проверяет, установлена ли прозрачность для окна.
    """
    try:
        # Получение текущего значения прозрачности окна
        result = subprocess.run(
            ["xprop", "-id", window_id, "_NET_WM_WINDOW_OPACITY"],
            stdout=subprocess.PIPE, text=True, stderr=subprocess.DEVNULL
        )
        
        output = result.stdout.strip()
        print(output)
        return output == "_NET_WM_WINDOW_OPACITY:  not found."
    except Exception as e:
        print(f"Ошибка при проверке прозрачности для окна {window_id}: {e}")
        return False


def get_vscode_windows():
    """
    Получает список окон с названием, содержащим 'Visual Studio Code'.
    """
    try:
        # Получение списка окон с использованием wmctrl
        result = subprocess.run(["wmctrl", "-l"], stdout=subprocess.PIPE, text=True)
        windows = result.stdout.strip().split("\n")

        vscode_windows = []
        for window in windows:
            if "Visual Studio Code" in window:
                if is_window_transparent(window):
                    window_id = window.split()[0]
                    vscode_windows.append(window_id)
        return vscode_windows
    except Exception as e:
        print(f"Ошибка при поиске окон VSCode: {e}")
        return []

def set_window_opacity(window_id, opacity="0xBFFFFFFF"):
    """
    Устанавливает прозрачность для заданного окна.
    """
    try:
        subprocess.run([
            "xprop",
            "-id", window_id,
            "-format", "_NET_WM_WINDOW_OPACITY", "32c",
            "-set", "_NET_WM_WINDOW_OPACITY", opacity
        ])
        print(f"Прозрачность для окна {window_id} установлена на {opacity}.")
    except Exception as e:
        print(f"Ошибка при установке прозрачности для окна {window_id}: {e}")

def main():
    print("Ожидание окон VSCode...")
    while True:
        windows = get_vscode_windows()
        if windows:
            print(f"Найдено {len(windows)} окон VSCode.")
            for window_id in windows:
                print(f"Устанавливаем прозрачность для окна {window_id}...")
                set_window_opacity(window_id)
            break
        else:
            print("Окна VSCode не найдены, повторная проверка через 2 секунды...")
        time.sleep(2)

if __name__ == "__main__":
    main()
