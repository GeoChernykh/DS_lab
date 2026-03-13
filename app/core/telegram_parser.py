import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
import pandas as pd

load_dotenv()


api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('API_HASH')

channels = ["kievreal1", "ps_zsu","air_alert_ua", "war_monitor"]

data = []

from datetime import datetime, timezone

start_date = datetime(2022, 2, 24, tzinfo=timezone.utc)

with TelegramClient("session", api_id, api_hash) as client:
    for channel in channels:
        print(f'парсинг каналу: {channel}')
        count = 0

        for msg in client.iter_messages(channel):
            if msg.date < start_date:
                break

            data.append({
                "id": msg.id,
                "date": msg.date,
                "text": msg.text,
            })
            count += 1
            if count % 500 == 0:
                print(f"Зібрано {count} повідомлень з каналу {channel}")
        print(f"Завершенний парсинг каналу {channel}")


df = pd.DataFrame(data)
df = df.sort_values(by="date")
df.to_csv("telegram_data.csv", index=False)
print("\nУспішно збережено, Загальна кількість рядків:", len(df))

