# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:40:35 2022

@author: lwolu
"""

# Python file(s)
from electric_car import ElectricCar


class ModelS(ElectricCar):
    
    car_model = "Model S"
    """
    car_model (str): (class attribute) Name of model for every 
        instance object of the class.
    """
    
    car_type = "Agile Sports Sedan"
    """
    car_type (str): (class attribute) Name of the general model 
        type for every instance object of the class.
    """
    
    has_lane_assist = True
    """has_lane_assist (bool): (class attribute) Every instance
        object of this class has lane assist technology.
    """
    
    
    def __init__(self, color="Pearl White Multi-Coat", price=99990, year_built=2022, 
                     drive_type="AWD", range_type="Standard", 
                 wheel_type="19in Tempest", interior="All Black Ebony", 
                 inventory_type="New", charge_time="8.75 hrs", 
                 has_selfdriving=False, has_plaid_mode=False):
        """
        Initializes an instance object of the ModelS class. Uses 
            the ElectricCar class as an initializer for the 
            model, color, price, year_built, drive_type, range_type,
            wheel_type, interior, inventory_type, and charge_time
            parameters.

        Args:
            color (str, optional): The color that the Model S is. 
                Defaults to "Pearl White Multi-Coat".
            price (int, optional): How much the Model S costs. 
                Defaults to 99990.
            year_built (int, optional): The year the Model S was 
                built in. Defaults to 2022.
            drive_type (str, optional): The type of drivetrain that the
                Model S has (Ex: AWD, FWD, or RWD). Defaults to "AWD".
            range_type (str, optional): What type of range that the 
                electric car has (Ex: Standard or long distance). 
                Defaults to "Standard".
            wheel_type (str, optional): What type of wheels that the 
                Model S has (Ex: 18in chrome). Defaults to "19in Tempest".
            interior (str, optional): The style of the Model S's 
                interior (Ex: Dark Grey Mesh). Defaults to 
                "All Black Ebony".
            inventory_type (str, optional): The inventory status of
                the Model S (Ex: New or used). Defaults to "New".
            charge_time (str, optional): How long it takes the Model S
                to fully charge. Defaults to "X hrs". Defaults to 
                "8.75 hrs".
            has_selfdriving (TYPE, optional): Whether the Model S has 
                self-driving technology. Defaults to False.
            has_plaid_mode (TYPE, optional): Whether the Model S has 
                plaid mode technology. Defaults to False.

        """

        super().__init__(model=ModelS.car_model, color="Pearl White Multi-Coat", 
                         price=99990, year_built=2022, 
                         model_type=ModelS.car_type, drive_type="AWD", 
                         range_type="Standard", wheel_type="19in Tempest", 
                         interior="All Black Ebony", 
                         inventory_type="New", charge_time="8.75 hrs")
        
        if color == None: 
            self._color = "Pearl White Multi-Coat"
        else:
            self._color = color 
            
        if price == None: 
            self._price = 99990
        else: 
            self._price = price
            
        if year_built == None: 
            self._year_built = 2022
        else:
            self._year_built = year_built 
            
        if drive_type == None: 
            self._drive_type = "AWD"
        else:
            self._drive_type = drive_type 
            
        if range_type == None: 
            self._range_type = "Standard"
        else:
            self._range_type = range_type 
            
        if wheel_type == None: 
            self._wheel_type = "19in Tempest"
        else:
            self._wheel_type = wheel_type 
            
        if interior == None: 
            self._interior = "All Black Ebony"
        else:
            self._interior = interior 
        
        if inventory_type == None: 
            self._inventory_type = "New"
        else:
            self._inventory_type = inventory_type 
            
        if charge_time == None:
            self._charge_time = "8.75 hrs"
        else:
            self._charge_time = charge_time
        
        if has_selfdriving == None: 
            self._has_selfdriving = str(False)
        else:
            self._has_selfdriving = str(has_selfdriving) 
            
        if has_plaid_mode == None: 
            self._has_plaid_mode = str(False)
        else:
            self._has_plaid_mode = str(has_plaid_mode)
        
        self._has_lane_assist = str(ModelS.has_lane_assist)
        self._model = ModelS.car_model
        self._model_type = ModelS.car_type
        self._id_ = id(self) 
        
    @classmethod    
    def get_details(cls):
        """
        Returns the essential class attributes for the Model S class.
        """
        return (f'Car Model: {cls.car_model}\n'
                f'Car Type: {cls.car_type}')    
    
    @staticmethod
    def remove(modelS, identification):
        """
        Deletes the specified Model S instance object and
            removes it from the cars list.

        Args:
            modelS (obj): The Model S object to delete.
            identification (int): ID needed to confirm this action.

        """
        if modelS.id_ == identification: 
            print("Destructor called. ModelS object, ")
            print(f"{modelS.color} {modelS.model} has been deleted\n")
            del(modelS)
        else:
            print("Unable to remove ModelS object " + 
                  "since ID doesn't exist in list.")
            
    def drive(self):
        """
        Simulates driving the Model S. 
        
        In doing so, the price of the Model S will decrease, 
            and become used if it was initially new.
            
        """
        price = float(self.price)
        if self.inventory_type.lower() == "new":
            print(f"Driving {self.color} ModelS...")
            self._inventory_type = "Used"
            self._price = price * .8
            self._price = '${:,.2f}'.format(self._price)
        else:
            print(f"Driving {self.color} ModelS...")
            self._price = price * .9
            self._price = '${:,.2f}'.format(self._price)
   
    def extra_features(self):
        """
        Returns the additional features of the specified 
            Model S object.
            
        Overrides the ElectricCar method. 
        
        """
        return(f"Additional feature(s) of this {self.model}, "
              f"made in {self.year_built}\n"
              f"Has self driving: {self._has_selfdriving}\n" 
              f"Has plaid mode: {self._has_plaid_mode}\n"
              f"Has lane assist: {self._has_lane_assist}"
              f"Charge time: {self.charge_time}") 
   
    def __str__(self):
        """
        Allows the Model S object to be returned from the print 
            function. 

        Inherits the ElectricCar class magic method to print the 
            ID, model, year built, color, price, model type, 
            drive type, range type, wheel type, interior,
            and inventory type instance attributes.
           
        """
        return super().__str__()
    
    @property 
    def has_selfdriving(self):
        """
        Returns the boolean of if the specified Model S has 
            self-driving technology.
            
        """
        return str(self._has_selfdriving)
    
    @has_selfdriving.setter 
    def has_selfdriving(self, update):
        """
        Updates the boolean of if the specified Model S has 
            self-driving technology.
            
        """
        self._has_selfdriving = str(update)
        
    @property 
    def has_plaid_mode(self):
        """
        Returns the boolean of if the specified Model S has 
            plaid mode technology.
            
        """
        return str(self._has_plaid_mode)
    
    @has_plaid_mode.setter 
    def has_plaid_mode(self, updated):
        """
        Updates the boolean of if the specified Model S has 
            self-driving technology.
            
        """
        self._has_plaid_mode = updated
    

def main():
    print("***ModelS class testing***\n")
    
    print("Class data)")
    print(ModelS.get_details())
    
    count = 1
    print("\n---------------------------------")
    print(f"\nCreate ModelS object #{count}:")
    print("Without providing arguments)")
    
    m1 = ModelS()
    
    print(m1)
    print("\nFeatures)")
    print(m1.extra_features())

   
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate ModelS object #{count}:")
    print("Initialize with arguments)")
    
    m2 = ModelS("Solid Black", 143990, 2022, "AWD", "Plaid",
                "21in Arachnid", "Cream Carbon Fiber",
                "New", "59 mins", True, True)
    
    print(m2)
    print()
    
    print(m2.extra_features())
    
    print("\nSee Inventory Status)")
    print(m2.value_status())
    print("After driving)")
    m2.drive()
    print(m2.value_status())
    
    
    print("\n---------------------------------")
    print("\nOutput list of ModelS object IDs)")
    print(ModelS.cars)
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    ModelS.remove(m1, m1.id_)
    ModelS.remove(m2, m2.id_)
    

if __name__ == '__main__':
    main()
