from employee import Employee
def main():
    employee1 = Employee('Avi','Engineering')
    print("Employee's name: {}".format(employee1.name))
    print("Employee's department: {}".format(employee1.department))
    employee1.name = input("Enter a new employee name. ")
    employee1.department = input("Enter a new department. ")
    print("My new name is: {}.".format(employee1.name))
    print("My new department is: {}.".format(employee1.department))
if __name__ == "__main__":
    main()