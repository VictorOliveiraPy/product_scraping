import subprocess
from datetime import datetime, timedelta

import pytz
import schedule
import time

from apscheduler.schedulers.background import BackgroundScheduler

sp_timezone = pytz.timezone('America/Sao_Paulo')
next_run = timedelta(hours=24).total_seconds()


def run_crawl():
    subprocess.call(["scrapy", "crawl", "open_food"], bufsize=0)


scheduler = BackgroundScheduler()
scheduler.add_job(run_crawl, 'interval', seconds=next_run)


if __name__ == "__main__":
    run_crawl()
    scheduler.start()

    while True:
        time.sleep(60)
