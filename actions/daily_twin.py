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
        location = pyautogui.locateCenterOnScreen(f"assets/screenshots/{image_name}", confidence=confidence)
        if location:
            pyautogui.click(location)
            print(f"✅ Клик: {image_name}")
            return True
        time.sleep(0.5)
    print(f"❌ Не найдено: {image_name}")
    return False

def claim_temporary_rewards():
    """Сбор временных наград"""
    print("🎁 Сбор временных наград")
    if not wait_and_click("reward_temp.png"): return
    time.sleep(2)
    if wait_and_click("reward_temp2.png"):
        time.sleep(1)
        wait_and_click("reward_collect_all.png")
        time.sleep(1)
        wait_and_click("close_popup.png")
        time.sleep(1)
        wait_and_click("back_icon.png")
    else:
        wait_and_click("back_icon.png")
    print("✅ Временные награды собраны")

def claim_privileges():
    """Сбор привилегий (отметка)"""
    print("🎁 Сбор привилегий")
    if not wait_and_click("reward_privilege.png"): return
    time.sleep(2)
    if wait_and_click("priv_mark.png"):
        time.sleep(1)
        wait_and_click("priv_checkin.png")
        time.sleep(1)
    wait_and_click("back_icon.png")
    print("✅ Привилегии собраны")

def claim_rank_rewards():
    """Посещение рейтинга: почтить + забрать награды"""
    print("🎖 Рейтинг")
    if not wait_and_click("reward_rank.png"): return
    time.sleep(2)
    if not wait_and_click("rank_server_entry.png"): return
    time.sleep(2)
    tabs = [None, "history_tab.png", "intimacy_tab.png", "achieve_tab.png", "dress_tab.png"]
    for tab in tabs:
        if tab:
            wait_and_click(tab)
            time.sleep(1)
        wait_and_click("respect_btn.png")
        time.sleep(1)
        wait_and_click("gold_get.png")
        time.sleep(1)
    wait_and_click("back_icon.png")
    time.sleep(1)
    wait_and_click("total_rank.png")
    time.sleep(1)
    wait_and_click("respect_btn.png")
    time.sleep(1)
    wait_and_click("gold_get.png")
    time.sleep(1)
    wait_and_click("guild_tab.png")
    time.sleep(1)
    wait_and_click("respect_btn.png")
    time.sleep(1)
    wait_and_click("gold_get.png")
    time.sleep(1)
    wait_and_click("back_icon.png")
    time.sleep(1)
    wait_and_click("back_icon.png")
    print("✅ Рейтинг завершён")

def claim_duties():
    """Обязанности: пропустить + забрать награды"""
    print("📘 Обязанности")
    if not wait_and_click("reward_duty.png"): return
    time.sleep(2)
    wait_and_click("duty_skip.png")
    time.sleep(1)
    wait_and_click("duty_knowledge.png")
    time.sleep(1)
    wait_and_click("duty_silver.png")
    time.sleep(1)
    wait_and_click("duty_fame.png")
    time.sleep(1)
    wait_and_click("back_icon.png")
    print("✅ Обязанности завершены")

def claim_palace_rewards():
    """Дворец: зал славы и бюро одежды"""
    print("🏛 Дворец")
    if not wait_and_click("palace.png"): return
    time.sleep(2)
    if wait_and_click("reward_hall.png"):
        time.sleep(1)
        wait_and_click("hall_greet.png")
        time.sleep(1)
        wait_and_click("back_icon.png")
        time.sleep(1)
    if wait_and_click("reward_dress.png"):
        time.sleep(1)
        wait_and_click("dress_open.png")
        time.sleep(1)
        wait_and_click("back_icon.png")
        time.sleep(1)
        wait_and_click("home_icon.png")
    print("✅ Дворец завершён")

def claim_tasks():
    """Задания: получить награды и сундуки"""
    print("📜 Задания")
    if not wait_and_click("tasks_button.png"): return
    time.sleep(2)
    while wait_and_click("task_claim_button.png", timeout=3):
        time.sleep(1)
    while wait_and_click("task_reward_box.png", timeout=3):
        time.sleep(1)
    wait_and_click("back_icon.png")
    print("✅ Задания завершены")

def run_daily_twin_actions(twin_name):
    """
    Запуск полного набора ежедневных задач для твинка.
    twin_name — имя твинка (строка)
    """
    print(f"📅 Выполнение всех ежедневных задач для: {twin_name}")
    claim_temporary_rewards()
    claim_privileges()
    claim_rank_rewards()
    claim_duties()
    claim_palace_rewards()
    claim_tasks()
    print(f"✅ Все ежедневные действия для {twin_name} завершены")

