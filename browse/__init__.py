from typing import List, Dict
from products import dao


class Product:
    """Represents a product in the system."""
    
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> 'Product':
        """
        Creates a Product instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing product details.
        
        Returns:
            Product: An instance of the Product class.
        """
        return Product(
            id=data['id'], 
            name=data['name'], 
            description=data['description'], 
            cost=data['cost'], 
            qty=data.get('qty', 0)
        )


def list_products() -> List[Product]:
    """
    Lists all products available in the system.
    
    Returns:
        List[Product]: A list of Product instances.
    """
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """
    Retrieves a product by its ID.
    
    Args:
        product_id (int): The ID of the product.
    
    Returns:
        Product: An instance of the Product class.
    """
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load(product_data)


def add_product(product: Dict):
    """
    Adds a new product to the system.
    
    Args:
        product (dict): A dictionary containing product details.
    """
    if 'qty' in product and product['qty'] < 0:
        raise ValueError("Quantity cannot be negative.")
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a product.
    
    Args:
        product_id (int): The ID of the product.
        qty (int): The new quantity.
    
    Raises:
        ValueError: If the quantity is negative.
    """
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    dao.update_qty(product_id, qty)
