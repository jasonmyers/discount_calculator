class DiscountCalculator(object):

    def calculate(self, total, discount, discount_type):

        if discount_type == 'percent':
            discount_percent = float(discount)/100
            discount_amount = float(total) * discount_percent
        elif discount_type == 'absolute':
            discount_amount = discount
        else:
            raise ValueError("Invalid Discount Type")

        return discount_amount