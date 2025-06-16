import time
import pyautogui

def wait_and_click(image_name, timeout=15, confidence=0.8):
    """
    Поиск шаблона на экране и клик по нему.
    Ожидает появления изображения в течение timeout секунд.
    """
    print(f"🔍 Ожидание: {image_name}")
    start = time.time()
    while time.time() - start < timeout:
        location = pyautogui.locateCenterOnScreen(f"screenshots/{image_name}", confidence=confidence)
        if location:
            pyautogui.click(location)
            print(f"✅ Клик: {image_name}")
            return True
        time.sleep(0.5)
    print(f"❌ Не найдено: {image_name}")
    return False

def run_daily_main_actions(main_name):
    """
    Выполняет расширенные ежедневные действия для основы (главного аккаунта).
    main_name — имя основы (строка)
    Здесь будут расширенные действия: вход, сбор наград, дополнительные активности и т.д.
    """
    print(f'Начинаю расширенные ежедневные действия для основы: {main_name}')
    # TODO: добавить реальные расширенные действия
    print(f'Завершены расширенные ежедневные действия для основы: {main_name}') 
