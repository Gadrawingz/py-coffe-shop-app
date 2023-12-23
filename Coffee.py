class Coffee:
    # Constructor
    def __init__(self, name, price):
        formatted_price = float(price)
        self.name = name
        self.price = formatted_price

    def check_budget(self, budget):
        # Check if the budget is valid
        if not isinstance(budget, (int, float)):
            print('Enter money in float or integer')
            exit()

        if budget < 0:
            print('Sorry you don\'t have money')
            exit()

    def get_change(self, budget):
        return budget - self.price