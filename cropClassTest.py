class Crop:
    """A lovely jubbly class on crops!"""

    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        #SET THE ATTRIBUTES with an INITIAL value

        #Adding UNDERSCORES to each attribute (which is a variable in a class), to indicate that they should be considered private
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"


        #_VARIABLENAME means VARIABLENAME is private
