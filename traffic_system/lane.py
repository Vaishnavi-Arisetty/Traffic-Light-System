import time

from traffic_system.signal import Signal


class Lane:
    lane_name = ""

    def __init__(self):
        self.signal = Signal()

    def operate_lane_signal(self):
        """
        This method operates the signal for this lane
        """
        self.signal.turn_on_green()
        time.sleep(7)
        self.signal.turn_on_yellow()
        time.sleep(4)
        self.signal.turn_on_red()
        time.sleep(2)
