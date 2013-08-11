class DiscountCalculator(object):

    def calculate(self, total, discount, discount_type):
        discount_percent = float(discount)/100
        discount_amount = float(total) * discount_percent
        return discount_amount