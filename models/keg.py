class Keg:
    def __init__(self,beer,capacity,purchase_cost,selling_price, id=None):
        self.beer = beer
        self.fill_level = capacity
        self.capacity = capacity
        self.cost = purchase_cost
        self.price = selling_price
        self.id = id