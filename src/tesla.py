# -*- coding: utf-8 -*-
"""
Created on Mon May  9 06:03:31 2022

@author: lwolu
"""

# Required imports for method calculations
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Python file(s)
from corporation import Corporation
        
        
class Tesla(Corporation):
    
    filing_status = 'C Corp'
    """
    filing_status (str): (class attribute) The tax filing status of Tesla.
    """
        
    tax_rate = 21
    """
    tax_rate (int): (class attribute) The corporate tax rate for Tesla.
    """
    
    total_revenue = 2270000000
    """
    total_revenue (int): (class attribute) Tesla's revenue so far this 
        year.
    """
    
    total_expenses = 1685000000
    """
    total_expenses (int): (class attribute) Tesla's expenses so far 
        this year.
    """
    
    date_founded = '7/1/2003'
    """
    date_founded (str): (class attribute) When Tesla was founded.
    """
    
    stock_ticker = 'TSLA'
    """
    stock_ticker (str): (class attribute) The symbol used to uniquely 
    identify publicly traded shares of Tesla.
    """
    
    founders = ['Elon Musk, Martin Eberhard, JB Straubel, '
                'Marc Tarpenning, Ian Wright']
    """
    founders (list[str]): (class attribute) The people who started the 
        company Tesla.
    """
    
    name='Tesla'
    """
    name (str): (class attribute) The name of the company.
    """
    
    headquarters='Austin, TX' 
    """
    headquarters (str): (class attribute) The location of Tesla's 
        main office.
    """
    
    industry='Automotive and Clean Energy'
    """
    industry (str): (class attribute) The business areas in which 
        Tesla operates in.
    """
    
    
    def __init__(self, bio=None, 
                 revenue=0, expenses=0):
        """
        Initializes an instance object of the Tesla class. Uses 
            the Corporation class as an initializer for the 
            name, headquarters, industry, and bio parameters.
   
        Args:
            bio (str, optional): Brief introduction of what 
                Tesla represents. Defaults to None.
            revenue (int, optional): The current revenue of Tesla 
                for the quarter. Defaults to 0.
            expenses (int, optional): The current expenses of Tesla 
                for the quarter. Defaults to 0.

        """
        
        super().__init__(name=Tesla.name, headquarters=Tesla.headquarters, 
                         industry=Tesla.industry, bio=None)    
        
        if bio == None:
            self._bio = ('We design and manufacture electric ' 
            'vehicles, battery energy storage from home to ' 
            'grid-scale, solar panels and solar roof tiles, ' 
            'and related products and services.')
        else: 
            self._bio = bio
            
        self._revenue = revenue
        self._expenses = expenses
        
    @classmethod
    def get_details(cls):
        """
        The essential class attributes for the Tesla class.
        
        Returns:
            string (str): The name, date founded, founders, headquarters, 
                industry, and stock ticker of Tesla.

        """
        string = ""
        string += f"Name: {cls.name}\n"
        string += f"Date founded: {cls.date_founded}\n"
        string += "Founders: "
        string += ', '.join(map(str, cls.founders))
        string += f"Headquarters: {cls.headquarters}\n"
        string += f"Industry: {cls.industry}\n"
        string += f"Stock ticker: {cls.stock_ticker}"
        
        return string
        
    @classmethod
    def tax_status(cls):
        """
        The tax related class attributes associated with Tesla.
        
        Returns:
            string (str): The filing status and tax rate of Tesla.
        
        """
        string = ""
        string += f'Filing status: {cls.filing_status}\n'
        string += f'Tax rate: {cls.tax_rate}%'
        
        return string
        
    @classmethod 
    def get_total_revenue(cls):
        """
        Returns the total revenue that Tesla has earned for this year.
        """
        string = ""
        string += "$"
        string += format(cls.total_revenue,",")
        
        return string
        
    @classmethod 
    def get_total_expenses(cls):
        """
        Returns the total expenses that Tesla has for this year.
        """
        string = ""
        string += "$"
        string += format(cls.total_expenses,",")
        
        return string
        
    @classmethod 
    def total_profit(cls):
        """
        Returns Tesla's profit expressed as a dollar amount 
            and margin for this year.
        """
        profit = cls.total_revenue - cls.total_expenses 
        margin = (profit / cls.total_revenue) * 100
        profit = format(profit,",")
        margin = '%.2f' % round(margin, 2)
        
        string = f"Total Profit: ${profit}\n"
        string += f"Total Margin: {margin}%"
    
        return string
        
    @classmethod 
    def time_as_company(cls):
        """
        Returns the total time elapsed in years, months, and days
            since Tesla was founded.
        """
        company_date = cls.date_founded.split('/')
        company_day = int(company_date[1])
        company_month = int(company_date[0])
        company_year = int(company_date[2])
        
        company_datetime = datetime(company_year, company_month, company_day)
        
        end_date = datetime.today()
        diff_in_years = relativedelta(end_date, company_datetime).years
        diff_in_months = relativedelta(end_date, company_datetime).months
        diff_in_days = relativedelta(end_date, company_datetime).days
        
        string = ('---Time since Tesla was founded---' + '\n' +
                  str(diff_in_years) + ' years, ' +
                  str(diff_in_months) + ' months, ' +
                  str(diff_in_days) + ' days')
        
        return string

    def current_profit(self):
        """
        Returns Tesla's current profit expressed as a dollar amount 
            and margin for this quarter.
        """
        profit = self.revenue - self.expenses 
        
        if self.revenue == 0:
            margin = 0
        else: 
            margin = (profit / self.revenue) * 100
        
        margin = '%.2f' % round(margin, 2)
        profit = format(profit,",")
        
        string = f"Current Profit: ${profit}\n"
        string += f"Current Margin: {margin}%"
        
        return string

    def get_financials(self):
        """
        Returns the essential financial information for the current 
            quarter and the year so far.

        """
        current_revenue = format(self.revenue,",")
        current_expenses = format(self.expenses,",")
        
        total_revenue = format(self.total_revenue,",")
        total_expenses = format(self.total_expenses,",")
        
        string = "So far this fiscal quarter:\n"
        string += f"Current revenue: ${current_revenue}\n"
        string += f"Current expenses: ${current_expenses}\n"
        string += self.current_profit()
        string += "\n"
        string += "\nSo far this fiscal year:\n"
        string += f"Total revenue: ${total_revenue}\n"
        string += f"Total expenses: ${total_expenses}\n"
        string += Tesla.total_profit()
        
        return string

    def sell(self, car_model, amt_sold=1):
        """
        Used to sell Tesla car inventory. After each car is sold, 
            the current and total revenue along with expenses are 
            each increased. This updates the results of multiple 
            methods for the Tesla class.

        Args:
            car_model (str): The type of Tesla car that will be sold.
            amt_sold (int, optional): The number of Tesla cars to sell. 
                Defaults to 1.

        """
        if car_model.lower() == "model3":
            
            print(f"Selling {amt_sold} Model 3 cars...")
            for i in range(amt_sold):
                revenue = 46990
                expenses = 32000
                self.revenue += revenue
                self.expenses += expenses
                Tesla.total_revenue += revenue
                Tesla.total_expenses += expenses
            
        elif car_model.lower() == "models":
            
            print(f"Selling {amt_sold} Model S cars...")
            for i in range(amt_sold):
                revenue = 99990
                expenses = 66600
                self.revenue += revenue
                self.expenses += expenses
                Tesla.total_revenue += revenue
                Tesla.total_expenses += expenses
            
        elif car_model.lower() == "modelx":
            
            print(f"Selling {amt_sold} Model X cars...")
            for i in range(amt_sold):
                revenue = 114990
                expenses = 73000
                self.revenue += revenue
                self.expenses += expenses
                Tesla.total_revenue += revenue
                Tesla.total_expenses += expenses
            
        elif car_model.lower() == "modely":
            
            print(f"Selling {amt_sold} Model Y cars...")
            for i in range(amt_sold):
                revenue = 62990
                expenses = 37000
                self.revenue += revenue
                self.expenses += expenses
                Tesla.total_revenue += revenue
                Tesla.total_expenses += expenses
            
        else:
            print("The {car_model} hasn't been released yet, or doesn't exist")

    def __str__(self):
        """
        Allows the Tesla object to be returned from the print 
            function. 
         
        Inherits the Corporation class magic method to print the 
            name, headquarters, industry, and bio instance attributes.
        
        Returns:
            string (str): The name, headquarters, industry, bio, 
                date founded, and stock ticker of Tesla.
        """
        result = super().__str__()
        result += ("\nDate Founded: " + self.date_founded + '\n')
        result += ("Stock ticker: " + self.stock_ticker + '\n')
        return result
    
    def __del__(self):
        """
        Allows the Tesla object to be deleted from the del statement.
        """
        print('Destructor called. Tesla object has been deleted')
    
    @property 
    def bio(self):
        """
        Returns Tesla's bio.
        """
        return self._bio 
    
    @bio.setter 
    def bio(self, updated):
        """
        Updates Tesla's bio.
        """
        self._bio = updated
    
    @property 
    def revenue(self):
        """
        Returns Tesla's current revenue.
        """
        return self._revenue 
    
    @revenue.setter 
    def revenue(self, new_value):
        """
        Updates Tesla's current revenue.
        """
        self._revenue = new_value
        
    @property 
    def expenses(self):
        """
        Returns Tesla's current expenses.
        """
        return self._expenses 
    
    @expenses.setter 
    def expenses(self, new_value):
        """
        Updates Tesla's current expenses.
        """
        self._expenses = new_value
        
        
def main():
    print("***Tesla class testing***\n")
    
    print("Class data)")
    print(Tesla.get_details())
    
    print("\nTax status)")
    print(Tesla.tax_status())
    
    print()
    print(Tesla.time_as_company())
    
    print("\n---------------------------------")
    print("\nCreate Tesla object without providing arguments")
    
    t = Tesla()
    
    print(t)
    print("Initial Financials)")
    
    print(t.get_financials())
    print()
    
    model3_amt = 557
    models_amt = 87
    modelx_amt = 238
    modely_amt = 202
    print("Sell the following)")
    print(f"{model3_amt} Model 3 Cars")
    print(f"{models_amt} Model S Cars")
    print(f"{modelx_amt} Model X Cars")
    print(f"{modely_amt} Model Y Cars\n")
    
    t.sell("model3", model3_amt)
    t.sell("models", models_amt)
    t.sell("modelx", modelx_amt)
    t.sell("modely", modely_amt)
    
    print("\nUpdated Financials)")
    
    print(t.get_financials())
    
    print("---------------------------------")
    print("\nCall Destructor on Tesla object:")
    del(t)
    

if __name__ == '__main__':
    main()
  
