from pricing import get_net_price

price = 200
tax_rate = 0.075
discount = 5

net_price = get_net_price(
    price,
    tax_rate,
    discount
)

print(net_price)
