

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
    # function to handle any special offers
    def apply_discounts(item, quantity, discount_offers):
        total_discounted_price = 0
        for required_qty, offer_price in sorted(discount_offers, key=lambda x: -x[0]):
            num_offers = quantity // required_qty
            total_discounted_price += num_offers * offer_price
            quantity -= num_offers * required_qty
        return total_discounted_price, quantity
    
    def apply_free_items(item, quantity, free_item_offers, items):
        for required_qty, free_item, free_qty in free_item_offers:
            if free_item in items:
                eligible_free_items = (quantity // required_qty) * free_qty
                items[free_item] = max(0, items[free_item]-eligible_free_items)
    
    for item,quantity in list(items.items()):
        if item in offers:
            discount_offers = [(details[1], details[2]) for details in offers[item] if details[0] == 'discount']
            free_item_offers = [(details[1], details[2], details[3]) for details in offers[item] if details[0] == 'free']
        
            discounted_price, remaining_qty = apply_discounts(item, quantity, discount_offers)
            total_price += discounted_price
            apply_free_items(item, remaining_qty, free_item_offers, items)
            total_price += remaining_qty * prices[item]
        else:
            total_price += quantity * prices[item]
    return total_price



