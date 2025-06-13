import pyautogui
import time

# Удобная функция с ожиданием и кликом по центру картинки
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

# Переход по шагам
wait_and_click("1_pir_na_ves_mir.png")
time.sleep(1)

wait_and_click("2_pereyti.png")
time.sleep(1)

wait_and_click("3_posetit_banket.png")
time.sleep(1)

wait_and_click("4_vybrat_banket.png")
time.sleep(1)

# Вводим ID
wait_and_click("5_id_pole.png")
time.sleep(0.5)
pyautogui.write("eu17400000169")
time.sleep(0.5)

wait_and_click("6_iskat.png")
time.sleep(2)

wait_and_click("7_posetit.png")
time.sleep(1)

wait_and_click("8_posetit.png")
time.sleep(1)

wait_and_click("9_krasnye_konverty.png")
time.sleep(1)

wait_and_click("10_posetit.png")
time.sleep(1)

wait_and_click("11_podtverdit.png")
time.sleep(1)

print("�� Банкет завершён")