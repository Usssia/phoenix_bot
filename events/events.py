# events.py — управление состоянием акций и рейтингов

# --- Банкетные функции временно отключены ---
# from events.banquet import run_banquet_create
# from events.banquet_event import run_banquet_event
# from actions.account_switch import switch_account
# from actions.game_enter import enter_game
# from actions.game_exit import exit_game

# TWINS = [
#     "usssia_S172", "usssia_S176",
#     "usssia1_S171", "usssia1_S172", "usssia1_S173",
#     "usssia2_S171", "usssia2_S172", "usssia2_S173", "usssia2_S175", "usssia2_S176"
# ]
# BANQUET_ID = "eu17400000169"

# def run_banquet_cycle(repeats=1):
#     for i in range(repeats):
#         print(f"\n=== Запуск банкета №{i+1} ===")
#         switch_account("usssiabat")
#         enter_game("usssia_main")
#         run_banquet_create("usssia_main")
#         exit_game("usssia_main")
#         for twin in TWINS:
#             switch_account(twin)
#             enter_game(twin)
#             run_banquet_event(twin, BANQUET_ID)
#             exit_game(twin)
#         print(f"=== Банкет №{i+1} завершён ===\n")

# BANQUET_RATING_ACTIVE = False
BANQUET_RATING_ACTIVE = False  # Банкетные функции отключены

# Здесь можно добавить другие флаги для будущих событий:
# SOME_EVENT_ACTIVE = False
# ANOTHER_EVENT_ACTIVE = True

# Используйте эти переменные в основном цикле для управления логикой бота 

# Список всех твинов, которые должны участвовать в банкете (без основы)
TWINS = [
    "usssia_S172", "usssia_S176",
    "usssia1_S171", "usssia1_S172", "usssia1_S173",
    "usssia2_S171", "usssia2_S172", "usssia2_S173", "usssia2_S175", "usssia2_S176"
]

# Фиксированный ID банкета (укажите свой)
BANQUET_ID = "eu17400000169"


def run_banquet_cycle(repeats=1):
    """
    Запускает цикл банкетов:
    1. Основой создаёт банкет (banquet.py)
    2. Все твинки по очереди заходят и выполняют banquet_event (banquet_event.py)
    3. Повторяет цикл нужное количество раз (repeats)
    """
    for i in range(repeats):
        print(f"\n=== Запуск банкета №{i+1} ===")
        # 1. Основой создаём банкет
        # switch_account("usssiabat")
        # enter_game("usssia_main")
        # run_banquet_create("usssia_main")
        # exit_game("usssia_main")

        # 2. Все твинки участвуют в банкете
        for twin in TWINS:
            # switch_account(twin)
            # enter_game(twin)
            # run_banquet_event(twin, BANQUET_ID)
            # exit_game(twin)
            pass
        print(f"=== Банкет №{i+1} завершён ===\n")

# Пример вызова:
# run_banquet_cycle(repeats=1) 