"""Convert raw CSV rows into Order objects."""

from analytics.models import Order


def transform_order(row: dict[str, str]) -> Order:
    """
    Transform a raw CSV row into an Order object.

    Args:
        row: A dictionary representing a row from the CSV.

    Returns:
        An Order object.
    """
    return Order(
        order_id=int(row["order_id"]),
        customer=row["customer"],
        category=row["category"],
        amount=float(row["amount"]),
        status=row["status"],
    )
