class Virus(object):
    '''
    Virus objects will infect persons

    _____Attributes______:

    name: String: Contains virus name.

    infection_rate: Float. The chance that the virus spreads to a new human.

    mortality_rate: Float. The chance that the virus kills the host.

    _____Methods_____:

    __init__(self, name, infection_rate, kill_rate)
        -All parameters should be set to the passed value.
    '''

    def __init__(self, name, infection_rate, mortality_rate):
        self.name = name
        self.infection_rate = infection_rate
        self.mortality_rate = mortality_rate
