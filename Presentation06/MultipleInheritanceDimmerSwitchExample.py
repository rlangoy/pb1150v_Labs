class LightSwitch():
    __switchIsOn = None

    def __init__(self):
        self.turnOff()

    def turnOn(self):
        print("Switch is on")
        self.__switchIsOn = True

    def turnOff(self):
        print("Switch is off")
        self.__switchIsOn = False


class LighDimmerSwitch(LightSwitch):
    __level = None

    def __init__(self):
        super().__init__()  # Call Base Constructor
        self.__level = 0

    def leveUp(self):
        if (self.__level < 99):
            self.__level += 1

    def leveDown(self):
        if (self.__level > 1):
            self.__level -= 1


if __name__ == "__main__":
    oSwitch = LightSwitch()
    oSwitch.turnOn()

    oDimmerSwitch = LighDimmerSwitch()
    oDimmerSwitch.turnOn()
    oDimmerSwitch.leveUp()
    oDimmerSwitch.leveUp()
    print(oDimmerSwitch.__dict__)

# !@# osv...
#  oDimmerSwitch.__switchIsOn=True
#  print(f"oSwitch.switchIsOn = {oDimmerSwitch.__switchIsOn}")
