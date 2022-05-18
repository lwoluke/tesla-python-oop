# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:41:02 2022

@author: lwolu
"""

# Python file(s)
from electric_car import ElectricCar


class Model3(ElectricCar):
    
    car_model = "Model 3"
    """
    car_model (str): (class attribute) Name of model for every 
        instance object of the class.
    """
    
    car_type = "Compact Sedan"
    """
    car_type (str): (class attribute) Name of the general model 
        type for every instance object of the class.
    """
    
    has_lane_assist = True
    """has_lane_assist (bool): (class attribute) Every instance
        object of this class has lane assist technology.
    """
    
    def __init__(self, color="White", price=42190, year_built=2022, 
                     drive_type="RWD", range_type="Standard", 
                 wheel_type="18in Aero", interior="All Black Leather", 
                 inventory_type="New", charge_time="8.5 hrs", 
                 has_selfdriving=False, has_lane_assist=False):
        """
        Initializes an instance object of the Model3 class. Uses 
            the ElectricCar class as an initializer for the 
            model, color, price, year_built, drive_type, range_type,
            wheel_type, interior, inventory_type, and charge_time
            parameters.
        
        Args:
            color (str, optional): The color that the Model 3 is. 
                Defaults to "White".
            price (int, optional): How much the Model 3 costs. 
                Defaults to 42190.
            year_built (int, optional): The year the Model 3 was 
                built in. Defaults to 2022.
            drive_type (str, optional): The type of drivetrain that the
                Model 3 has (Ex: AWD, FWD, or RWD). Defaults to "RWD".
            range_type (str, optional): What type of range that the 
                electric car has (Ex: Standard or long distance). 
                Defaults to "Standard".
            wheel_type (str, optional): What type of wheels that the 
                Model 3 has (Ex: 18in chrome). Defaults to "18in Aero".
            interior (str, optional): The style of the Model 3's 
                interior (Ex: Dark Grey Mesh). Defaults to 
                "All Black Leather".
            inventory_type (str, optional): The inventory status of
                the Model 3 (Ex: New or used). Defaults to "New".
            charge_time (str, optional): How long it takes the Model 3
                to fully charge. Defaults to "X hrs". Defaults to 
                "8.5 hrs".
            has_selfdriving (bool, optional): Whether the Model 3 has 
                self-driving technology. Defaults to False.
            has_lane_assist (bool, optional): Whether the Model 3 has 
                lane assist technology. Defaults to False.

        """
        super().__init__(model=Model3.car_model, color="White", 
                         price=42190, year_built=2022, 
                         model_type=Model3.car_type, drive_type="RWD", 
                         range_type="Standard", wheel_type="18in Aero", 
                         interior="All Black Leather", 
                         inventory_type="New", charge_time="8.5 hrs")
        
        
        if color == None:
            self._color = "White"
        else: 
            self._color = color
        
        if price == None: 
            self._price = 42190 
        else: 
            self._price = price
        
        if year_built == None: 
            self._year_built = 2022 
        else: 
            self._year_built = year_built 
            
        if drive_type == None: 
            self._drive_type = "RWD"
        else:
            self._drive_type = drive_type
            
        if range_type == None: 
            self._range_type = "Standard"
        else:
            self._range_type = range_type
            
        if wheel_type == None:
            self._wheel_type = "18in Aero"
        else:
            self._wheel_type = wheel_type 
            
        if interior == None: 
            self._interior = "All Black Leather"
        else:
            self._interior = interior 
            
        if inventory_type == None: 
            self._inventory_type = "New"
        else:
            self._inventory_type = inventory_type
            
        if charge_time == None:
            self._charge_time = "8.5 hrs"
        else: 
            self._charge_time = charge_time
            
        if has_selfdriving == None: 
            self._has_selfdriving = str(False)
        else:
            self._has_selfdriving = str(has_selfdriving)
            
        self._has_lane_assist = str(has_lane_assist)
        self._model = Model3.car_model
        self._model_type = Model3.car_type
        self._id_ = id(self) 
        
        
    @classmethod    
    def get_details(cls):
        """
        Returns the essential class attributes for the Model 3 class.
        """
        return (f'Car Model: {cls.car_model}\n'
                f'Car Type: {cls.car_type}')
        
    @staticmethod
    def remove(model3, identification):
        """
        Deletes the specified Model 3 instance object and
            removes it from the cars list.

        Args:
            model3 (obj): The Model 3 object to delete.
            identification (int): ID needed to confirm this action.

        """
        if model3.id_ == identification: 
            print("Destructor called. Model3 object,\n"
                  f"{model3.color} {model3.model} has been deleted\n")
            del(model3)
        else:
            print("Unable to remove Model3 object "  
                  "since ID doesn't exist in list.")
            
    def drive(self):
        """
        Simulates driving the Model 3. 
        
        In doing so, the price of the Model 3 will decrease, 
            and become used if it was initially new.
            
        """
        price = float(self.price)
        if self.inventory_type.lower() == "new":
            print(f"Driving {self.drive_type} Model 3...")
            self._inventory_type = "Used"
            self._price = price * .8
            self._price = '${:,.2f}'.format(self._price)
        else:
            print(f"Driving {self.drive_type} Model 3...")
            self._price = price * .9
            self._price = '${:,.2f}'.format(self._price)
        
    def extra_features(self):
        """
        Returns the additional features of the specified 
            Model 3 object.
            
        Overrides the ElectricCar method. 
        
        """
        return(f"Additional feature(s) of this {self.model}, "
              f"made in {self.year_built})\n"
              f"Has self driving: {self._has_selfdriving}\n"
              f"Has lane assist: {self._has_lane_assist}\n"
              f"Charge time: {self.charge_time}")
        
    def __str__(self):
        """
        Allows the Model 3 object to be returned from the print 
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
        Returns the boolean of if the specified Model 3 has 
            self-driving technology.
            
        """
        return str(self._has_selfdriving)
    
    @has_selfdriving.setter 
    def has_selfdriving(self, update):
        """
        Updates the boolean of if the specified Model 3 has 
            self-driving technology.
            
        """
        self._has_selfdriving = str(update)
        
    @property 
    def has_lane_assist(self):
        """
        Returns the boolean of if the specified Model 3 has 
            lane assist technology.
            
        """
        return str(self._has_lane_assist)
    
    @has_lane_assist.setter 
    def has_lane_assist(self, updated_status):
        """
        Updates the boolean of if the specified Model 3 has 
            lane assist technology.
            
        """
        self._has_lane_assist = str(updated_status)
        
        
        
def main():
    print("***Model3 class testing***\n")
    
    print("Class data)")
    print(Model3.get_details())
    
    count = 1
    print("\n---------------------------------")
    print(f"\nCreate Model3 object #{count}:")
    print("Without providing arguments)")
    
    m1 = Model3()
    
    print(m1)
    print("\nFeatures)")
    print(m1.extra_features())

   
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate Model3 object #{count}:")
    print("Initialize with arguments)")
    
    m2 = Model3("Red", 75000, 2020, "AWD", "Performance",
                "20in Überturbine", "Black and White Mesh", 
                "Used", "9 hrs", True, True)
    
    print(m2)
    print()
    
    print(m2.extra_features())
    
    print("\nSee Inventory Status)")
    print(m2.value_status())
    print("After driving)")
    m2.drive()
    print(m2.value_status())
    
    
    print("\n---------------------------------")
    print("\nOutput list of Model3 object IDs)")
    print(Model3.cars)
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    Model3.remove(m1, m1.id_)
    Model3.remove(m2, m2.id_)
    

if __name__ == '__main__':
    main()
