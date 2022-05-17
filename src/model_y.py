# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:39:08 2022

@author: lwolu
"""

# Python file(s)
from electric_car import ElectricCar


class ModelY(ElectricCar):
    
    car_model = "Model Y"
    """
    car_model (str): (class attribute) Name of model for every 
        instance object of the class.
    """
    
    car_type = "Crossover"
    """
    car_type (str): (class attribute) Name of the general model 
        type for every instance object of the class.
    """
    
    has_lane_assist = True
    """has_lane_assist (bool): (class attribute) Every instance
        object of this class has lane assist technology.
    """

    def __init__(self, color="Pearl White Multi-Coat", price=62990, 
                 year_built=2022, drive_type="AWD", range_type="Long Range", 
                 wheel_type="19in Gemini", interior="All Black", 
                 inventory_type="New", charge_time="10 hrs", 
                 has_selfdriving=False, number_seats=5, has_tow_hitch=False):
        """
        Initializes an instance object of the ModelY class. Uses 
            the ElectricCar class as an initializer for the 
            model, color, price, year_built, drive_type, range_type,
            wheel_type, interior, inventory_type, and charge_time
            parameters.

        Args:
            color (str, optional): The color that the Model Y is. 
                Defaults to "Pearl White Multi-Coat".
            price (int, optional): How much the Model Y costs. 
                Defaults to 62990.
            year_built (int, optional): The year the Model Y was 
                built in. Defaults to 2022.
            drive_type (str, optional): The type of drivetrain that the
                Model Y has (Ex: AWD, FWD, or RWD). Defaults to "AWD".
            range_type (str, optional): What type of range that the 
                electric car has (Ex: Standard or long distance). 
                Defaults to "Long Range".
            wheel_type (str, optional): What type of wheels that the 
                Model Y has (Ex: 18in chrome). Defaults to "19in Gemini".
            interior (str, optional): The style of the Model Y's 
                interior (Ex: Dark Grey Mesh). Defaults to 
                "All Black".
            inventory_type (str, optional): The inventory status of
                the Model Y (Ex: New or used). Defaults to "New".
            charge_time (str, optional): How long it takes the Model Y
                to fully charge. Defaults to "X hrs". Defaults to 
                "10 hrs".
            has_selfdriving (bool, optional): Whether the Model Y has 
                self-driving technology. Defaults to False.
            number_seats (int, optional): How many seats that the 
                Model Y has. Defaults to 5.
            has_tow_hitch (bool, optional): Whether the Model Y has 
                a tow hitch. Defaults to False.

        """

        super().__init__(model=ModelY.car_model, 
                         color="Pearl White Multi-Coat", price=62990,
                         year_built=2022, model_type=ModelY.car_type, 
                         drive_type="AWD", range_type="Long Range", 
                         wheel_type="19in Gemini", 
                         interior="All Black", 
                         inventory_type="New", charge_time="10 hrs")
        
        if color == None: 
            self._color = "Pearl White Multi-Coat"
        else:
            self._color = color 
            
        if price == None: 
            self._price = 62990
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
            self._range_type = "Long Range"
        else:
            self._range_type = range_type 
            
        if wheel_type == None: 
            self._wheel_type = "19in Gemini"
        else:
            self._wheel_type = wheel_type 
        
        if interior == None: 
            self._interior = "All Black"
        else:
            self._interior = interior 
    
        if inventory_type == None: 
            self._inventory_type = "New"
        else:
            self._inventory_type = inventory_type 
            
        if charge_time == None: 
            self._charge_time = "10 hrs"
        else:
            self._charge_time = charge_time
        
        if has_selfdriving == None: 
            self._has_selfdriving = str(False)
        else:
            self._has_selfdriving = str(has_selfdriving)
        
        if number_seats == None: 
            self._number_seats = 5
        else:
            self._number_seats = number_seats
        
        if has_tow_hitch == None:
            self._has_tow_hitch = str(False)
        else:
            self._has_tow_hitch = str(has_tow_hitch)
            
        
        self._has_lane_assist = str(ModelY.has_lane_assist)
        self._model = ModelY.car_model
        self._model_type = ModelY.car_type
        self._id_ = id(self) 
        
        
    @classmethod    
    def get_details(cls):
        """
        Returns the essential class attributes for the Model S class.
        """
        return(f'Car Model: {cls.car_model}\n'
               f'Car Type: {cls.car_type}')    
    
    @staticmethod
    def remove(modelY, identification):
        """
        Deletes the specified Model Y instance object and
            removes it from the cars list.

        Args:
            modelY (obj): The Model S object to delete.
            identification (int): ID needed to confirm this action.

        """
        if modelY.id_ == identification: 
            print("Destructor called. ModelY object, ")
            print(f"{modelY.color} {modelY.model} has been deleted\n")
            del(modelY)
        else:
            print("Unable to remove ModelY object " + 
                  "since ID doesn't exist in list.")
            
    def drive(self):
        """
        Simulates driving the Model Y. 
        
        In doing so, the price of the Model Y will decrease, 
            and become used if it was initially new.
            
        """
        price = float(self.price)
        if self.inventory_type.lower() == "new":
            print(f"Driving {self.inventory_type} ModelY...")
            self._inventory_type = "Used"
            self._price = price * .8
            self._price = '${:,.2f}'.format(self._price)
        else:
            print(f"Driving {self.inventory_type} ModelY...")
            self._price = price * .9
            self._price = '${:,.2f}'.format(self._price)
            
    def extra_features(self):
        """
        Returns the additional features of the specified 
            Model Y object.
            
        Overrides the ElectricCar method. 
        
        """
        return(f"Additional feature(s) of this {self.model}, "
               f"made in {self.year_built}\n"
               f"Has self driving: {self._has_selfdriving}"
               f"Has tow hitch: {self._has_tow_hitch}"
               f"Number of seats: {self._number_seats}"
               f"Charge time: {self.charge_time}") 
    
    def __str__(self):
        """
        Allows the Model Y object to be returned from the print 
            function. 

        Inherits the ElectricCar class magic method to print the 
            ID, model, year built, color, price, model type, 
            drive type, range type, wheel type, interior,
            and inventory type instance attributes.
           
        """
        return super().__str__()
    
    @property 
    def has_tow_hitch(self):
        """
        Returns the boolean of if the specified Model Y has 
            a tow hitch.
            
        """
        return self._has_tow_hitch 
    
    @has_tow_hitch.setter 
    def has_tow_hitch(self, updated):
        """
        Updates the boolean of if the specified Model Y has 
            a tow hitch.
            
        """
        self._has_tow_hitch = updated
    
    @property 
    def number_seats(self):
        """
        Returns how many seats the specified Model Y has.
        """
        return self._number_seats
    
    @number_seats.setter 
    def number_seats(self, updated):
        """
        Updates how many seats the specified Model Y has.
        """
        self._number_seats = updated
    
    @property 
    def has_selfdriving(self):
        """
        Returns the boolean of if the specified Model Y has 
            self-driving technology.
            
        """
        return str(self._has_selfdriving)
    
    @has_selfdriving.setter 
    def has_selfdriving(self, update):
        """
        Updates the boolean of if the specified Model Y has 
            self-driving technology.
            
        """
        self._has_selfdriving = str(update)
                

def main():
    print("***ModelY class testing***\n")
    
    print("Class data)")
    print(ModelY.get_details())
    
    count = 1
    print("\n---------------------------------")
    print(f"\nCreate ModelY object #{count}:")
    print("Without providing arguments)")
    
    m1 = ModelY()
    
    print(m1)
    print("\nFeatures)")
    print(m1.extra_features())

   
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate ModelY object #{count}:")
    print("Initialize with arguments)")
    
    m2 = ModelY("Red Multi-Coat", 82990, 2022, "AWD", "Long Range",
                "20in Induction", "Black and White", "New", 
                "9.35 hrs", True, 7, True)
    
    print(m2)
    print()
    
    print(m2.extra_features())
    
    print("\nSee Inventory Status)")
    print(m2.value_status())
    print("After driving)")
    m2.drive()
    print(m2.value_status())
    
    
    print("\n---------------------------------")
    print("\nOutput list of ModelY object IDs)")
    print(ModelY.cars)
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    ModelY.remove(m1, m1.id_)
    ModelY.remove(m2, m2.id_)
    

if __name__ == '__main__':
    main() 
