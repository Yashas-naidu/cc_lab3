import json
from typing import List
from products import Product, get_product
from cart import dao


class Cart:
    """Represents a shopping cart for a user."""
    
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        """Loads a cart instance from dictionary data."""
        contents = [get_product(product_id) for product_id in json.loads(data['contents'])]
        return Cart(data['id'], data['username'], contents, data['cost'])


def get_cart(username: str) -> List[Product]:
    """
    Retrieves all products in the user's cart.
    
    Args:
        username (str): The username of the user.

    Returns:
        List[Product]: List of product objects in the cart.
    """
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    products_in_cart = []
    for cart_detail in cart_details:
        product_ids = json.loads(cart_detail['contents'])  # Parse safely
        products_in_cart.extend([get_product(product_id) for product_id in product_ids])

    return products_in_cart


def add_to_cart(username: str, product_id: int) -> None:
    """
    Adds a product to the user's cart.
    
    Args:
        username (str): The username of the user.
        product_id (int): ID of the product to add.
    """
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int) -> None:
    """
    Removes a product from the user's cart.
    
    Args:
        username (str): The username of the user.
        product_id (int): ID of the product to remove.
    """
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str) -> None:
    """
    Deletes the user's cart.
    
    Args:
        username (str): The username of the user.
    """
    dao.delete_cart(username)
