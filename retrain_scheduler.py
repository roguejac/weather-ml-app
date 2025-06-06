import schedule
import time
from ml_model import train_model

def job():
    print("Retraining model...")
    train_model()

schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)