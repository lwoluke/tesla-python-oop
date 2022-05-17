# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:42:35 2022

@author: lwolu
"""


class Corporation:
    
    
    company_type = 'Corporation'
    """
    company_type (str): (class attribute) The type of company 
        that the class is.
    """
    
    company_type_explanation = ("A corporation is a fully independent " + 
            "business that's made up of multiple shareholders who are " +
            "provided with stock in the business.")
    """
    company_type_explanation (str): (class attribute) Brief description 
        explaining what a corporation is.
    """
    
    tax_filing_types = "S and C Corporation"
    """
    tax_filing_types (str): (class attribute) The options for tax 
        filing that a corporation has.
    
    A C corporation (or C-corp) is a legal structure for a corporation 
        in which the owners, or shareholders, are taxed separately from 
        the entity. C corporations, the most prevalent of corporations, 
        are also subject to corporate income taxation. The taxing of 
        profits from the business is at both corporate and personal levels, 
        creating a double taxation situation.

    Source: https://www.investopedia.com/terms/c/c-corporation.asp#:~:text=What%20Is%20a%20C%20Corporation,subject%20to%20corporate%20income%20taxation.

    
    A S corporation, also known as an S subchapter, refers to a type 
        of legal business entity. Requirements give a corporation with 
        100 shareholders or less the benefit of incorporation while 
        being taxed as a partnership. Shareholders report income and 
        losses on individual tax returns, and pay taxes at ordinary tax rates.
        
    Source: https://www.investopedia.com/articles/investing/091614/understanding-s-corporations.asp
        
    """
    
    def __init__(self, name='Default Name Placeholder', 
                 headquarters='Default Location Placeholder', 
                 industry='Default Industry Placeholder', 
                 bio='Default Info Placeholder'):
        """
        Initializes an instance object of the Corporation class.

        Args:
            name (str, optional): The name of the corporation. Defaults 
                to 'Default Name Placeholder'.
            headquarters (str, optional): Where the corporation is 
                located. Defaults to 'Default Location Placeholder'.
            industry (str, optional): What industry the corporation is 
                in. Defaults to 'Default Industry Placeholder'.
            bio (str, optional): Brief introduction of the what the 
                corporation represents. Defaults to 
                'Default Info Placeholder'.

        """
        
        if name == None:
            self._name = 'Default Name Placeholder'
        else: 
            self._name = name
        
        if headquarters == None:
            self._headquarters = 'Default Location Placeholder'
        else:
            self._headquarters = headquarters
        
        if industry == None:
            self._industry = 'Default Industry Placeholder'
        else:
            self._industry = industry
            
        if bio == None:
            self._bio = 'Default Info Placeholder'
        else: 
            self._bio = bio
    
    def greet(self):
        """
        Returns an introduction message for a Corporation object using its 
            name, industry, and headquarters instance attributes. 

        """
        return(f'Hello, this is {self.name}. We specialize '
              f'in {self.industry} and are located in {self.headquarters} ')
    
    @classmethod
    def company_meaning(cls):
        """
        Returns the class attributes for the Corporation class.
        """
        string = ""
        string += ('Type of company: ' + cls.company_type + '\n')
        string += ('Explanation: ' + cls.company_type_explanation + '\n')
        string += ('Tax filing types: ' + cls.tax_filing_types + '\n')
        return string
        
    def __str__(self):
        """
        Allows the Corporation object to be returned from the print 
            function. 
         
        Returns:
            string (str): The name, headquarters, industry, and bio
                of the corporation specified.

        """
        string = ""
        string += ('Company name: ' + self.name + '\n')
        string += ('Headquarters: ' + self.headquarters + '\n')
        string += ('Industry: ' + self.industry + '\n')
        string += ('Info: ' + self.bio)
        return string
          
    def __del__(self):
        """
        Allows the Corporation object to be deleted from the del statement.
        """
        print('Destructor called. Corporation object '
              f'{self.name} has been deleted')
    
    @property 
    def name(self):
        """
        Returns the name of the specified corporation.
        """
        return self._name
    
    @name.setter
    def name(self, new_name):
        """
        Updates the name of the specified corporation.
        """
        self._name = new_name
        
    @property 
    def headquarters(self):
        """
        Returns the headquarters of the specified corporation.
        """
        return self._headquarters
    
    @headquarters.setter
    def headquarters(self, new_headquarters):
        """
        Updates the headquarters of the specified corporation.
        """
        self._headquarters = new_headquarters
    
    @property 
    def industry(self):
        """
        Returns the industry of the specified corporation.
        """
        return self._industry
    
    @industry.setter
    def industry(self, new_industry):
        """
        Updates the industry of the specified corporation.
        """
        self._industry = new_industry
        
    @property 
    def bio(self):
        """
        Returns the bio of the specified corporation.
        """
        return self._bio
    
    @bio.setter
    def bio(self, new_bio):
        """
        Updates the bio of the specified corporation.
        """
        self._bio = new_bio
    
    
def main():
    print("***Corporation class testing***\n")
    
    print("Class data)")
    print(Corporation.company_meaning())
    
    count = 1
    print("---------------------------------")
    print(f"\nCreate Corporation object #{count}")
    
    c1_info = "Through the company's four main business " \
        "segments—cloud and license, hardware, and services—Oracle " \
        "sells its cloud-engineering services and systems " \
        "and database management systems." 
        
    c1 = Corporation("Oracle", "Austin, TX", "Enterprise Software", c1_info)
    
    print("Greet method: ", end="")
    print(c1.greet())
    print("Update headquarters to Seattle, WA and industry to Cloud Computing")
    
    c1.headquarters = "Seattle, WA"
    c1.industry = "Cloud Computing"
    
    print("Greet method: ", end="")
    print(c1.greet())
    count += 1
    
    
    print("\n---------------------------------")
    print(f"\nCreate Corporation object #{count}")
    print("Without providing arguments)")
    print("Greet method: ", end="")
    
    c2 = Corporation()
    
    print(c2.greet())
    print("After updating all arguments)")
    
    c2_info = "A private spaceflight company based in Kent, Washington " \
        "that is working to send tourists to space on its reusable " \
        "suborbital rocket called New Shepard. The company was created " \
        "in 2000 by Jeff Bezos, the founder and CEO of Amazon.com." 
        
    c2.name = "Blue Orgin"
    c2.headquarters = "Kent, WA"
    c2.industry = "Aerospace"
    c2.bio = c2_info
    
    print("Greet method: ", end="")
    print(c2.greet())
    print("Get company bio)")
    print(c2.bio)
    count += 1
    
    
    print("\n---------------------------------")
    print(f"\nCreate Corporation object #{count}")
    print("Without providing arguments)")
    print("Print object)")
    
    c3 = Corporation()
    
    print(c3)
    print("After updating info and name)")
    
    c3.bio = "This company is still a mystery."
    c3.name = "Undercover"
    
    print("Print object)")
    print(c3)
    
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} Corporation objects:")
    del(c1)
    del(c2)
    del(c3)
    

if __name__ == '__main__':
    main()
