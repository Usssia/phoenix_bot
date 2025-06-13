# bot.py — основной управляющий класс бота

from config import ACCOUNT_IDS
from actions.daily_twin import run_daily_twin_actions
from actions.daily_main import run_daily_main_actions
from actions.account_switch import switch_account
from actions.game_enter import enter_game
from actions.game_exit import exit_game
#from events.banquet_event import run_banquet_event
from events.events import BANQUET_RATING_ACTIVE
from actions.ldplayer_start import start_ldplayer
import os
import sys
import time

TEMPLATES_PATH = os.path.abspath("screenshots")

class Bot:
    def run(self):
        try:
            print('Бот запущен!')
            start_ldplayer()  # LDPlayer теперь запускается перед всеми действиями
            # Перебираем все аккаунты и их твинов
            for group in ACCOUNT_IDS:
                for twin in group:
                    try:
                        # Переключаемся на нужный аккаунт
                        switch_account(twin)
                        # Входим в игру
                        enter_game(twin)

                        # Если это основа — выполняем расширенные действия
                        if twin == "usssia_main":
                            run_daily_main_actions(twin)
                            # Банкет для основы только если рейтинг НЕ активен
                            # if not BANQUET_RATING_ACTIVE:
                            #     run_banquet_event(twin)
                        else:
                            # Для твинов — обычные действия
                            run_daily_twin_actions(twin)
                            # Банкет для твинов только если рейтинг активен
                            # if BANQUET_RATING_ACTIVE:
                            #     run_banquet_event(twin)

                        # Выходим из игры
                        exit_game(twin)
                    except Exception as e:
                        print(f"❌ Ошибка при обработке аккаунта {twin}: {e}")
                        print("Пропускаем этот аккаунт и продолжаем...")
                        time.sleep(5)
                        continue
            print('✅ Бот успешно завершил работу!')
        except KeyboardInterrupt:
            print("\n⚠️ Бот остановлен пользователем!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Критическая ошибка: {e}")
            print("Бот остановлен из-за ошибки!")
            sys.exit(1) 