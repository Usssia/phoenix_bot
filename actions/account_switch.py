import time
import os
import pyautogui
from config import TEMPLATES_PATH


def wait_and_click(image_name, timeout=30, confidence=0.7):
    """
    Ждёт появления изображения и кликает по нему.
    """
    print(f"🔍 Ожидание: {image_name}")
    start = time.time()
    full_path = os.path.join(TEMPLATES_PATH, image_name)
    while time.time() - start < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(full_path, confidence=confidence)
            if location:
                pyautogui.click(location)
                print(f"✅ Клик: {image_name}")
                return True
        except Exception as e:
            print(f"⚠️ Ошибка при поиске: {e}")
        time.sleep(0.5)
    print(f"❌ Не найдено: {image_name}")
    return False

# --- Последовательность шагов ---
def switch_account_sequence():
    # 1. Клик по иконке игры
    wait_and_click("game_icon.png", timeout=30)
    time.sleep(5)
    # 2. Клик по иконке профиля
    wait_and_click("profile_icon.png", timeout=30)
    time.sleep(5)
    # Здесь будут следующие шаги по вашему сценарию
