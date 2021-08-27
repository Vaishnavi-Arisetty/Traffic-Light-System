import pytest

from traffic_system.four_way_junction import FourWayJunction


class TestFourWayJunction:

    four_way_junction = FourWayJunction()

    def test_automatic_signal(self):
        assert self.four_way_junction.automatic_signal() == "Automatic Signal Operation is done"

    def test_on_four_way_junction_signal(self):
        assert self.four_way_junction.on_four_way_junction_signal() == "Automatic Signal Operation is done"

