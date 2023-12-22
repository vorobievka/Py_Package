from application import salary
from application.db import people
from datetime import datetime
import requests


if __name__ == '__main__':
    dt = datetime.today()
    response = requests.get('https://api.github.com')

    print(salary.calculate_salary())

    people.get_employees()

    print(f"Today: {dt.day}-{dt.month}-{dt.year}")
    print(f"Time: {dt.hour}:{dt.minute}:{dt.second}")

    print("Test availability api.github: ", response)
