# config.py — конфигурация для автоматизации

# Список аккаунтов и их твинков (по порядку переключения)
ACCOUNT_IDS = [
    ["usssia_main", "usssia_S172", "usssia_S176"],                 # Аккаунт 1: основа и два твина
    ["usssia1_S171", "usssia1_S172", "usssia1_S173"],            # Аккаунт 2: три твина
    ["usssia2_S171", "usssia2_S172", "usssia2_S173", "usssia2_S175", "usssia2_S176"], # Аккаунт 3: пять твинов
]

# Имена аккаунтов (по порядку)
ACCOUNT_NAMES = [
    "usssiabat",   # для группы 1
    "usssia1",     # для группы 2
    "usssia2"      # для группы 3
]

# Соответствие твинка и сервера (имя твинка: имя файла картинки сервера)
SERVER_MAP = {
    "usssia_main": "server174.png",
    "usssia_S172": "server172.png",
    "usssia_S176": "server176.png",
    "usssia1_S171": "server171.png",
    "usssia1_S172": "server172.png",
    "usssia1_S173": "server173.png",
    "usssia2_S171": "server171.png",
    "usssia2_S172": "server172.png",
    "usssia2_S173": "server173.png",
    "usssia2_S175": "server175.png",
    "usssia2_S176": "server176.png",
}

# Здесь можно добавить другие параметры (пути, тайминги и т.д.) 

import os

TEMPLATES_PATH = os.path.abspath("screenshots") 