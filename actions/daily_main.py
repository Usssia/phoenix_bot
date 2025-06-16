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
    """
    print(f'📅 Выполнение всех ежедневных задач для ОСНОВЫ: {main_name}')

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
        for tab in ["history_tab.png", "intimacy_tab.png", "achieve_tab.png", "dress_tab.png"]:
            wait_and_click(tab)
            time.sleep(1)
            wait_and_click("respect_btn.png")
            wait_and_click("gold_get.png")
        wait_and_click("back_icon.png")
        time.sleep(1)
        wait_and_click("total_rank.png")
        wait_and_click("respect_btn.png")
        wait_and_click("gold_get.png")
        wait_and_click("guild_tab.png")
        wait_and_click("respect_btn.png")
        wait_and_click("gold_get.png")
        wait_and_click("back_icon.png")
        wait_and_click("back_icon.png")

    # 4. Обязанности
    print("📘 Обязанности")
    if wait_and_click("reward_duty.png"):
        time.sleep(2)
        wait_and_click("duty_skip.png")
        wait_and_click("duty_knowledge.png")
        wait_and_click("duty_silver.png")
        wait_and_click("duty_fame.png")
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
