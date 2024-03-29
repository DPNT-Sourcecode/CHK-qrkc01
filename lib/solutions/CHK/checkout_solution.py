

# noinspection PyUnusedLocal
# skus = unicode string
def checkout_r1(skus: str):
    """
    Calculate the total checkout value of all items in the basket
    considering any special offers

    Args:
    - skus (str): String containing the SKUs of all products

    Returns:
    - int: The total checkout value or -1 for illegal input
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers = {'A': (3,130), 'B': (2,45)}
    items = {}
    for sku in skus:
        if sku not in prices:
            return -1
        if sku in items:
            items[sku] += 1
        else:
            items[sku] = 1
    
    total_price = 0
    for item, quantity in items.items():
        if item in offers:
            offer_quantity, offer_price = offers[item]
            offer_count = quantity // offer_quantity
            normal_count = quantity % offer_quantity
            total_price += offer_count * offer_price + normal_count * prices[item]
        else:
            print(total_price, quantity, prices, item)
            total_price += quantity * prices[item]    
    return total_price    


def checkout_r2(skus: str):
    """
    Calculate the total checkout value of all items in the basket
    considering any special offers

    Args:
    - skus (str): String containing the SKUs of all products

    Returns:
    - int: The total checkout value or -1 for illegal input
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    discount_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
    }
    free_item_offers = {
        'E': [('B', 2, 1)], 
    }
    items = {}

    for sku in skus:
        if sku not in prices:
            return -1
        if sku in items:
            items[sku] += 1
        else:
            items[sku] = 1
    
    # Apply free item offers
    for item, offers in free_item_offers.items():
        for free_item, required_qty, free_qty in offers:
            if item in items and free_item in items:
                num_free_items = (items[item] // required_qty) * free_qty
                items[free_item] = max(0, items[free_item] - num_free_items)

    total_price = 0
    # Apply discount offers and calculate total
    for item, quantity in items.items():
        if item in discount_offers:
            for offer_qty, offer_price in discount_offers[item]:
                while quantity >= offer_qty:
                    total_price += offer_price
                    quantity -= offer_qty
        # Calculate price for remaining items
        total_price += quantity * prices[item]

    return total_price

def calculate_total_checkout_value(skus, prices, discount_offers, free_item_offers, group_discount_offers = None) -> int:
    """
    Core logic to calculate the total prices for a string of SKUs, 
    This considers prices, discount offers and free item offers.

    Parameters:
    - skus (str): A string containing SKUS of all the products in the basket
    - prices (dict): Mapping of product prices
    - discount_offers (dict): Mapping to show relevant discounts for the products
    - free_item_offers (dict): Mapping to show list of free items which can be applied to combinations of products
    - group_discount_offers (dict| None): Mapping for offers which contain combinations of specific set of products to redeem

    Returns:
    - int: Total checkout value of the itemes
    """
    items = {}

    for sku in skus:
        if sku not in prices:
            return -1
        if sku in items:
            items[sku] += 1
        else:
            items[sku] = 1
    total_price = 0

    if group_discount_offers:
        for group_items, (required_qty, group_price) in group_discount_offers.items():
            available_items = {item: items[item] for item in group_items if item in items}
            total_group_items = sum(available_items.values())
            while total_group_items >= required_qty:
                total_price += group_price
                total_group_items -= required_qty

                for item in sorted(group_items, key=lambda x:prices[x]):
                    if required_qty == 0:
                        break
                    if item in available_items and available_items[item] > 0:
                        deduct_count = min(available_items[item], required_qty)
                        available_items[item] -= deduct_count
                        items[item] -= deduct_count
                        required_qty -= deduct_count

                available_items = {item: items[item] for item in group_items if item in items and items[item] > 0}
                total_group_items = sum(available_items.values())

    
    # Apply free item offers based on item comparison
    for item, quantity in items.copy().items():
        if item in free_item_offers:
            for offer_item, required_qty, free_qty in free_item_offers[item]:
                # If the offer applies to the item itself
                if offer_item == item:
                    total_free_items = (quantity // (required_qty + 1)) * free_qty
                    items[item] -= total_free_items
                # If the offer applies to another item
                elif offer_item in items:
                    num_free_items = (quantity // required_qty) * free_qty
                    items[offer_item] = max(0, items[offer_item] - num_free_items)

    # Apply discount offers and calculate total
    for item, quantity in items.items():
        if item in discount_offers:
            for offer_qty, offer_price in discount_offers[item]:
                while quantity >= offer_qty:
                    total_price += offer_price
                    quantity -= offer_qty
        # Calculate price for remaining items
        total_price += quantity * prices[item]

    return total_price

def checkout_r3(skus: str):
    """
    Calculate the total checkout value of all items in the basket
    considering any special offers

    Args:
    - skus (str): String containing the SKUs of all products

    Returns:
    - int: The total checkout value or -1 for illegal input
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
    discount_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
    }
    free_item_offers = {
        'E': [('B', 2, 1)], 
        'F': [('F', 2, 1)]
    }

    total = calculate_total_checkout_value(skus, prices, discount_offers, free_item_offers)
    return total
    
def checkout_r4(skus: str):
    """
    Calculate the total checkout value of all items in the basket
    considering any special offers

    Args:
    - skus (str): String containing the SKUs of all products

    Returns:
    - int: The total checkout value or -1 for illegal input
    """
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
        'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40,
        'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40,
        'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
    }
    discount_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]
    }
    free_item_offers = {
        'E': [('B', 2, 1)],
        'F': [('F', 2, 1)],
        'N': [('M', 3, 1)], 
        'R': [('Q', 3, 1)], 
        'U': [('U', 3, 1)], 
    }

    total = calculate_total_checkout_value(skus, prices, discount_offers, free_item_offers)
    return total
    
def checkout(skus: str):
    """
    Calculate the total checkout value of all items in the basket
    considering any special offers

    Args:
    - skus (str): String containing the SKUs of all products

    Returns:
    - int: The total checkout value or -1 for illegal input
    """
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
        'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40,
        'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40,
        'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21
    }
    discount_offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)]
    }
    free_item_offers = {
        'E': [('B', 2, 1)],
        'F': [('F', 2, 1)],
        'N': [('M', 3, 1)], 
        'R': [('Q', 3, 1)], 
        'U': [('U', 3, 1)], 
    }

    group_discount_offers = {
        ('S', 'T', 'X', 'Y', 'Z'): (3,45)
    }

    total = calculate_total_checkout_value(skus, prices, discount_offers, free_item_offers, group_discount_offers)
    return total


