from exceptions import NameIsNull, SalaryIsNull, SalaryNotInt, NameNotStr
from abc import ABC, abstractmethod


class ValidateAbc(ABC):
    @abstractmethod
    def emp_validate(self):
        pass

class EmployeeValidator(ValidateAbc):

    def emp_validate(emp):
        if not emp.name:
            raise NameIsNull('NameIsNull')
        elif type(emp.name) != str:
            raise NameNotStr('NameNotString')
        elif not emp.sal:
            raise SalaryIsNull('SalaryIsNull')
        elif type(emp.sal) != int:
            raise SalaryNotInt('SalaryNotInt')
        else:
            return True







        # try:
        #     if emp.name == '':
        #         raise NameIsNull('NameIsNull')
        #     elif not emp.sal:
        #         raise SalaryIsNull('SalaryIsNull')
        #     elif type(emp.sal) != int:
        #         raise SalaryNotInt('SalaryNotInt')
        #     else:
        #         return True
        # except NameIsNull as e:
        #     return print('\n', e)
        # except SalaryIsNull as e:
        #     return print('\n', e)
        # except SalaryNotInt as e:
        #     return print('\n', e)

