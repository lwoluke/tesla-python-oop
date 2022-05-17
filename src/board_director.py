# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:35:22 2022

Contains the essential information needed to 
    identify and represent a company board director.

@author: lwolu
"""

# Python file(s)
from person import Person
from employee import Employee


class BoardDirector(Employee, Person):
    
    total_directors = 9
    """
    total_directors (int): (class attribute) Tesla's current total 
        number board directors.
    """
    
    def __init__(self, name='FirstName LastName', age='XX', 
                 address='Default Address', phone='XXX-XXX-XXXX', 
                 title="Director", salary="XXX,XXX", 
                 office_address="1 Tesla Road", office_phone=3239891010,
                 share_of_company=0):
        """
        Initializes an instance object of the BoardDirector class. Uses 
            the Employee class as an initializer for the name, 
            age, address, phone, title, salary, office_address, 
            and office_phone parameters.
            
        The total number of board directors increases by one each time 
            a new BoardDirector object is created.

        Args:
            name (str, optional): The name of the board director. Defaults 
                to 'FirstName LastName'.
            age (int, optional): How old the board director is. Defaults 
                to 'XX'.
            address (str, optional): Where the employee lives. Defaults 
                to 'Default Address'.
            phone (int, optional): What the phone number of the board director 
                is. Defaults to 'XXX-XXX-XXXX'.
            title (str, optional): The job title for the board director. 
                Defaults to "Director".
            salary (int, optional): How much money the board director makes 
                per year. Defaults to "XXX,XXX".
            office_address (str, optional): Where the board director's 
                office is located. Defaults to "1 Tesla Road".
            office_phone (int, optional): What the board director's office 
                phone number is. Converted from an int value 
                to proper phone number format after object creation. 
                Defaults to 3239891010.
            share_of_company (int, optional): The board director's share 
                of the company. Defaults to 0.

        """
        super().__init__(name='FirstName LastName', age='XX', 
                     address='Default Address', phone='XXX-XXX-XXXX',
                     title="Director", salary="XXX,XXX",
                     office_address="1 Tesla Road", 
                     office_phone='323-999-6789')
        
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
            self._title = 'Director'
        else:
            self._title = title 
            
        if salary == None: 
            self._salary = "XXX,XXX"
        else:
            self._salary = salary
            
        if office_phone == None:
            self._office_phone = '323-999-6789'
        elif type(office_phone) == int:
            office_phone = str(office_phone)
            self._office_phone = format(int(office_phone[:-1]), ",").replace(",", "-") \
                + office_phone[-1]
        else:
            self._office_phone = office_phone

        if office_address == None:
            self._office_address = "1 Tesla Road"
        else:
            self._office_address = office_address

        if share_of_company == None:
            self._share_of_company = 0
        else:
            self._share_of_company = share_of_company

        BoardDirector.total_directors += 1
        
    @classmethod 
    def get_details(cls):
        """
        Returns the class attribute for the BoardDirector class.
        
        Overrides the get_details method of the Employee class.
        """
        return ("Class Data)\n" + 
                "Number of Board Directors at Tesla: " + 
                str(format(cls.total_directors,",")))
    
    # Overrides Person class method 
    def greet(self):
        """
        Returns an introduction message for a BoardDirector object 
            using its name, title, and share_of_company instance 
            attributes. 
        
        Overrides the greet method of the Employee class.

        """
        return(f"Hello, my name is {self.name}. " +
               f"My title is {self.title} and I have " +
               f"a {self.share_of_company}% share of the company")
    
    def __str__(self):
        """
        Allows the BoardDirector object to be returned from the print 
            function. The salary is converted to proper numerical 
            format before being returned.
         
        Inherits the Employee class magic method to print the 
           name, age, address, phone, and salary instance attributes.
        
        Returns:
            string (str): The name, age, address, phone, salary,
                title, and share of company of the board director 
                specified.

        """
        string = super().__str__()
        
        string += ("\nTitle: " + self.title + "\n")
        string += ("Share of Company: " + str(self.share_of_company) + "%")
        
        return string
    
    @property 
    def share_of_company(self):
        """
        Returns the share of the company for the specified board director.
        """
        return self._share_of_company
    
    def __del__(self):
        """
        Allows the BoardDirector object to be deleted from the del statement.
        """
        print(f'Destructor called. BoardDirectors object {self.name} has been deleted')
    

def main():
    print("***BoardDirector class testing***\n")
    
    print(BoardDirector.get_details())
    
    
    count = 1
    print("\n---------------------------------")
    print(f"Create BoardDirector object #{count}:")
    
    print("Only provide share of company argument since property is immutable)")
    b1 = BoardDirector(None,None,None,None,None,None,None,None,22)
    
    print("Print share of company: ", end="")
    print(str(b1.share_of_company) + "%")
    print("Greeting method should be default except for share of company)")
    print("Greeting: ", end="")
    print(b1.greet())
    
    print("After updating all arguments)")
    
    b1.name = "Elon Musk"
    b1.age = 50
    b1.address = "1 Space World"
    b1.phone = 19385827389
    b1.title = "Founder"
    b1.salary = 999999999
    b1.office_address = "1 Tesla Road"
    b1.office_phone = 3239891010
    
    print("Greeting: ", end="")
    print(b1.greet())
    print("Had birthday, should be one year older")
    b1.birthday()
    print("Greeting: ", end="")
    print(b1.greet())
    print("Is person at retirement age, meaning >= 60 years old? ", end="")
    print(b1.at_retirement_age())
    print(f"What share of the company does {b1.name} own? ", end="")
    print(str(b1.share_of_company) + "%")
   
    
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate BoardDirector object #{count}:")
    
    b2 = BoardDirector("Larry Ellison", 77, "777 Oracle Lane", 
                       7773339999, "Director", 77755581,
                       "1 Oracle Lane", 7779891010, 1.5)
    
    print("Greeting: ", end="")
    print(b2.greet())
    print("Change title from Director to Oracle)")
    
    b2.title = "Oracle"
    
    print(b2.greet())
    print("Is person at retirement age, meaning >= 60 years old? ", end="")
    print(b2.at_retirement_age())
    print(f"What share of the company does {b2.name} own? ", end="")
    print(str(b2.share_of_company) + "%")
    
    
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate BoardDirector object #{count}:")
    
    print("Provide all arguments in object creation)")
    
    b3 = BoardDirector("Kathleen Wilson-Thompson", 63, "66 Great Lake Blvd",
                       6636646666, "Founder", 97755558, 
                       "1 Tesla Road", 7777891031, 0.55)
    
    print("Print object)")
    print(b3)
    print("Contact Information:")
    
    print(b3.contact_details())
    
    print("Updated Contact Information:")
    
    b3.address = "68 Litte Pond Avenue"
    b3.phone = 1014449959
    
    print(b3.contact_details())
    print(f"What share of the company does {b3.name} own? ", end="")
    print(str(b3.share_of_company) + "%")
    
    print("\n---------------------------------\n")
    
    print(BoardDirector.get_details())
    
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    del(b1)
    del(b2)
    del(b3)
    

if __name__ == '__main__':
    main()
