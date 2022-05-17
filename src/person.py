# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:33:18 2022

Contains the essential information 
    needed to identify and represent a person.

@author: lwolu
"""


class Person:
    
    def __init__(self, name='FirstName LastName', age='XX', 
                 address='Default Address', phone='XXX-XXX-XXXX'):
        """
        Initializes an instance object of the Person class.

        Args:
            name (str, optional): The name of the person. Defaults to 
                'FirstName LastName'.
            age (int, optional): How old the person is. Defaults to 
                'XX'.
            address (str, optional): Where the person lives. Defaults 
                to 'Default Address'.
            phone (str, optional): What the phone number of the person is. 
                Defaults to 'XXX-XXX-XXXX'.

        """
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
        
    def greet(self):
        """
        Returns the name and age of the person specified.
        """
        return f'Hello, my name is {self.name}. I am {self.age} years old'
        
    def birthday(self):
        """
        The person specified becomes a year older.
        """
        self._age += 1
        
    def at_retirement_age(self):
        """
        Returns boolean based on the age is the person specified, 
            whether they are old enough to retire.
        """
        if type(self._age) == int and self._age >= 60:
            return True
        else:
            return False
    
    def contact_details(self):
        """
        Returns the contact details of the person specified.
        """
        return f"Address - {self._address}, Phone - {self._phone}"
        
    def __str__(self):
        """
        Allows the Person object to be returned from the print function.

        Returns:
            string (str): The name, age, address, and phone of the 
                person specified.

        """
        string = ""
        string += ('Name: ' + self.name + '\n')
        string += ('Age: ' + str(self.age) + '\n')
        string += ('Address: ' + self.address + '\n')
        string += ('Phone: ' + self.phone)
        return string
        
    def __del__(self):
        """
        Allows the Person object to be deleted from the del statement.
        """
        print(f'Destructor called. Person object {self.name} has ' 
              'been deleted')

    @property 
    def name(self):
        """
        Returns the name of the specified person.
        """
        return self._name 
    
    @name.setter 
    def name(self, new_name):
        """
        Updates the name of the specified person.
        """
        self._name = new_name 
        
    @property 
    def age(self):
        """
        Returns the age of the specified person.
        """
        return self._age 
    
    @age.setter 
    def age(self, new_age):
        """
        Updates the age of the specified person.
        """
        self._age = new_age 
        
    @property 
    def address(self):
        """
        Returns the address of the specified person.
        """
        return self._address 
    
    @address.setter 
    def address(self, new_address):
        """
        Updates the address of the specified person.
        """
        self._address = new_address
        
    @property 
    def phone(self):
        """
        Returns the default parameter phone string, or the phone 
            number of the specified person in proper formatting.
        """
        if type(self._phone) == int:
            self._phone = str(self._phone)
            return format(int(self._phone[:-1]), ",").replace(",", "-") \
                + self._phone[-1]
        else:
            return self._phone
        
    
    @phone.setter 
    def phone(self, new_number):
        """
        Updates the phone number of the specified person, by
            converting the int value representation into a
            proper phone number format.
        
        """
        if type(new_number) == int:
            new_number = str(new_number)
            self._phone = format(int(new_number[:-1]), ",").replace(",", "-") \
                + new_number[-1]
        else:
            self._phone = new_number
            
        
    
def main():
    """
    Tests the Person class.
    """
    print("***Person class testing***\n")
    
    
    count = 1
    print(f"Create person object #{count}:")
    print("Without providing arguments)")
    print("Greet method: ", end="")
    
    p1 = Person()
    print(p1.greet())
    
    print("After updating all arguments)")
    
    p1.name = "Bill Edmond"
    p1.age = 35 
    p1.address = "123 Sagamore Lane"
    p1.phone = 1234837198
    
    print("Greeting: ", end="")
    
    print(p1.greet())
    
    print("Had birthday, should be one year older")
    
    p1.birthday()
    
    print("Greeting: ", end="")
    
    print(p1.greet())
    
    print("Is person at retirement age, meaning >= 60 years old? ", end="")
    
    print(p1.at_retirement_age())
   
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate person object #{count}:")
    
    p2 = Person("Emma Smith", 29, "10 Main Street", 9381058384)
    
    print("Greeting: ", end="")
    
    print(p2.greet())
    
    print("Change age to 65 and name to Jennifer")
    
    p2.age = 65
    p2.name = "Jennifer Smith"
    
    print("Greeting: ", end="")
    
    print(p2.greet())
    
    print("Is person at retirement age, meaning >= 60 years old? ", end="")
    
    print(p2.at_retirement_age())
    
    
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate person object #{count}:")
    print("Without providing arguments)")
    print("Print object)")
    
    p3 = Person() 
    print(p3)
    
    print("After updating all arguments)")
    
    p3.name = "Carl Orson"
    p3.age = 19
    p3.address = "85 Silouette Road"
    p3.phone = 1928563817
    
    print("Greeting: ", end="")
    
    print(p3.greet())
    
    print("See Contact Information:")
    
    print(p3.contact_details())
    
    print("Updated Contact Information:")
    
    p3.address = "444 Delian Street"
    p3.phone = 3334449999
    print(p3.contact_details())
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    
    del(p1)
    del(p2)
    del(p3)
    

if __name__ == '__main__':
    main()
        
