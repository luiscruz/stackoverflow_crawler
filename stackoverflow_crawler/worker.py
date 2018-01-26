import os
import csv
import datetime
from time import sleep
import random

from crawler import get_results_count

def create_csv_row(keyword):
    count = get_results_count(keyword)
    timestamp = str(datetime.datetime.today())
    return "{},{},{}\n".format(timestamp, keyword, count)

if __name__ == "__main__":
    csv_filename = "results.csv"
    CSV_HEADER = [
        "timestamp",
        "keyword",
        "count",
    ]
    KEYWORDS = [
        "JUnit",
        "AndroidJunitRunner",
        "RoboElectric",
        "RoboSpock",
        "AndroidViewClient",
        "Appium",
        "Calabash",
        "Espresso",
        "Monkeyrunner",
        "PythonUIAutomator",
        "Robotium",
        "UIAutomator",
        "Project Quantum",
        "Qmetry",
        "Saucelabs",
        "Firebase",
        "Perfecto",
        "Bitbar",
        "Travis CI",
        "Circle CI",
        "AppVeyor",
        "CodeShip",
        "CodeFresh",
        "Wercker",
    ]
    if not os.path.isfile(csv_filename):
        with open(csv_filename, 'w') as csv_file:
            csv_file.write(",".join(CSV_HEADER)+"\n")
    with open(csv_filename, 'a') as csv_file:
        for keyword in KEYWORDS:
            csv_file.write(create_csv_row(keyword))
            sleep(random.uniform(2,5))
