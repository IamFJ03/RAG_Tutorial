from langchain_core.tools import tool

@tool
def get_order(order_id: str):
    """
    Tool to fetch all data of specific order using id provided
    Args:
        order_id: the id provided by user to fecth order data from database
    """

@tool
def get_order_item(item_id: str):
    """
        Tool to fetch all data of specific item using id provided
        Args:
            item_id: the id provided by user to fetch specific item data from database
        """
@tool
def create_ticket(
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