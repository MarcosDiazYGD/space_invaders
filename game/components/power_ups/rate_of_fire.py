from game.components.power_ups.power_up import PowerUp
from game.utils.constants import RATE_OF_FIRE, RATE_OF_FIRE_TYPE


class Rate_Of_Fire(PowerUp):
    def __init__(self):
        super().__init__(RATE_OF_FIRE, RATE_OF_FIRE_TYPE)
