

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
    offers = {
        'A': [('discount', 5,200), ('discount', 3,130)],
        'B': [('discount', 2,45)],
        'E': [('free', 2, 'B', 1)]}
    items = {}

    for sku in skus:
        if sku not in prices:
            return -1
        if sku in items:
            items[sku] += 1
        else:
            items[sku] = 1
    
    total_price = 0
    # function to handle any special offers and negate quantities for bygof
    def apply_offers(item,quantity,offers, items):
        total = 0
        for offer_type, *offer_details in sorted(offers, key=lambda x: -x[1]):
            if offer_type == 'discount':
                required_qty, offer_price = offer_details
                while quantity >= required_qty:
                    total += offer_price
                    quantity -= required_qty
            elif offer_type == "free":
                required_qty, free_item, free_qty = offer_details
                if quantity >= required_qty and free_item in items:
                    eligible_free_items = min(items[free_item], (quantity // required_qty)*free_qty)
                    items[free_item] = max(0, items[free_item] - eligible_free_items)
        # Add any left over quantities post offers
        total += quantity * prices[item]
        return total
    
    for item,quantity in list(items.items()):
        if item in offers:
            total_price += apply_offers(item,quantity,offers[item], items)
        else:
            total_price += quantity * prices[item]
    return total_price


