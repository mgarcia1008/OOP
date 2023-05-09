class Car:
    # class attributes
    wheels = 4
    doors = 2


    # constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    # instance method
    def start(self):
        print("The car is starting...")


    # instance method
    def stop(self):
        print("The car is stopping...")


    # instance method
    def drive(self):
        print("The car is driving...")


# create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2021) #instance is my_car (inside here are the attributes)


# access instance attributes
print(my_car.make) # output: Toyota
print(my_car.model) # output: Corolla
print(my_car.year) # output: 2021


# call instance methods
my_car.start() # output: The car is starting...
my_car.drive() # output: The car is driving...
my_car.stop() # output: The car is stopping...
#In this example, the Car class has three attributes: wheels, doors, and make, model, and year
# that are instance attributes. The class also has three methods: start(), stop(), and drive().


#To create an instance of the Car class, we use the constructor method __init__() to pass
# in the make, model, and year of the car. We then call the instance methods on the
# my_car object to perform actions on the car instance.


#in Python, self is a special parameter that is used within class methods to refer to the
#instance of the class on which the method is called. It allows us to access and modify the
# attributes of the instance.


#When we define a class method, we need to include the self parameter as the first parameter
# in the method definition. This is a convention, and self can be named anything,
# but it is recommended to use self for clarity and consistency.


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


    def bark(self):
        print(f"{self.name} is barking.")


# create an instance of Dog class
my_dog = Dog("Rex", "Labrador")


# access instance attributes
print(my_dog.name) # output: Rex
print(my_dog.breed) # output: Labrador


# call instance method
my_dog.bark() # output: Rex is barking.


#In this example, we define a Dog class with a constructor method __init__() that takes two
#parameters: name and breed. The self parameter is used to assign the values of name and
# breed to the instance variables self.name and self.breed.


#We also define a bark() method that prints a message indicating that the dog is barking.
#Notice that we use self.name in the bark() method to access the name of the instance of the
# Dog class.


#Finally, we create an instance of the Dog class and call the bark() method on the instance.
#When we call my_dog.bark(), self refers to the my_dog instance of the Dog class,
#so the output is "Rex is barking."
