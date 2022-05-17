# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:36:38 2022

Contains the essential information needed to 
    identify and represent a Tesla employee.

@author: lwolu
"""

# Python file(s)
from person import Person


class Employee(Person):
    
    total_employees = 70757
    """
    total_employees (int): (class attribute) Tesla's current total 
        number of employees.
    """
    
    def __init__(self, name='FirstName LastName', age='XX', 
                 address='Default Address', phone='XXX-XXX-XXXX', 
                 title="Default Title", salary="XXX,XXX", 
                 office_address="1 Tesla Road", 
                 office_phone='323-989-1010'):
        """
        Initializes an instance object of the Employee class. Uses 
            the Person class as an initializer for the 
            name, age, address, and phone parameters.
            
        The total number of employees increases by one each time 
            a new employee object is created.

        Args:
            name (str, optional): The name of the employee. Defaults 
                to 'FirstName LastName'.
            age (int, optional): How old the employee is. Defaults to 'XX'.
            address (str, optional): Where the employee lives. Defaults 
                to 'Default Address'.
            phone (int, optional): What the phone number of the employee 
                is. Defaults to 'XXX-XXX-XXXX'.
            title (str, optional): The job title for the employee. 
                Defaults to "Default Title".
            salary (int, optional): How much money the employee makes 
                per year. Defaults to "XXX,XXX".
            office_address (str, optional): Where the employee's 
                office is located. Defaults to "1 Tesla Road".
            office_phone (int, optional): What the employee's office 
                phone number is. Converted from an int value 
                to proper phone number format after object creation. 
                Defaults to 3239891010.

        """
        super().__init__(name='FirstName LastName', age='XX', 
                     address='Default Address', phone='XXX-XXX-XXXX')

        if name == None:
            self._name = 'FirstName LastName'
        else:
            self._name = name
            
        if age == None:
            self._age = 'XX'
        else:
            self._age = age
            
        if address == None: 
            self._address = 'Default Address'
        else:
            self._address = address 
        
        if phone == None:
            self._phone = 'XXX-XXX-XXXX'
        else:
            self._phone = phone      

        if title == None:
            self._title = "Default Title"
        else:
            self._title = title
            
        if salary == None:
            self._salary = "$XXX,XXX"
        else:
            self._salary = salary  
            
        if office_address == None:
            self._office_address = "1 Tesla Road"
        else:
            self._office_address = office_address  
        
        if office_phone == None:
            self._office_phone = '323-989-1010'
        else:
            self._office_phone = office_phone
             
        Employee.total_employees += 1
     
    @classmethod 
    def get_details(cls):
        """
        Returns the class attribute for the Employee class.
        """
        return ("Class Data)\n" + 
                "Number of Employees at Tesla: " + 
                str(format(cls.total_employees,",")))
     
    def greet(self):
        """
        Returns an introduction message for an Employee object using its 
            name and title instance attributes. 
        
        Overrides the greet method of the Person class.

        """
        return f"Hello, my name is {self.name}. My title is {self.title}."
     
    def federal_income_tax(self):
        """
        Returns the calculated federal income tax according to the 
            employee's salary.
            
        Int value result is converted to proper numerical format 
            when returned.
        """
        tax_rate = 0
        if self.salary <= 9950:
            tax_rate = .10
            tax_amt = self.salary * tax_rate
        
        elif 9951 <= self.salary <= 40525:
            tax_rate = .12
            tax_amt = ((self.salary - 9950) * tax_rate) + 995
            
        elif 40526 <= self.salary <= 86375:
            tax_rate = .22
            tax_amt = ((self.salary - 40525) * tax_rate) + 4664
            
        elif 86376 <= self.salary <= 164925:
            tax_rate = .24
            tax_amt = ((self.salary - 86375) * tax_rate) + 14751
            
        elif 164926 <= self.salary <= 209425:
            tax_rate = .32
            tax_amt = ((self.salary - 164925) * tax_rate) + 33603
            
        elif 209426 <= self.salary <= 523600:
            tax_rate = .35
            tax_amt = ((self.salary - 209425) * tax_rate) + 47843
            
        else:
            tax_rate = .37
            tax_amt = ((self.salary - 523600) * tax_rate) + 157804.25
            
            
        return '${:,.2f}'.format(tax_amt)
        
        
    def contact_details(self):
        """
        Returns the contact information of the specified employee.
        
        Overrides the contact_details method of the Person class.
        """
        return (f"Address - {self._office_address}, "
                f"Phone - {self.office_phone}")
    
    def get_raise(self, raise_amt):
        """
        Updates the employee's salary by specified dollar amount.
        """
        self._salary += raise_amt
        return self._salary 
        
    def convert_salary(self):
        """
        Returns the salary of the specified Employee object in 
            proper currency format.
            
        """
        if type(self._salary) == int:
            result = '${:,.2f}'.format(self._salary)
        else:
            result = self._salary
            
        return result
    
    def __str__(self):
        """
        Allows the Employee object to be returned from the print 
            function. The salary is converted to proper numerical 
            format before being returned.
         
        Inherits the Person class magic method to print the 
           name, age, address, and phone instance attributes.
        
        Returns:
            string (str): The name, age, address, phone, and salary 
                of the employee specified.

        """
        string = super().__str__()
        
        salary_amt = self.convert_salary()
        
        string += ("\nSalary: " + str(salary_amt))  
        
        return string
    
    def __del__(self):
        """
        Allows the Employee object to be deleted from the del statement.
        """
        print('Destructor called. Employee object has been deleted')
        
    @property 
    def title(self):
        """
        Returns the title of the specified employee.
        """
        return self._title
    
    @title.setter
    def title(self, new_title):
        """
        Updates the title of the specified employee.
        """
        self._title = new_title
        
    @property 
    def salary(self):
        """
        Returns the salary of the specified employee.
        """
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        """
        Updates the salary of the specified employee.
        """
        self._salary = new_salary
        
    @property 
    def office_address(self):
        """
        Returns the office address of the specified employee.
        """
        return self._office_address
    
    @office_address.setter
    def office_address(self, new_address):
        """
        Updates the office address of the specified employee.
        """
        self._office_address = new_address
    
    @property 
    def office_phone(self): 
        """
        Returns the office phone number in proper formatting for 
            the specified employee.
        """
        if type(self._office_phone) == int:
            self._office_phone = str(self._office_phone)
            return format(int(self._office_phone[:-1]), ",").replace(",", "-") \
                + self._office_phone[-1]
        else:
            return self._office_phone
    
    @office_phone.setter 
    def office_phone(self, new_number):
        """
        Updates the office phone number of the specified employee.
        """
        if type(new_number) == int:
            new_number = str(new_number)
            self._office_phone = format(int(new_number[:-1]), ",").replace(",", "-") \
                + new_number[-1]
        else:
            self._office_phone = new_number
        
        
def main():
    print("***Employee class testing***\n")
    
    print(Employee.get_details())
    
    count = 1
    print("\n---------------------------------")
    print(f"\nCreate Employee object #{count}:")
    
    print("Without providing arguments)")
    print("Greeting: ", end="")
    e1 = Employee()
    print(e1.greet())
    print("After updating all arguments)")
    
    e1.name = "Rian Ollor"
    e1.age = 22
    e1.address = "93 SpaceX Road"
    e1.phone = 1887774949
    e1.title = "Software Engineer"
    e1.salary = 250000 
    e1.office_address = "1 Tesla Road"
    e1.office_phone = 3239891010
    
    print("Greeting: ", end="")
    print(e1.greet())
    print("Change name to Brian Rodriguez")
    e1.name = "Brian Rodriguez"
    print("Greeting: ", end="")
    print(e1.greet())
    print("What is this employee's salary? ", end="")
    print(e1.convert_salary())
    print("After getting $15000.25 raise: ", end="")
    e1.get_raise(15000.25)
    print(e1.convert_salary())
   
   
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate Employee object #{count}:")
    print("Without providing arguments)")
    print("Print object)")
    e2 = Employee() 
    print(e2)
    
    e2.name = "Amy Tulgo"
    e2.age = 31
    e2.address = "101 Dalmatians Road"
    e2.phone = 8383774949
    e2.title = "Electronics Mechanic"
    e2.salary = 65000 
    e2.office_address = "1 Tesla Road"
    
    print("After updating all arguments)")
    print("Print object)")
    print(e2)
    print("Get Contact Info:")
    print(e2.contact_details())
    print("Updated Office Phone Number:")
    e2.office_phone = 3458899182
    print(e2.contact_details())
    
    
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate Employee object #{count}:")
    
    e3 = Employee("Samantha Friedman", 22, "999 Journey Street", 3583774978, 
                  "AI Researcher", 1005000, "1 Tesla Road", 3239891010)
    
    print("Greeting: ", end="")
    print(e3.greet())
    print("See Contact Information:")
    print(e3.contact_details())
    print(f"How much does {e3.name} pay in federal income taxes? ", end="")
    print(e3.federal_income_tax())
    
    print("\n---------------------------------\n")
    
    print(Employee.get_details())
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    del(e1)
    del(e2)
    del(e3)
    

if __name__ == '__main__':
    main()
