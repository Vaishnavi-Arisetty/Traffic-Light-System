import sys

from traffic_system.lane import Lane


class FourWayJunction:

    def __init__(self):
        self.lane_one = Lane()
        self.lane_one.lane_name = "Lane 1"
        self.lane_two = Lane()
        self.lane_two.lane_name = "Lane 2"
        self.lane_three = Lane()
        self.lane_three.lane_name = "Lane 3"
        self.lane_four = Lane()
        self.lane_four.lane_name = "Lane 4"
        self.automatic_system_on = True

    def on_four_way_junction_signal(self):
        """
        This method switches on the four way junction signal.

        :return: returns the string returned from the automatic signal function.
        """
        self.automatic_system_on = True
        print("Turned on the four way junction signal")
        return self.automatic_signal()

    def off_four_way_junction_signal(self):
        """
        This method switches off the four way junction switch.
        """
        self.automatic_system_on = False
        print("Turned off the four way junction signal")
        sys.exit()

    def automatic_signal(self):
        """
        This method operates the signal for each lane sequentially.

        :return: returns a string that says operation is done.
        """
        four_lanes = [self.lane_one, self.lane_two, self.lane_three, self.lane_four]

        if self.automatic_system_on:
            for lane in four_lanes:
                print(lane.lane_name)
                lane.operate_lane_signal()

        return "Automatic Signal Operation is done"
