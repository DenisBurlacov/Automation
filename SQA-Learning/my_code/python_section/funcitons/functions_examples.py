def my_adder(a, b):
    total = a + b
    return total


total = my_adder(10, 12)
print(total)


def has_no_sales_tax(state):
    state_with_no_tax = ['AK', 'DE', 'MT', 'NH', 'OR']
    not_tax = None
    if state in state_with_no_tax:
        not_tax = True
    else:
        not_tax = False
    return not_tax


result = has_no_sales_tax('DE')
print(result)