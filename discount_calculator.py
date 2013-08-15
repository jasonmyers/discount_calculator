class DiscountCalculator(object):

    def calculate(self, total, discount, discount_type):

        if discount_type == 'percent':
            discount_percent = float(discount)/100
            discount_amount = float(total) * discount_percent
        else:
            discount_amount = discount

        return discount_amount