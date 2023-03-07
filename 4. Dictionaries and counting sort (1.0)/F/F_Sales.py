def output_customers(lines):
    customers = {}
    for line in lines:
        customer, product, amount = line.split()
        if customer not in customers:
            customers[customer] = {}
        if product not in customers[customer]:
            customers[customer][product] = 0
        customers[customer][product] += int(amount)

    for customer in sorted(customers.keys()):
        print(f"{customer}:")
        for product in sorted(customers[customer].keys()):
            print(f"{product} {customers[customer][product]}")


if __name__ == "__main__":
    lines = []
    with open("input.txt") as f:
        lines = f.readlines()

    output_customers(lines)
