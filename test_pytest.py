import pytest
from emp_cls import Employee
from validate import EmployeeValidator
from exceptions import NameIsNull, SalaryIsNull, SalaryNotInt, NameNotStr


@pytest.fixture()
def setup():
    name = 'akhil'
    sal = 20
    return Employee(name, sal)

def test_emp_obj_success(setup):
    assert isinstance(setup, Employee)

def test_emp_obj_fails(setup):
    emp_obj = setup
    assert not isinstance(emp_obj, EmployeeValidator)

def test_emp_validator_success(setup):
    assert True == EmployeeValidator.emp_validate(setup)

def test_emp_name_none():
    name = ''
    sal = 20
    emp_obj = Employee(name, sal)
    with pytest.raises(NameIsNull):
        EmployeeValidator.emp_validate(emp_obj)

def test_emp_name_str():
    name = 25
    sal = 30
    emp_obj = Employee(name, sal)
    with pytest.raises(NameNotStr):
        EmployeeValidator.emp_validate(emp_obj)

def test_emp_sal_none():
    name = 'abc'
    sal = ''
    emp_obj = Employee(name, sal)
    with pytest.raises(SalaryIsNull):
        EmployeeValidator.emp_validate(emp_obj)

def test_emp_sal_int():
    name = 'abc'
    sal = 'aaa'
    emp_obj = Employee(name, sal)
    with pytest.raises(SalaryNotInt):
        EmployeeValidator.emp_validate(emp_obj)





