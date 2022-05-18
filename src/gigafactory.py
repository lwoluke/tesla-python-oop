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
    
    total_cars = 19000
    """
    total_cars (int): (class attribute) The current total number of cars 
        that have been built at the factory.
    """
    
    model3_cars = 8553
    """
    model3_cars (int): (class attribute) The current total number of 
        Model 3 cars that have been built at the factory.
    """
    
    modelY_cars = 3598
    """
    model3_cars (int): (class attribute) The current total number of 
        Model 3 cars that have been built at the factory.
    """
    
    modelS_cars = 1939
    """
    modelS_cars (int): (class attribute) The current total number of 
        Model S cars that have been built at the factory.
    """
    
    modelX_cars = 4910
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

        Updates the list of the GigaFactory object by adding Tesla car 
            objects to the list to relfect these changes.

        Args:
            model (str): The name of the Tesla car model to build.
            batch_size (int, optional): How many cars of that 
                particular model name that will be built. Defaults to 1.

        Returns:
            str: Message explaining whether the batch of the specified
                Tesla model was able to built successfully.

        """
        if model.lower() == "model3":
            print(f"Building Model3 Batch of Size {batch_size}...")
            
            for i in range(batch_size):
                self._manufactured_cars.append(Model3())
                GigaFactory.model3_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
                
            return f'Successfully built {batch_size} Model 3 car(s)'
            
        elif model.lower() == "models":
            print(f"Building ModelS Batch of Size {batch_size}...")
            
            for i in range(batch_size):
                self._manufactured_cars.append(ModelS())
                GigaFactory.modelS_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
                
            return f'Successfully built {batch_size} Model S car(s)'
            
        elif model.lower() == "modelx":
            print(f"Building ModelX Batch of Size {batch_size}...")
            
            for i in range(batch_size):
                self._manufactured_cars.append(ModelX())
                GigaFactory.modelX_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
                
            return f'Successfully built {batch_size} Model X car(s)'
            
        elif model.lower() == "modely":
            print(f"Building ModelY Batch of Size {batch_size}...")
            
            for i in range(batch_size):
                self._manufactured_cars.append(ModelY())
                GigaFactory.modelY_cars += 1
                GigaFactory.total_cars += 1
                self._production_size += 1
                
            return f'Successfully built {batch_size} Model Y car(s)'
        
        else:
            return(f"The {model} isn't a car that Tesla has, "
                   "or hasn't become ready for production yet.")
            
    def sell(self, model, amt_to_sell):
        """
        Sells a specified number of a particular car model. If there aren't 
            any cars of that model name in the instance list, or there 
            are more that are requested to be sold then exist in the instance
            list, an error message will appear.
        
        Updates the list of the GigaFactory object by removing Tesla car 
            objects from the list to relfect these changes.

        Args:
            model (str): The model name of the Tesla car that will be sold.
            amt_to_sell (int): How many cars of that particular Tesla model
                to sell.

        Returns:
            str: Message explaining whether the amount of the specified
                Tesla model was able to sell successfully.

        """
        amt_sold = 0
        
        if model.lower() == "model3":
            print(f"Selling {amt_to_sell} Model 3 cars...")
            
            for i in reversed(range(len(self.manufactured_cars))):
                
                if amt_sold == amt_to_sell:
                    return f'Successfully sold {amt_to_sell} Model 3 car(s)'
                
                if isinstance(self.manufactured_cars[i], Model3):
                    del self.manufactured_cars[i]
                    GigaFactory.model3_cars -= 1
                    GigaFactory.total_cars -= 1
                    self._production_size -= 1
                    amt_sold += 1
                    
            return f'Unable to sell {amt_to_sell} Model 3 car(s)'
            
        elif model.lower() == "models":
            print(f"Selling {amt_to_sell} Model S cars...")
            
            for i in reversed(range(len(self.manufactured_cars))):
                
                if amt_sold == amt_to_sell:
                    return f'Successfully sold {amt_to_sell} Model S car(s)'
                
                if isinstance(self.manufactured_cars[i], ModelS):
                    del self.manufactured_cars[i]
                    GigaFactory.modelS_cars -= 1
                    GigaFactory.total_cars -= 1
                    self._production_size -= 1
                    amt_sold += 1
                    
            return f'Unable to sell {amt_to_sell} Model S car(s)'
            
        elif model.lower() == "modelx":
            print(f"Selling {amt_to_sell} Model X cars...")
            
            for i in reversed(range(len(self.manufactured_cars))):
                
                if amt_sold == amt_to_sell:
                    return f'Successfully sold {amt_to_sell} Model X car(s)'
                
                if isinstance(self.manufactured_cars[i], ModelX):
                    del self.manufactured_cars[i]
                    GigaFactory.modelX_cars -= 1
                    GigaFactory.total_cars -= 1
                    self._production_size -= 1
                    amt_sold += 1
                    
            return f'Unable to sell {amt_to_sell} Model X car(s)'
            
        elif model.lower() == "modely":
            print(f"Selling {amt_to_sell} Model Y cars...")
            
            for i in reversed(range(len(self.manufactured_cars))):
                
                if amt_sold == amt_to_sell:
                    return f'Successfully sold {amt_to_sell} Model Y car(s)'
                
                if isinstance(self.manufactured_cars[i], ModelY):
                    del self.manufactured_cars[i]
                    GigaFactory.modelY_cars -= 1
                    GigaFactory.total_cars -= 1
                    self._production_size -= 1
                    amt_sold += 1
                    
            return f'Unable to sell {amt_to_sell} Model Y car(s)'
        
        else:
            return(f"The {model} isn't a car that Tesla has, "
                  "or hasn't become ready for production yet.")
    
    def remove(self, obj):
        """
        Deletes the specified Tesla car instance object and
            removes it from the cars list.

        Args:
            obj (int): The specified object to delete.

        """   
        if obj in self.manufactured_cars:
            index = self.manufactured_cars.index(obj)
            print('Destructor called. Tesla car object ' \
                  'has been deleted')
            del self.manufactured_cars[index]
            
        else:
            print("Unable to remove Tesla car object " + 
                  "since object doesn't exist in list.")  
      
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
        return (f"Percentage of Model3: {cls.model3_ratio()}%\n" 
                f"Percentage of ModelS: {cls.modelS_ratio()}%\n"
                f"Percentage of ModelX: {cls.modelX_ratio()}%\n"
                f"Percentage of ModelY: {cls.modelY_ratio()}%\n")
    
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
        
        net_m3 = (after_m3 - before_m3)
        net_ms = (after_ms - before_ms)
        net_mx = (after_mx - before_mx)
        net_my = (after_my - before_my)
        
        net_m3 = '%.3f' % round(net_m3, 3)
        net_ms = '%.3f' % round(net_ms, 3)
        net_mx = '%.3f' % round(net_mx, 3)
        net_my = '%.3f' % round(net_my, 3)
        
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
    
    print(GigaFactory.production_ratio())
    
    print("\nCreate GigaFactory object:")
    
    g = GigaFactory()
    
    model3_build_amt = 2
    modelS_build_amt = 6
    modelX_build_amt = 10
    modelY_build_amt = 20
    
    print(g.build("model3", model3_build_amt))
    print(g.build("models", modelS_build_amt))
    print(g.build("modelx", modelX_build_amt))
    print(g.build("modely", modelY_build_amt))
    
    print()
    print(g.manufactured_cars)
    
    print("\nUpdated Production Ratios)")
    
    after_m3 = float(GigaFactory.model3_ratio())
    after_ms = float(GigaFactory.modelS_ratio())
    after_mx = float(GigaFactory.modelX_ratio())
    after_my = float(GigaFactory.modelY_ratio())
    list2 = [after_m3, after_ms, after_mx, after_my]
    
    print(GigaFactory.production_ratio())
    
    print("Percentage Change in Production Ratios)")
    
    print(GigaFactory.net_change_ratios(list1, list2))
    
    print("\nSelling Cars)")
    print("Amount to sell for each model:")
    
    model3_sell_amt = 5
    modelS_sell_amt = 2
    modelX_sell_amt = 11
    modelY_sell_amt = 8
    
    print(f"Model 3: {model3_sell_amt}")
    print(f"Model S: {modelS_sell_amt}")
    print(f"Model X: {modelX_sell_amt}")
    print(f"Model Y: {modelY_sell_amt}\n")
    
    print("Won't be able to sell the desired amount of Model 3 cars.")
    print(g.sell("model3", model3_sell_amt))
    print()
    
    print("Will be able to sell the desired amount of Model S cars.")
    print(g.sell("models", modelS_sell_amt))
    print()
    
    print("Won't be able to sell the desired amount of Model X cars.")
    print(g.sell("modelx", modelX_sell_amt))
    print()
    
    print("Will be able to sell the desired amount of Model Y cars.")
    print(g.sell("modely", modelY_sell_amt))
    
    print("\nUpdated Production Ratios)")
    
    after_m3 = float(GigaFactory.model3_ratio())
    after_ms = float(GigaFactory.modelS_ratio())
    after_mx = float(GigaFactory.modelX_ratio())
    after_my = float(GigaFactory.modelY_ratio())
    list3 = [after_m3, after_ms, after_mx, after_my]
    
    print(GigaFactory.production_ratio())
    
    print("Percentage Change in Production Ratios from Initial Production "
          "Ratios)")
    
    print(GigaFactory.net_change_ratios(list1, list3))
    
    print("\nCall Destructor on GigaFactory object:")
    del(g)
    

if __name__ == '__main__':
    main()
