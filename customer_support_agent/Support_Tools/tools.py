from langchain_core.tools import tool
import random
import string
@tool
def create_ticket(
    customer_id: str,
    order_id: str,
    ticket_type: str,
    description: str,
    item_id: int | None = None
):
    """
    Create a customer support ticket.

    Args:
        order_id: Related order ID.
        ticket_type: Type of support request.
        description: Description of the customer's issue.
        item_id: Optional item ID related to the ticket.
    """
    ticket_id = 'TCK'+ ''.join(
        random.choices(string.digits, k=4)
    )



@tool
def update_ticket(
    ticket_id: str,
    status: str | None = None,
    priority: str | None = None,
    description: str | None = None
):
    """
    Update an existing support ticket.

    Args:
        ticket_id: Ticket ID.
        status: New ticket status.
        priority: New priority.
        description: Updated ticket description.
    """

@tool
def get_ticket(ticket_id: str):
    """
    Tool to get ticket based on the id
    Args:
        ticket_id: id used to fetch ticket data to view status support estimation etc
    """

@tool
def process_refund(order_id: str):
    """
    Initiate a refund for an eligible order.
    """

@tool
def cancel_order(order_id: str, item_id: int | None = None):
    """
    Cancel an order or a specific item if cancellation is allowed.

    Args:
        order_id: The order ID to cancel.
        item_id: Optional item ID for partial cancellation.
    """

@tool
def create_return(order_id: str, item_id: int):
    """
    Create a return request for a specific item.

    Args:
        order_id: The order ID.
        item_id: The item being returned.
    """