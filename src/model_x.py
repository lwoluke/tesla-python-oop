# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:40:05 2022

@author: lwolu
"""

# Python file(s)
from electric_car import ElectricCar


class ModelX(ElectricCar):
    
    car_model = "Model X"
    """
    car_model (str): (class attribute) Name of model for every 
        instance object of the class.
    """
    
    car_type = "SUV"
    """
    car_type (str): (class attribute) Name of the general model 
        type for every instance object of the class.
    """
    
    has_lane_assist = True
    """has_lane_assist (bool): (class attribute) Every instance
        object of this class has lane assist technology.
    """
    
    def __init__(self, color="Pearl White Multi-Coat", price=114990, 
                 year_built=2022, drive_type="AWD", range_type="Standard", 
                 wheel_type="20in Cyberstream", interior="All Black Ebony", 
                 inventory_type="New", charge_time="9.5 hrs", 
                 has_selfdriving=False, has_plaid_mode=False, 
                 storage_size="Standard", number_seats=5):
        """
        Initializes an instance object of the ModelX class. Uses 
            the ElectricCar class as an initializer for the 
            model, color, price, year_built, drive_type, range_type,
            wheel_type, interior, inventory_type, and charge_time
            parameters.

        Args:
            color (str, optional): The color that the Model X is. 
                Defaults to "Pearl White Multi-Coat".
            price (int, optional): How much the Model X costs. 
                Defaults to 114990.
            year_built (int, optional): The year the Model X was 
                built in. Defaults to 2022.
            drive_type (str, optional): The type of drivetrain that the
                Model X has (Ex: AWD, FWD, or RWD). Defaults to "AWD".
            range_type (str, optional): What type of range that the 
                electric car has (Ex: Standard or long distance). 
                Defaults to "Standard".
            wheel_type (str, optional): What type of wheels that the 
                Model X has (Ex: 18in chrome). Defaults to "20in Cyberstream".
            interior (str, optional): The style of the Model X's 
                interior (Ex: Dark Grey Mesh). Defaults to 
                "All Black Ebony".
            inventory_type (str, optional): The inventory status of
                the Model X (Ex: New or used). Defaults to "New".
            charge_time (str, optional): How long it takes the Model X
                to fully charge. Defaults to "X hrs". Defaults to 
                "9.5 hrs".
            has_selfdriving (bool, optional): Whether the Model X has 
                self-driving technology. Defaults to False.
            has_plaid_mode (TYPE, optional): Whether the Model X has 
                plaid mode technology. Defaults to False.
            storage_size (TYPE, optional): How much storage space the
                Model X has. Defaults to "Standard".
            number_seats (TYPE, optional): How many seats that the 
                Model X has. Defaults to 5.

        """

        super().__init__(model=ModelX.car_model, 
                         color="Pearl White Multi-Coat", price=114990,
                         year_built=2022, model_type=ModelX.car_type, 
                         drive_type="AWD", range_type="Standard", 
                         wheel_type="20in Cyberstream", 
                         interior="All Black Ebony", 
                         inventory_type="New", charge_time="9.5 hrs")
        
        if color == None:
            self._color = "Pearl White Multi-Coat"
        else: 
            self._color = color
        
        if price == None: 
            self._price = 114990 
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
            self._wheel_type = "20in Cyberstream"
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
            self._charge_time = "9.5 hrs"
        else: 
            self._charge_time = charge_time
        
        if storage_size == None:
            self._storage_size = "Standard"
        else:
            self._storage_size = storage_size 
            
        if number_seats == None:
            self._number_seats = 5
        else:
            self._number_seats = number_seats
            
        if has_plaid_mode == None: 
            self._has_plaid_mode = str(False)
        else:
            self._has_plaid_mode = str(has_plaid_mode)
            
        if has_selfdriving == None: 
            self._has_selfdriving = str(False)
        else:
            self._has_selfdriving = str(has_selfdriving)
  
        self._model = ModelX.car_model
        self._model_type = ModelX.car_type
        self._id_ = id(self) 
        
        
    @classmethod    
    def get_details(cls):
        """
        Returns the essential class attributes for the Model X class.
        """
        return (f'Car Model: {cls.car_model}\n'
                f'Car Type: {cls.car_type}')    
    
    @staticmethod
    def remove(modelX, identification):
        """
        Deletes the specified Model X instance object and
            removes it from the cars list.

        Args:
            modelX (obj): The Model X object to delete.
            identification (int): ID needed to confirm this action.

        """
        if modelX.id_ == identification: 
            print("Destructor called. ModelX object, ")
            print(f"{modelX.color} {modelX.model} has been deleted\n")
            del(modelX)
        else:
            print("Unable to remove ModelX object " + 
                  "since ID doesn't exist in list.")
            
    def drive(self):
        """
        Simulates driving the Model X. 
        
        In doing so, the price of the Model X will decrease, 
            and become used if it was initially new.
            
        """
        price = float(self.price)
        if self.inventory_type.lower() == "new":
            print(f"Driving {self.inventory_type} ModelX...")
            self._inventory_type = "Used"
            self._price = price * .8
            self._price = '${:,.2f}'.format(self._price)
        else:
            print(f"Driving {self.inventory_type} ModelX...")
            self._price = price * .9
            self._price = '${:,.2f}'.format(self._price)
            
    def extra_features(self):
        """
        Returns the additional features of the specified 
            Model X object.
            
        Overrides the ElectricCar method. 
        
        """
        return(f"Additional feature(s) of this {self.model}, " 
               f"made in {self.year_built})\n"
               f"Has self driving: {self._has_selfdriving}\n"
               f"Has plaid mode: {self._has_plaid_mode}\n"
               f"Storage Size: {self._storage_size}\n"
               f"Number of seats: {self._number_seats}\n"
               f"Charge time: {self.charge_time}") 
    
    def __str__(self):
        """
        Allows the Model X object to be returned from the print 
            function. 

        Inherits the ElectricCar class magic method to print the 
            ID, model, year built, color, price, model type, 
            drive type, range type, wheel type, interior,
            and inventory type instance attributes.
           
        """
        return super().__str__()
        
    
    @property 
    def number_seats(self):
        """
        Returns how many seats that the specified Model X has.
        """
        return self._number_seats
    
    @number_seats.setter 
    def number_seats(self, updated):
        """
        Updates how many seats that the specified Model X has.
        """
        self._number_seats = updated
    
    @property 
    def storage_size(self):
        """
        Returns how much storage space that the Model X has.
        """
        return self._storage_size 
    
    @storage_size.setter 
    def storage_size(self, updated):
        """
        Updates how much storage space that the Model X has.
        """
        self._storage_size = updated
    
    @property 
    def has_selfdriving(self):
        """
        Returns the boolean of if the specified Model X has 
            self-driving technology.
            
        """
        return str(self._has_selfdriving)
    
    @has_selfdriving.setter 
    def has_selfdriving(self, update):
        """
        Updates the boolean of if the specified Model X has 
            self-driving technology.
            
        """
        self._has_selfdriving = str(update)
        
    @property 
    def has_plaid_mode(self):
        """
        Returns the boolean of if the specified Model X has 
            plaid mode technology.
            
        """
        return str(self._has_plaid_mode)
    
    @has_plaid_mode.setter 
    def has_plaid_mode(self, updated):
        """
        Updates the boolean of if the specified Model X has 
            plaid mode technology.
            
        """
        self._has_plaid_mode = updated
        

def main():
    print("***ModelX class testing***\n")
    
    print("Class data)")
    print(ModelX.get_details())
    
    count = 1
    print("\n---------------------------------")
    print(f"\nCreate ModelX object #{count}:")
    print("Without providing arguments)")
    
    m1 = ModelX()
    
    print(m1)
    print("\nFeatures)")
    print(m1.extra_features())

   
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate ModelX object #{count}:")
    print("Initialize with arguments)")
    
    m2 = ModelX("Midnight Silver Metallic", 159990, 2022, "AWD", "Plaid",
                "22in Turbine", "Black and White Carbon Fiber",
                "New", "9.25 hrs", True, True, "Extra Large", 6)
    
    print(m2)
    print()
    
    print(m2.extra_features())
    
    print("\nSee Inventory Status)")
    print(m2.value_status())
    print("After driving)")
    m2.drive()
    print(m2.value_status())
    
    
    print("\n---------------------------------")
    print("\nOutput list of ModelX object IDs)")
    print(ModelX.cars)
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    ModelX.remove(m1, m1.id_)
    ModelX.remove(m2, m2.id_)
    

if __name__ == '__main__':
    main()
