class ShoppingCart:
    
    # write your code here
    def __init__(self, total=0, emp_discount=None, items=[]):
        self.total = total
        self.employee_discount = emp_discount
        self.items = items
    
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total

    def mean_item_price(self):
        num_items = len(self.items)
        mean = self.total / num_items
        return mean

    def median_item_price(self):
        prices = [item["price"] for item in self.items]
        num_items = len(prices)
        if (num_items%2 == 0):
            mid_high = int(num_items / 2)
            mid_low = mid_high - 1
            median = (prices[mid_high] + prices[mid_low]) / 2
            return median
        mid_odd = int(num_items / 2)
        median = prices[mid_odd]
        return median

    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount / 100
            discounted_total = self.total * (1-discount)
            return discounted_total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()  
            self.total -= removed_item['price']
        else:
            return "There are no items in your cart!"
        return self.total
        