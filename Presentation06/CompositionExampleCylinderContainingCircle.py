import math

class Circle:
    '''
      This class contains information about a circle.
    '''

    radius : float   # This attribute represents the radius of the circle. It is expected to be a float.

    def __init__(self, radius):
        '''
        This is the constructor method for the Circle class.
        It initializes the radius of the circle to the provided value.

        Parameters:
        radius (float): The radius of the circle
        '''
        self.radius=radius

    def getArea(self):
        '''
        This method calculates and returns the surface area of the circle.

        Returns:
        float: The surface area of the circle (could be in square meters)
        '''
        return math.pi * self.radius*self.radius

    def getCircumference(self):
        '''
        This method calculates and returns the circumference of the circle.

        Returns:
        float: The circumference of the circle (could be in meters)
        '''
        return 2*math.pi  * self.radius

class Cylinder:
    '''
      This class contains information about a cylinder.
    '''

    circularBase : Circle
    height : float

    def __init__(self, height: float,circularBase: Circle):
        '''
        The constructor method for the Cylinder class.
        It initializes the base and height of the cylinder to the provided values.

        Parameters:
        base (Circle): The base of the cylinder
        height (float): The height of the cylinder
        '''
        self.circularBase = circularBase
        self.height = height

    def getVolume(self):
        '''
        This method calculates and returns the volume of the cylinder.

        Returns:
        float: The volume of the cylinder (could be in cubic meters)
        '''
        return self.circularBase.getArea() * self.height

    def getArea(self):
        '''
        This method calculates and returns the total surface area of the cylinder.

        Returns:
        float: The total surface area of the cylinder (in square meters)
        '''
        lateral_surface_area = self.circularBase.getCircumference() * self.height  # Lateral surface area
        base_area = 2 * self.circularBase.getArea()                                # Area of two bases
        return lateral_surface_area + base_area


if __name__ == "__main__":
    circle=Circle(radius=2.0)  # Creating an instance of Circle class with radius 2
    print(f"Circle's Radius is {circle.radius} meter")  # Printing the radius of the circle
    print(f"Circle's Area is  {circle.getArea():.2f} square meter")  # Printing the area of the circle

    cylinder=Cylinder(height=4.0,circularBase=Circle(radius=2.0))
    print(f"My Cylinder's variables is: {cylinder.__dict__}")
    print(f"Cylinders's height is  {cylinder.height:.2f}  meter")  # Printing the height of the cylinder
    print(f"Cylinders's Volume is  {cylinder.getVolume():.2f}  meter**3")  # Printing the Volume of the Cylinder
    print(f"Cylinder's Total Surface Area is {cylinder.getArea():.2f} square meters")  # Printing the total surface area of the cylinder
    print(f"Cylinders's base radius is  {cylinder.circularBase.radius:.2f}  meter")  # Printing the height of the cylinder
    print(f"Cylinders's base Area is  {cylinder.circularBase.getArea():.2f} square meter")  # Printing the area of the circle

'''
UML Class Relation Diagram 
  Online Viewer: https://www.planttext.com/

@startuml

skinparam RoundCorner 20

top to bottom direction

class Circle {
  +radius : float
  +__init__(radius: float)
  +getArea() : float
  +getCircumference() : float
}

class Cylinder {
  +circularBase : Circle
  +height : float
  +__init__(height: float, circularBase: Circle)
  +getArea() : float
  +getVolume() : float
}

Circle *-- Cylinder : circularBase

@enduml


'''