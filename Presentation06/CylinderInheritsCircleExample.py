import math

class Circle:
    '''
    This class contains information about a circle.
    '''

    radius: float  # This attribute represents the radius of the circle. It is expected to be a float.

    def __init__(self, radius):
        '''
        This is the constructor method for the Circle class.
        It initializes the radius of the circle to the provided value.

        Parameters:
        radius (float): The radius of the circle
        '''
        self.radius = radius

    def getArea(self):
        '''
        This method calculates and returns the surface area of the circle.

        Returns:
        float: The surface area of the circle (in square meters)
        '''
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        '''
        This method calculates and returns the circumference of the circle.

        Returns:
        float: The circumference of the circle (in meters)
        '''
        return 2 * math.pi * self.radius

class Cylinder(Circle):
    '''
    This class contains information about a cylinder.
    '''

    height: float

    def __init__(self, radius: float, height: float):
        '''
        The constructor method for the Cylinder class.
        It initializes the radius of the base and the height of the cylinder.

        Parameters:
        radius (float): The radius of the cylinder's base
        height (float): The height of the cylinder
        '''
        super().__init__(radius)  # Initialize the radius using the Circle's constructor
        self.height = height

    def getArea(self):
        '''
        This method calculates and returns the total surface area of the cylinder.

        Returns:
        float: The total surface area of the cylinder (in square meters)
        '''
        lateral_surface_area = 2 * math.pi * self.radius * self.height  # Lateral surface area
        base_area = 2 * super().getArea()  # Area of two bases
        return lateral_surface_area + base_area

    def getVolume(self):
        '''
        This method calculates and returns the volume of the cylinder.

        Returns:
        float: The volume of the cylinder (in cubic meters)
        '''
        return super().getArea() * self.height

    def getCircumference(self):
        '''
        Raises an exception if someone tries to call getCircumference on a cylinder.
        '''
        raise NotImplementedError("A cylinder doesn't have a single circumference. This method is not applicable.")


if __name__ == "__main__":
    circle = Circle(radius=2.0)  # Creating an instance of Circle class with radius 2
    print(f"Circle's Radius is {circle.radius} meter")  # Printing the radius of the circle
    print(f"Circle's Area is {circle.getArea():.2f} square meters")  # Printing the area of the circle
    print(f"Circle's Circumference is {circle.getCircumference():.2f} meters")  # Printing the circumference of the circle

    cylinder = Cylinder(radius=2.0, height=4.0)  # Creating a Cylinder instance
    print(f"Cylinder's height is {cylinder.height:.2f} meters")  # Printing the height of the cylinder
    print(f"Cylinder's Volume is {cylinder.getVolume():.2f} cubic meters")  # Printing the volume of the cylinder
    print(f"Cylinder's Total Surface Area is {cylinder.getArea():.2f} square meters")  # Printing the total surface area of the cylinder

    try:
        # Attempting to call getCircumference on a Cylinder will raise an exception
        print(f"Cylinder's Circumference is {cylinder.getCircumference():.2f} meters")
    except NotImplementedError as e:
        print(e)


'''
UML Class Relation Diagram 
  Online Viewer: https://www.planttext.com/
  
@startuml
skinparam roundcorner 20

class Circle {
    + radius: float
    + __init__(radius: float)
    + getArea(): float
    + getCircumference(): float
}

class Cylinder {
    + height: float
    + __init__(radius: float, height: float)
    + getArea(): float
    + getVolume(): float
    + getCircumference(): NotImplementedError
}

Circle <|-- Cylinder

@enduml
'''