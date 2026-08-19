from langchain_core.tools import tool
import random
import string
from datetime import datetime
from DB_Manager.ticketsDB import TicketDatabaseManager
from DB_Manager.orderItemsDB import OrderItemDatabaseManager

ticket = TicketDatabaseManager()
order_item = OrderItemDatabaseManager()

@tool
def create_ticket(
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
    created_at = datetime.now().isoformat()
    

    ticket.add_ticket(ticket_id, ticket_type, customer_id, order_id, item_id, status, description, created_at)




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
