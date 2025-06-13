import os
import time
import pyautogui
from config import TEMPLATES_PATH

def wait_and_click(image_name, timeout=15, confidence=0.7):
    """
    Функция ждёт появления изображения на экране и кликает по нему.
    
    Параметры:
    image_name - имя файла изображения (например, "ok_button.png")
    timeout - сколько секунд ждать появления изображения
    confidence - точность совпадения (от 0 до 1, где 1 - точное совпадение)
    """
    print(f"🔍 Ищем на экране: {image_name}")
    
    # Запоминаем время начала поиска
    start_time = time.time()
    
    # Полный путь к файлу изображения
    image_path = os.path.join(TEMPLATES_PATH, image_name)
    
    # Продолжаем поиск, пока не истечёт время ожидания
    while time.time() - start_time < timeout:
        try:
            # Ищем изображение на экране
            # locateCenterOnScreen возвращает координаты центра найденного изображения
            image_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            
            # Если изображение найдено
            if image_location:
                # Кликаем по найденным координатам
                pyautogui.click(image_location)
                print(f"✅ Нашли и кликнули по: {image_name}")
                return True
                
        except Exception as error:
            print(f"⚠️ Ошибка при поиске изображения: {error}")
            
        # Ждём полсекунды перед следующей попыткой
        time.sleep(0.5)
    
    # Если изображение не найдено за отведённое время
    print(f"❌ Не удалось найти: {image_name}")
    return False

def start_ldplayer(ldplayer_path=r"C:\LDPlayer\LDPlayer9\dnplayer.exe", wait_time=15):
    """
    Функция запускает LDPlayer и ждёт его загрузки.
    
    Параметры:
    ldplayer_path - путь к файлу LDPlayer
    wait_time - сколько секунд ждать после запуска
    
    Возвращает:
    True - если LDPlayer успешно запущен
    False - если произошла ошибка
    """
    try:
        # Проверяем, существует ли файл LDPlayer
        if not os.path.exists(ldplayer_path):
            print(f"❌ Ошибка: файл {ldplayer_path} не найден")
            return False
        
        # Запускаем LDPlayer
        print(f"🚀 Запускаем LDPlayer: {ldplayer_path}")
        os.startfile(ldplayer_path)
        
        # Ждём, пока LDPlayer запустится
        print(f"⏳ Ждём {wait_time} секунд для загрузки...")
        time.sleep(wait_time)
        
        # Проверяем, появилось ли окно с кнопкой "Ясно"
        print("🔍 Проверяем, есть ли окно с кнопкой 'Ясно'...")
        try:
            # Ищем кнопку "Ясно" в течение 20 секунд
            if wait_and_click("ok_button.png", timeout=20):
                print("✅ Нашли и нажали кнопку 'Ясно'")
                # Ждём 2 секунды после нажатия
                time.sleep(2)
        except:
            # Если кнопка не появилась - это нормально, продолжаем работу
            print("ℹ️ Окно с кнопкой 'Ясно' не появилось, продолжаем...")
        
        print("✅ LDPlayer успешно запущен")
        return True
        
    except Exception as error:
        # Обрабатываем любые другие ошибки
        print(f"❌ Ошибка при запуске LDPlayer: {error}")
        return False
