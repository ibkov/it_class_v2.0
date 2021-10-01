from .models import Tasks
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import requests


def send_telegram(text: str, channel_id):
    token = "1098094286:AAGmN7YpguBfJOiPgXLyx-OtPW15pQ76ESU"
    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")


def check_tasks():
    active_task = Tasks.objects.all()
    for i in active_task:
        if i.date == dt.datetime.now().date():
            if i.status_task == "ST10":
                send_telegram("Доступна новая задача дня.", -584490192)
            elif i.status_task == "ST11":
                send_telegram("Доступна новая задача дня.", -1001491502255)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_tasks, 'cron', hour='10', minute='00')
    scheduler.start()
