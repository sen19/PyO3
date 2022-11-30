from employees.empl_exceptions import EmailAlreadyExistsException


class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email
        self.validate()
        self.save_email()  # -> write email to file

    def save_email(self):
        """Open file in append mode a+. Write email."""
        with open('email.txt','a+') as r:
            r.write(f'{self.email}'+'\n')

    def validate(self):
        """
        1. Read the file with emails.
        2. Check that self.email in file.
        3. If not: do nothing
        4. Else: raise EmailAlreadyExistsException
        :return:
        """
        with open('email.txt') as r:
            for i in r:
                if i == f'{self.email}'+'\n':
                    raise EmailAlreadyExistsException
            else:
                pass




