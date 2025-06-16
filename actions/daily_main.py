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
    
def if_found_then_click(image_name, x, y, confidence=0.8, timeout=5):
    """
    Если на экране найдена картинка — клик по заданным координатам (x, y).
    Если нет — шаг пропускается.
    """
    print(f"🔍 Проверка: {image_name}")
    start = time.time()
    while time.time() - start < timeout:
        if pyautogui.locateOnScreen(f"screenshots/{image_name}", confidence=confidence):
            print(f"✅ Найдено {image_name} — кликаю по координате ({x}, {y})")
            pyautogui.click(x, y)
            return True
        time.sleep(0.5)
    print(f"❌ {image_name} не найдено — шаг пропущен")
    return False
def drag_left(start_x, start_y, distance=300, duration=0.5):
    """
    Зажимает левую кнопку мыши в точке (start_x, start_y) и тянет влево на заданное расстояние.
    """
    print(f"🖱️ Зажимаю мышь и веду влево от ({start_x}, {start_y}) на {distance}px")
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(start_x - distance, start_y, duration=duration)
    pyautogui.mouseUp()
    print("✅ Свайп влево завершён")

def drag_right(start_x, start_y, distance=300, duration=0.5):
    """
    Зажимает левую кнопку мыши в точке (start_x, start_y) и тянет вправо на заданное расстояние.
    """
    print(f"🖱️ Зажимаю мышь и веду вправо от ({start_x}, {start_y}) на {distance}px")
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(start_x + distance, start_y, duration=duration)
    pyautogui.mouseUp()
    print("✅ Движение завершено")

def run_daily_main_actions(main_name):
    """
    Выполняет ежедневные действия для главного аккаунта (основы)
    """
    print(f'📅 Начинаю ежедневные задачи для ОСНОВЫ: {main_name}')

    # === Шаг 1. Проверка на открытие окна "Охота" ===
    print("🧭 Проверка на 'Охоту'")
    if wait_and_click("pereyti.png", timeout=5):
        print("📌 Обнаружено окно 'Охота' — выходим из него...")
        time.sleep(5)
        wait_and_click("back_icon.png")
        time.sleep(1)
        wait_and_click("back_icon.png")
        time.sleep(1)
        wait_and_click("back_button.png")  # большая кнопка 'Назад'
        time.sleep(1)
        wait_and_click("home_icon.png")
    else:
        print("✅ Окно 'Охота' не появилось — продолжаем...")

    # === Шаг 2. Проверка на другие возможные окна (пока заготовка) ===

    # === Шаг 2. Проверка окна "Не напоминать больше сегодня" (1-я версия)
    if_found_then_click("ne_napominat_segodnya.png", 905, 915)
    time.sleep(1)
    pyautogui.click(997, 564)  # Клик по экрану
    
    # === Шаг 3. Проверка другого варианта окна (например, на другом экране)
    if_found_then_click("ne_napominat_segodnya_alt.png", 905, 915)
    time.sleep(1)
    pyautogui.click(997, 564)  # Клик по экрану
    
    # === Шаг 4. Проверка окна "Уведомление"
    if_found_then_click("close_popup.png", 1191, 200)


    # === Шаг 5. Закрытие окна "Оффлайн-доход" ===
    def check_additional_window_4():
        if wait_and_click("close_btn.png", timeout=5):
            print("💰 Проверка на окно 'Оффлайн-доход'")
        else:
            print("Окно 'Оффлайн-доход' не появилось")
    check_additional_window_4()



    # === Далее идут основные ежедневные действия ===

    # 1. Временные награды
    print("🎁 Сбор временных наград")
    if wait_and_click("reward_temp.png"):
        time.sleep(2)
        wait_and_click("reward_temp2.png")
        time.sleep(1)
        wait_and_click("reward_collect_all.png")
        time.sleep(1)
        wait_and_click("close_popup.png")
        time.sleep(1)
        wait_and_click("back_icon.png")
    else:
        wait_and_click("back_icon.png")

    # 2. Привилегии
    print("🎁 Сбор привилегий")
    if wait_and_click("reward_privilege.png"):
        time.sleep(2)
        wait_and_click("priv_mark.png")
        time.sleep(1)
        wait_and_click("priv_checkin.png")
        time.sleep(1)
        wait_and_click("back_icon.png")




    # 3. Рейтинг
    print("🎖 Рейтинг")
    if wait_and_click("reward_rank.png"):
        time.sleep(2)
        wait_and_click("rank_server_entry.png")
        time.sleep(2)
        wait_and_click("respect_all.png")
        for _ in range(5):
            pyautogui.click(997, 564)  # Клик по экрану
            time.sleep(1)
        wait_and_click("back_icon.png")
        time.sleep(1)
        
        wait_and_click("total_rank.png")
        wait_and_click("respect_all.png")
        for _ in range(2):
            pyautogui.click(997, 564)  # Клик по экрану
            time.sleep(1)
        for _ in range(2):
            wait_and_click("back_icon.png", timeout=1)

    # 4. Питомец
    print("Питомец")
    if wait_and_click("close.png"):
        time.sleep(2)
        wait_and_click("magasin.png")
        wait_and_click("10.png")
        wait_and_click("10.png")
        wait_and_click("10.png")
        wait_and_click("buy.png")
        wait_and_click("magasin.png")
        wait_and_click("tarelka.png")
        wait_and_click("max.png")
        wait_and_click("dobavit.png")
        wait_and_click("back_icon.png")
        


    

    # 5. Дворец
    print("🏛 Дворец")
    if wait_and_click("palace.png"):
        time.sleep(2)
        if wait_and_click("reward_hall.png"):
            wait_and_click("hall_greet.png")
            wait_and_click("back_icon.png")
        if wait_and_click("reward_dress.png"):
            wait_and_click("dress_open.png")
            wait_and_click("back_icon.png")
            wait_and_click("home_icon.png")

    # 6. Задания
    print("📜 Задания")
    if wait_and_click("tasks_button.png"):
        time.sleep(2)
        while wait_and_click("task_claim_button.png", timeout=3):
            time.sleep(1)
        while wait_and_click("task_reward_box.png", timeout=3):
            time.sleep(1)
        wait_and_click("back_icon.png")

    print(f"✅ Все ежедневные действия для ОСНОВЫ {main_name} завершены")
