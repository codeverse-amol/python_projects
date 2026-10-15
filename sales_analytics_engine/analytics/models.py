"""Define the Order model."""

from dataclasses import dataclass



@dataclass
class Order:
    order_id: int
    customer : str
    category : str
    amount : float
    status : str
