import traceback

from employees.empl_exceptions import EmailAlreadyExistsException
from employees.employee import Employee

import datetime

def main():
    emp1 = Employee('John','1000','john@gmail.com')


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        with open('logs.txt', 'a+') as fp:
            fp.write(traceback.format_exc() + '\n')
        raise f'{datetime.date.today()}{datetime.datetime.now().hour}:' \
              f'{datetime.datetime.now().minute} {traceback.format_exc}'




    # write traceback to the logs txt
    # 1. with open...
    # 2. message = f"{datetime.date.today()}
    # {datetime.datetime.now().hour}:
    # {datetime.datetime.now().minute} {traceback.format_exc}"
    # 3. log a message in the file
    # 3*. implement with logging https://docs.python.org/3/library/logging.html
