class DiscountCalculator(object):

    def calculate(self, total, discount, discount_type):
        if discount_type == 'percent':
            if discount > 100:
                raise ValueError("Discount % cannot be greater than 100%")
            discount_percent = float(discount)/100
            discount_amount = float(total) * discount_percent
        elif discount_type == 'absolute':
            if discount > total:
                raise ValueError("Absolute Discount cannot be greater than amount")
            discount_amount = discount
        else:
            raise ValueError("Invalid Discount Type")

        return discount_amount