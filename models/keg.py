class Keg:
    def __init__(self,beer,capacity, id=None):
        self.beer = beer
        self.fill_level = capacity
        self.capacity = capacity
        self.id = id