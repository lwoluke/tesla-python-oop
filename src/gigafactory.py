# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:37:57 2022

@author: lwolu
"""


# Python file(s)
from model_3 import Model3
from model_s import ModelS 
from model_x import ModelX 
from model_y import ModelY
from electric_car import ElectricCar


class GigaFactory(ElectricCar):
    
    location = "Austin, Texas"
    """
    location (str): (class attribute) Where the factory is located.
    """
    
    built = "2020-2022"
    """
    built (str): (class attribute) Time period of when the factory was built.
    """
    
    area = "3.3 sq miles"
    """
    area (str): (class attribute) The size of the factory in square miles.
    """
    
    owner = "Tesla"
    """
    owner (str): (class attribute) Who owns the factory.
    """
    
    total_cars = 125000
    """
    total_cars (int): (class attribute) The current total number of cars 
        that have been built at the factory.
    """
    
    model3_cars = 92500
    """
    model3_cars (int): (class attribute) The current total number of 
        Model 3 cars that have been built at the factory.
    """
    
    modelY_cars = 12000
    """
    model3_cars (int): (class attribute) The current total number of 
        Model 3 cars that have been built at the factory.
    """
    
    modelS_cars = 5000
    """
    modelS_cars (int): (class attribute) The current total number of 
        Model S cars that have been built at the factory.
    """
    
    modelX_cars = 10500
    """
    modelX_cars (int): (class attribute) The current total number of 
        Model X cars that have been built at the factory.
    """
    
    def __init__(self, production_size=0):
        """
        Initializes an instance object of the GigaFactory class. 

        Args:
            production_size (int, optional): The number of cars that 
                have been produced in this production cycle. Defaults 
                to 0.

        """
        
        if production_size == None:
            self._production_size = 0
        else:
            self._production_size = production_size
            
        self._manufactured_cars = []
    
    def build(self, model, batch_size=1):
        """
        Produces a specified number of cars for a particular Tesla 
            car model.

        Args:
            model (TYPE): The name of the Tesla car model to build.
            batch_size (TYPE, optional): How many cars of that 
                particular model name that will be built. Defaults to 1.
                
        """
        if model.lower() == "model3":
            print(f"Building Model3 Batch of Size {batch_size}...")
            for i in range(batch_size):
                self._manufactured_cars.append(Model3())
                GigaFactory.model3_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
            
        elif model.lower() == "models":
            print(f"Building ModelS Batch of Size {batch_size}...")
            for i in range(batch_size):
                self._manufactured_cars.append(ModelS())
                GigaFactory.modelS_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
            
        elif model.lower() == "modelx":
            print(f"Building ModelX Batch of Size {batch_size}...")
            for i in range(batch_size):
                self._manufactured_cars.append(ModelX())
                GigaFactory.modelX_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
            
        elif model.lower() == "modely":
            print(f"Building ModelY Batch of Size {batch_size}...")
            for i in range(batch_size):
                self._manufactured_cars.append(ModelY())
                GigaFactory.modelY_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
        
        else:
            print(f"The {model} isn't a car that Tesla has, "
                  "or hasn't become ready for production yet.")
            
      
    def remove(self, arr, identification):
        """
        Deletes the specified ElectricCar instance object and
            removes it from the cars list.

        Args:
            arr (TYPE): The ElectricCar object to delete.
            identification (TYPE): ID needed to confirm this action.

        """   
        if identification in arr:
            index = arr.index(identification)
            print('Destructor called. ElectricCar object ' \
                  'has been deleted')
            del(arr[index])
            
        else:
            print("Unable to remove ElectricCar object " + 
                  "since ID doesn't exist in list.")  
      
    @classmethod 
    def get_details(cls):
        """
        Returns the essential class attributes for the GigaFactory class.
        """
        return (f"{cls.owner } GigaFactory"
                f"Located in: {cls.location}"
                f"Size: {cls.area}" 
                f"Total Cars Built: {cls.total_cars}")
        
    @classmethod 
    def model3_ratio(cls):
        """
        Returns the ratio of Model 3 cars that have been produced in 
            relation to total electric cars.
        """
        model3_ratio = cls.model3_cars / cls.total_cars * 100
        return '%.3f' % round(model3_ratio, 3)
        
    @classmethod 
    def modelS_ratio(cls):
        """
        Returns the ratio of Model S cars that have been produced in 
            relation to total electric cars.
        """
        modelS_ratio = cls.modelS_cars / cls.total_cars * 100
        return '%.3f' % round(modelS_ratio, 3)
        
    @classmethod 
    def modelX_ratio(cls):
        """
        Returns the ratio of Model X cars that have been produced in 
            relation to total electric cars.
        """
        modelX_ratio = cls.modelX_cars / cls.total_cars * 100
        return '%.3f' % round(modelX_ratio, 3)
        
    @classmethod 
    def modelY_ratio(cls):
        """
        Returns the ratio of Model Y cars that have been produced in 
            relation to total electric cars.
        """
        modelY_ratio = cls.modelY_cars / cls.total_cars * 100
        return '%.3f' % round(modelY_ratio, 3)
    
    @classmethod 
    def production_ratio(cls):
        """
        Returns the ratio of each electric car model that has been 
            produced in relation to total electric cars.
        """
        return (f"Percentage of Model3: {cls.model3_ratio()}%" 
                f"Percentage of ModelS: {cls.modelS_ratio()}"
                f"Percentage of ModelX: {cls.modelX_ratio()}"
                f"Percentage of ModelY: {cls.modelY_ratio()}")
    
    @staticmethod 
    def net_change_ratios(list1, list2):
        """
        Calculates the net change in the ratios of each car model 
            produced versus the total number of cars produced.
            
        Both of the list arguments passed into the method should 
            be of size 4, since there are 4 different car models
            that Tesla produces.

        Args:
            list1 (list[float]): The initial ratios of each of the 
                car models produced.
            list2 (list[float]): The updated ratios of each of the 
                car models produced.

        Returns:
            str: The net change in each of the car model ratios.

        """
        if len(list1) != 4 or len(list2) != 4:
            return 'Unable to calculate the net change of each car model.'
        
        before_m3 = list1[0]
        before_ms = list1[1]
        before_mx = list1[2]
        before_my = list1[3]
        after_m3 = list2[0]
        after_ms = list2[1]
        after_mx = list2[2]
        after_my = list2[3]
        
        net_m3 = (after_m3 - before_m3) * 100
        net_ms = (after_ms - before_ms) * 100
        net_mx = (after_mx - before_mx) * 100
        net_my = (after_my - before_my) * 100
        
        net_m3 = '%.2f' % round(net_m3, 2)
        net_ms = '%.2f' % round(net_ms, 2)
        net_mx = '%.2f' % round(net_mx, 2)
        net_my = '%.2f' % round(net_my, 2)
        
        return (f"Model3: {net_m3}%\n"
                f"ModelS: {net_ms}%\n" 
                f"ModelX: {net_mx}%\n"
                f"ModelY: {net_my}%")
                
    @property 
    def manufactured_cars(self):
        """
        Returns the list of cars that have been built in 
            this particular GigaFactory production cycle.
        """
        return self._manufactured_cars
    
    @manufactured_cars.setter 
    def manufactured_cars(self, arr):
        """
        Updates the list of cars that have been built in 
            this particular GigaFactory production cycle.
        """
        self._manufactured_cars = arr
        
    def __del__(self):
        """
        Allows the GigaFactory object to be deleted from the del statement.
        """
        print('Destructor called. GigaFactory object has been deleted')
    
    
def main():
    print("***GigaFactory class testing***\n")
    
    print("\nInitial Production Ratios)")
    
    before_m3 = float(GigaFactory.model3_ratio())
    before_ms = float(GigaFactory.modelS_ratio())
    before_mx = float(GigaFactory.modelX_ratio())
    before_my = float(GigaFactory.modelY_ratio())
    list1 = [before_m3, before_ms, before_mx, before_my]
    
    GigaFactory.production_ratio()
    
    print("\nCreate GigaFactory object:")
    
    g = GigaFactory()
    g.build("model3")
    g.build("models", 25)
    g.build("modelx", 3)
    g.build("modely", 2)
    
    print()
    print(g.manufactured_cars)
    
    print("\nUpdated Production Ratios)")
    
    after_m3 = float(GigaFactory.model3_ratio())
    after_ms = float(GigaFactory.modelS_ratio())
    after_mx = float(GigaFactory.modelX_ratio())
    after_my = float(GigaFactory.modelY_ratio())
    list2 = [after_m3, after_ms, after_mx, after_my]
    
    GigaFactory.production_ratio()
    
    print("\nPercentage Change in Production Ratios)")
    
    print(GigaFactory.net_change_ratios(list1, list2))
    
    print("\nCall Destructor on GigaFactory object:")
    del(g)
    

if __name__ == '__main__':
    main()
