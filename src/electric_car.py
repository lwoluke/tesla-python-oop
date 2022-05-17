# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:41:39 2022

@author: lwolu
"""


class ElectricCar:
    
    energy_source = 'Electric'
    """
    energy_source (str): (class attribute) Energy source of this 
        car type.
    """
    
    has_touchscreen = True
    """
    has_touchscreen (bool): (class attribute) All instances 
        have touchscreen.
    """
    
    has_caraoke = True 
    """
    has_caraoke (bool): (class attribute) All instances 
        have caraoke.
    """
    
    has_streaming = True
    """
    has_streaming (bool): (class attribute) All instances 
        have streaming.
    """
    
    has_internet= True
    """
    has_internet (bool): (class attribute) All instances 
        have internet.
    """
    
    cars = []
    """
    cars (list[int]): The IDs of the ElectricCar objects that
        have been created.
    """
    
    def __init__(self, model="Default Car Model", 
                 color="Default Color PlaceHolder", price="$XX,XXX", 
                 year_built="XXXX", model_type="Default Model Type", 
                 drive_type="Default Drive Type", 
                 range_type="Default Range Type", 
                 wheel_type="Default Wheel Type", 
                 interior="Default Interior", 
                 inventory_type="New", charge_time="X hrs"):
        """
        Initializes an instance object of the ElectricCar class. The object's
            ID is appended to the cars list in order to track those that 
            have been built. 

        Args:
            model (str, optional): The model name of the electric car. 
                Defaults to "Default Car Model".
            color (str, optional): The color that the electric car is. 
                Defaults to "Default Color PlaceHolder".
            price (int, optional): How much the electric car costs. 
                Defaults to "$XX,XXX".
            year_built (int, optional): The year the electric car was 
                built in. Defaults to "XXXX".
            model_type (str, optional): The general model type of the 
                electric car (Ex: Sedan, SUV, or Crossover). Defaults 
                to "Default Model Type".
            drive_type (str, optional): The type of drivetrain that the
                electric car has (Ex: AWD, FWD, or RWD). Defaults to 
                "Default Drive Type".
            range_type (str, optional): What type of range that the 
                electric car has (Ex: Standard or long distance). 
                Defaults to "Default Range Type".
            wheel_type (str, optional): What type of wheels that the 
                electric car has (Ex: 18in chrome). Defaults to 
                "Default Wheel Type".
            interior (str, optional): The style of the electric car's 
                interior (Ex: Black Leather). Defaults to "Default Interior".
            inventory_type (str, optional): The inventory status of
                the electric car (Ex: New or used). Defaults to "New".
            charge_time (str, optional): How long it takes the electric
                car to fully charge. Defaults to "X hrs".

        """
        
        if model == None:
            self._model = "Default Car Model PlaceHolder"
        else:
            self._model = model
            
        if color == None:
            self._color = "Default Color PlaceHolder"
        else:
            self._color = color
            
        if price == None:
            self._price = "XX,XXX"
        else:
            self._price = price    
            
        if year_built == None:
            self._year_built = "XXXX"
        else:
            self._year_built = year_built
            
        if model_type == None:
            self._model_type = "Default Model Type"
        else:
            self._model_type = model_type
            
        if drive_type == None:
            self._drive_type = "Default Drive Type"
        else:
            self._drive_type = drive_type
        
        if range_type == None:
            self._range_type = "Default Range Type"
        else:
            self._range_type = range_type 
        
        if wheel_type == None:
            self._wheel_type = "Default Wheel Type"
        else:
            self._wheel_type = wheel_type
        
        if interior == None:
            self._interior = "Default Interior"
        else:
            self._interior = interior
        
        if inventory_type == None:
            self._inventory_type = "New"
        else:
            self._inventory_type = inventory_type
            
        if charge_time == None:
            self._charge_time = "X hrs"
        else:
            self._charge_time = charge_time
            
        self._id_ = id(self)
        
        ElectricCar.cars.append(self._id_)
      
    @classmethod 
    def get_details(cls):
        """
        Returns the essential class attributes for the ElectricCar class.
        """
        string = "Features of all Electric Cars)\n"
        string += f"Energy source: {cls.energy_source}\n"
        string += f"Has touchsreen? {cls.has_touchscreen}\n" 
        string += f"Has caraoke? {cls.has_caraoke}\n" 
        string += f"Has streaming? {cls.has_streaming}\n" 
        string += f"Has internet? {cls.has_internet}"
        
        return string
        
    def remove(car, identification):
        """
        Deletes the specified ElectricCar instance object and
            removes it from the cars list.

        Args:
            car (obj): The car object to delete.
            identification (int): ID needed to confirm this action.

        """
        if car.id_ == identification:
            print(f'Destructor called. Car object {car.color} '
                  f'{car.model} has been deleted')
            del(car)
        else:
            print("Unable to remove ElectricCar object " + 
                  "since ID doesn't exist in list.")
    
    def extra_features(self):
        """
        Returns the additional features of the specified ElectricCar object.
        """
        return(f"Additional feature(s) of this {self.model}, " 
              f"made in {self.year_built}:\n"
              f"Charge time: {self.charge_time}")
        
        
    def drive(self):
        """
        Simulates driving the electric car. 
        
        In doing so, the price of the electric car will decrease, 
            and become used if it was initially new.
            
        """
        price = self.price
        if self.inventory_type.lower() == "new":
            print(f"Driving {self.inventory_type} Electric Car...")
            self._inventory_type = "Used"
            self._price = price * .8
            self._price = '${:,.2f}'.format(self._price)
        else:
            print(f"Driving {self.inventory_type} Electric Car...")
            self._price = price * .9
            self._price = '${:,.2f}'.format(self._price)      
            
    def value_status(self):
        """
        Returns the current value and condition of the electric car.
        """
        price = ElectricCar.convert_price(self.price)
        
        return(f"Electric Car is: {self.inventory_type}\n"
               f"Value is: {price}")
    
    def convert_price(price):
        """
        Returns the price of the electric car in proper currency format.
        """
        if type(price) == int:
            result = '${:,.2f}'.format(price)
        else:
            result = price
            
        return result
        
    def __str__(self):
        """
        Allows the ElectricCar object to be returned from the print 
            function.
         
        Returns:
            string (str): The ID, model, year built, color, price
                model type, drive type, range type, wheel type, interior,
                and inventory type of the electric car specified.

        """
        price = ElectricCar.convert_price(self.price)
        
        string = ("ID: " + str(self._id_) + "\n")
        string += ("Model: " + self._model + "\n")
        string += ("Year built: " + str(self._year_built) + "\n")
        string += ("Color: " + str(self._color) + "\n")
        string += ("Price: " + str(price) + "\n")
        string += ("Model type: " + self._model_type + "\n")
        string += ("Drive type: " + self._drive_type + "\n")
        string += ("Range type: " + str(self._range_type) + "\n")
        string += ("Wheel type: " + str(self._wheel_type) + "\n")
        string += ("Interior: " + self._interior + "\n")
        string += ("Inventory type: " + self._inventory_type)
        
        return string  
    
    @property 
    def model(self):
        """
        Returns the model name of the specified electric car.
        """
        return self._model
    
    @model.setter 
    def model(self, new_model):
        """
        Updates the model name of the specified electric car.
        """
        self._model = new_model 
        
    @property 
    def model_type(self):
        """
        Returns the general model type of the specified electric car.
        """
        return self._model_type 
    
    @model_type.setter 
    def model_type(self, new_type):
        """
        Updates the general model type of the specified electric car.
        """
        self._model_type = new_type
    
    @property 
    def year_built(self):
        """
        Returns the year that the specified electric car was manufactured.
        """
        return self._year_built
    
    @year_built.setter 
    def year_built(self, new_year):
        """
        Updates the year that the specified electric car was manufactured.
        """
        self._year_built = new_year
    
    @property 
    def drive_type(self):
        """
        Returns the drive type of the specified electric car.
        """
        return self._drive_type
    
    @drive_type.setter 
    def drive_type(self, new_type):
        """
        Updates the drive type of the specified electric car.
        """
        self._drive_type = new_type.upper()
    
    @property 
    def range_type(self):
        """
        Returns the range type of the specified electric car.
        """
        return self._range_type 
    
    @range_type.setter 
    def range_type(self, new_type):
        """
        Updates the drive type of the specified electric car.
        """
        self._range_type = new_type
        
    @property 
    def color(self):
        """
        Returns the color of the specified electric car.
        """
        return self._color 
    
    @color.setter 
    def color(self, new_color):
        """
        Updates the color of the specified electric car.
        """
        self._color = new_color
        
    @property 
    def wheel_type(self):
        """
        Returns the drive type of the specified electric car.
        """
        return self._wheel_type
    
    @wheel_type.setter 
    def wheel_type(self, new_type):
        """
        Updates the drive type of the specified electric car.
        """
        self._wheel_type = new_type
        
    @property    
    def interior(self):
        """
        Returns the interior style of the specified electric car.
        """
        return self._interior
    
    @interior.setter 
    def interior(self, new_type):
        """
        Updates the interior style of the specified electric car.
        """
        self._interior = new_type
        
    @property 
    def inventory_type(self):
        """
        Returns the inventory type of the specified electric car.
        """
        return self._inventory_type
    
    @inventory_type.setter 
    def inventory_type(self, new_type):
        """
        Updates the inventory type of the specified electric car.
        """
        self._inventory_type = new_type
    
    @property 
    def charge_time(self):
        """
        Returns the time it takes to charge the specified electric car.
        """
        return self._charge_time 
    
    @charge_time.setter 
    def charge_time(self, new_time):
        """
        Updates the time it takes to charge the specified electric car.
        """
        self._charge_time = new_time
     
    @property 
    def price(self):
        """
        Returns the value of the specified electric car.
        """
        return self._price
    
    @price.setter 
    def price(self, new_price):
        """
        Updates the value of the specified electric car.
        """
        self._price = new_price
     
    @property
    def id_(self):
        """
        Returns the ID of the specified electric car.
        """
        return self._id_
    
    @id_.setter 
    def id_(self, new_id):
        """
        Updates the ID of the specified electric car.
        """
        self._id_ = new_id
     

def main():
    print("***ElectricCar class testing***\n")
    
    print("Class data)")
    print(ElectricCar.get_details())
    
    count = 1
    print("\n---------------------------------")
    print(f"\nCreate ElectricCar object #{count}:")
    print("Without providing arguments)")
    
    e1 = ElectricCar()
    
    print(e1)
    print("\nAfter updating all arguments)")
    
    e1.model = "Nikola Tre Bev"
    e1.color = "Black"
    e1.year_built = 2022
    e1.model_type = "semi-truck"
    e1.drive_type = "awd"
    e1.range_type = "standard"
    e1.wheel_type = "19in Carbon"
    e1.interior = "Slate and White Mesh"
    e1.charge_time = "15 hrs"
    e1.price = 205000
    
    print(e1)
    

    count += 1
    print("\n---------------------------------")
    print(f"\nCreate ElectricCar object #{count}:")
    
    e2 = ElectricCar("GMC Hummer EV", "White", 108700, 2022, "SUV", 
                     "rwd", "long distance", "22in steel", "Auburn Leather", 
                     None, "11 hrs")

    print("See Inventory Status)")
    print(e2.value_status())
    print("After driving)")
    e2.drive()
    print(e2.value_status())
    
    
    count += 1
    print("\n---------------------------------")
    print(f"\nCreate ElectricCar object #{count}:")
    print("Without providing arguments for extra features)")
    
    e3 = ElectricCar()
    print(e3.extra_features())
    
    e3.model = "Nissan LEAF"
    e3.color = "Green"
    e3.year_built = 2020
    e3.model_type = "Compact Hatchback"
    e3.drive_type = "fwd"
    e3.range_type = "economy"
    e3.wheel_type = "17in Machined Grey"
    e3.interior = "Dark Grey Mesh"
    e3.charge_time = "8 hrs"
    
    print("After providing arguments for extra features)")
    print(e3.extra_features())
    
    print("\n---------------------------------")
    print("\nOutput list of Car object IDs")
    print(ElectricCar.cars)
    
    print("\n---------------------------------")
    print(f"\nCall Destructor on {count} objects")
    ElectricCar.remove(e1, e1.id_)
    ElectricCar.remove(e2, e2.id_)
    ElectricCar.remove(e3, e3.id_)


if __name__ == '__main__':
    main()
