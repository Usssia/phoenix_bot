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

def launch_game():
    """
    Запускает игру (двойной клик по иконке)
    """
    print("🎮 Запускаем игру...")
    time.sleep(5)  # Даём время на загрузку рабочего стола
    
    # Ищем иконку игры в течение 30 секунд
    start_time = time.time()
    while time.time() - start_time < 30:
        try:
            game_icon_location = pyautogui.locateCenterOnScreen(
                os.path.join(TEMPLATES_PATH, "game_icon.png"),
                confidence=0.7
            )
            if game_icon_location:
                pyautogui.doubleClick(game_icon_location)
                print("✅ Сделали двойной клик по иконке игры")
                time.sleep(5)  # Ждём запуска
                return True
        except Exception as error:
            print(f"⚠️ Ошибка при поиске иконки игры: {error}")
        time.sleep(0.5)
    print("❌ Не удалось найти иконку игры")
    return False

def enter_game(twin_id: str):
    """
    Вход в игру под указанным твином
    twin_id - имя твина (например, "usssia_S172")
    """
    print(f"[ENTER] Вход в твинка: {twin_id}")
    
    # 1. Запускаем игру
    if not launch_game():
        print("❌ Не удалось запустить игру")
        return False
    
    # 2. Ждём появления и кликаем по иконке профиля
    if not wait_and_click("profile_icon.png", timeout=20):
        print("❌ Не найдена иконка профиля")
        return False
    time.sleep(2)
    
    # 3. Кликаем по кнопке выхода из аккаунта
    if not wait_and_click("exit_account.png", timeout=15):
        print("❌ Не найдена кнопка выхода из аккаунта")
        return False
    time.sleep(1)
    
    # 4. Подтверждаем выход
    if not wait_and_click("confirm_exit.png", timeout=10):
        print("❌ Не найдена кнопка подтверждения выхода")
        return False
    time.sleep(3)  # Ждём возврата к экрану выбора аккаунта
    
    # 5. Кликаем по нужному аккаунту (например, usssia_bat.png)
    account_image = f"{twin_id.lower()}.png"  # Например, usssia_s172.png
    if not wait_and_click(account_image, timeout=20):
        print(f"❌ Не найден аккаунт: {account_image}")
        return False
    time.sleep(5)  # Ждём загрузки аккаунта
    
    # 6. Ждём появления кнопки "Поменять сервер"
    if not wait_and_click("server.png", timeout=30):
        print("❌ Не найдена кнопка 'Поменять сервер'")
        return False
    
    # 7. Извлекаем номер сервера из имени твина
    if "_" in twin_id and "S" in twin_id:
        server_number = twin_id.split("_")[-1].replace("S", "")
        server_image = f"server{server_number}.png"
    else:
        print(f"⚠️ Невозможно извлечь номер сервера из: {twin_id}")
        return False
    
    # 8. Выбираем нужный сервер
    if not wait_and_click(server_image, timeout=20):
        print(f"⚠️ Сервер не найден: {server_image}")
        return False
    
    # 9. Нажимаем "Начать игру"
    if not wait_and_click("start-game.png", timeout=30):
        print("❌ Не найдена кнопка 'Начать игру'")
        return False
    
    # 10. Ждём загрузки интерфейса
    print("[WAIT] Загружается интерфейс твинка...")
    time.sleep(10)
    return True 