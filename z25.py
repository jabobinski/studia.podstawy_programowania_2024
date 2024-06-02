class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)


employees_data = [
    ("ADAMS", "E7876", 50000, "ACCOUNTING"),
    ("JONES", "E7499", 45000, "RESEARCH"),
    ("MARTIN", "E7900", 50000, "SALES"),
    ("SMITH", "E7698", 55000, "OPERATIONS")
]

employees = [Employee(*data) for data in employees_data]

employees[0].assign_department("HR")

hours_worked = 55
print("Salary with overtime for {}: ${}".format(employees[0].emp_name,
                                                employees[0].calculate_emp_salary(hours_worked)))

for employee in employees:
    print("\nEmployee Details:")
    employee.print_employee_details()