def calc_total_price(discount, price, z = 100):
    print(z)
    if discount == 0:
        return price


    return price * discount


price = input('enter price :')
z = calc_total_price(price=price, discount=2, z=123)
print(z *8)
