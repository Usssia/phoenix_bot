import pyautogui
import time

def run_banquet_create(main_name):
    """
    Создаёт банкет для основы (главного аккаунта).
    main_name — имя основы (строка)
    Возвращает banquet_id (пока фиксированный, потом можно сделать получение с экрана).
    """
    print(f'[{main_name}] Создаю банкет...')

    def wait_and_click(image_name, timeout=10):
        print(f"Ожидаем: {image_name}")
        start = time.time()
        while True:
            location = pyautogui.locateCenterOnScreen(f"screenshots/{image_name}", confidence=0.8)
            if location:
                pyautogui.click(location)
                print(f"Нажато: {image_name}")
                return
            if time.time() - start > timeout:
                print(f"❌ Не найдена кнопка: {image_name}")
                return
            time.sleep(0.5)

    # Пример шагов для создания банкета (замените на реальные шаги)
    wait_and_click("1_pir_na_ves_mir.png")
    time.sleep(1)
    wait_and_click("create_banquet_button.png")  # пример, замените на реальное имя файла
    time.sleep(1)
    wait_and_click("confirm_create.png")         # пример, замените на реальное имя файла
    time.sleep(1)

    # Здесь можно добавить получение banquet_id с экрана (пока фиксированный)
    banquet_id = "eu17400000169"
    print(f"[{main_name}] Банкет создан, ID: {banquet_id}")
    return banquet_id 

#from events.events import run_banquet_cycle
#run_banquet_cycle(repeats=1)  # или любое нужное число повторов