class Signal:

    def __init__(self):
        self.red_light = False
        self.yellow_light = False
        self.green_light = False

    def turn_on_green(self):
        """
        This method switches off the red signal and turns on the green signal.
        """
        self.turn_off_red()
        self.green_light = True
        print("Green is on")

    def turn_on_red(self):
        """
        This method switches off the yellow signal and turns on the red signal.
        """
        self.turn_off_yellow()
        self.red_light = True
        print("Red is on")

    def turn_on_yellow(self):
        """
        This method switches off the green signal and turns on the yellow signal.
        """
        self.turn_off_green()
        self.yellow_light = True
        print("Yellow is on")

    def turn_off_green(self):
        """
        This method switches off the green signal.
        """
        self.green_light = False

    def turn_off_red(self):
        """
        This method switches off the red signal.
        """
        self.red_light = False

    def turn_off_yellow(self):
        """
        This method switches off the yellow signal.
        """
        self.yellow_light = False
