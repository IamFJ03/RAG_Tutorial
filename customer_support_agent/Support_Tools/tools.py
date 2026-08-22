from langchain_core.tools import tool
import random
import string
from datetime import datetime
from DB_Manager.ticketsDB import TicketDatabaseManager
from DB_Manager.orderItemsDB import OrderItemDatabaseManager
from DB_Manager.orderDB import OrderDatabaseManager
from typing import Literal
ticket = TicketDatabaseManager()
order_item = OrderItemDatabaseManager()
order = OrderDatabaseManager()

@tool
def create_ticket(
    ticket_type: str,
    description: str,
    status: Literal['open', 'in_progress', 'resolved', 'closed'],
    item_id: int
):
    """
    Create a customer support ticket for solving the issues customer have.

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
    all_data = order_item.fetch_item_by_id(item_id)
    result = {
        "order_id": all_data[1],
        "customer_id": all_data[7]
    }

    ticket.add_table(ticket_id, ticket_type, result['customer_id'], result['order_id'], item_id, status, description, created_at)
    response = ticket.get_ticket(ticket_id)
    return response



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
    Example: - what is the status of ticket TKT-1007? 
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
    order.update_table(order_id)
    result = order.fetch_order_by_id(order_id)
    return f"Your order Updated: {result}"