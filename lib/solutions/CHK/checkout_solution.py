

# noinspection PyUnusedLocal
# skus = unicode string
def checkout_old(skus: str):
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


def checkout(skus: str):
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
