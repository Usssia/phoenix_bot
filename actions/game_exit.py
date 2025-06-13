import time
import os
import pyautogui
from config import TEMPLATES_PATH


pyautogui.FAILSAFE = True

def wait_and_click(image_name, timeout=15, confidence=0.8):
    print(f"🔍 Ожидание: {image_name}")
    start = time.time()
    full_path = os.path.join(TEMPLATES_PATH, image_name)
    while time.time() - start < timeout:
        location = pyautogui.locateCenterOnScreen(full_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            print(f"✅ Клик: {image_name}")
            return True
        time.sleep(0.5)
    print(f"❌ Не найдено: {image_name}")
    return False

def exit_game(twin_name):
    """
    Выходит из игры под указанным твинком.
    twin_name — имя твинка (строка)
    Здесь будет логика выхода из игры (например, через меню).
    """
    print(f"[EXIT] Выход из твинка: {twin_name}")
    if not wait_and_click("open_menu.png", timeout=30):
        print("❌ Не найдена кнопка меню")
        return False
    if not wait_and_click("settings.png", timeout=20):
        print("❌ Не удалось открыть настройки")
        return False
    if not wait_and_click("change_server.png", timeout=20):
        print("❌ Не удалось нажать 'Смена сервера'")
        return False
    wait_and_click("close_popup.png", timeout=10)
    time.sleep(1)
    print("✅ Возврат к экрану выбора сервера завершён.")
    return True 