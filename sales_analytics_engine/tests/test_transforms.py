from analytics.models import Order
from analytics.transforms import transform_order

raw_row = {
    "order_id": "1001",
    "customer": "Alice Johnson",
    "category": "Electronics",
    "amount": "2499.99",
    "status": "Completed",
}

order = transform_order(raw_row)

# Check the returned object
assert isinstance(order, Order)

# Check field values and types
assert order.order_id == 1001
assert isinstance(order.order_id, int)

assert order.amount == 2499.99
assert isinstance(order.amount, float)

assert order.customer == "Alice Johnson"
assert order.category == "Electronics"
assert order.status == "Completed"

print("All transformation tests passed!")
print(order)