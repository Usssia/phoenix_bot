import os
import time

def stop_ldplayer():
    """
    Завершает процесс LDPlayer (эмулятора).
    """
    print("Завершаю LDPlayer...")
    os.system('taskkill /IM dnplayer.exe /F')
    print("LDPlayer завершён.")

def shutdown_computer():
    """
    Выключает компьютер (опционально).
    """
    print("Выключаю компьютер...")
    os.system('shutdown /s /t 5') 