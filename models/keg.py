class Keg:
    def __init__(self,beer,fill,capacity,purchase_cost,selling_price, id=None):
        self.beer = beer
        self.fill_level = fill
        self.capacity = capacity
        self.cost = purchase_cost
        self.price = selling_price
        self.id = id
    
    def sell_pint(self):
        self.fill_level -= 1