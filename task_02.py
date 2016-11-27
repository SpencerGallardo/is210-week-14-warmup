#! usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Warmup Task 2"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Calculates the total cost of a quantity of itmes if they exist in a
    given list.
    Args:
        shoplist(dict): A dictionary with the key equal to a item name in
        FRUIT, and the value equal to the quantity to purchase as an integer.
    Returns:
        A dictionary keyed by the item name and the value as the cost per-item.
    Examples:
        >>> get_cost_per_item({'Red Plum': 2})
        {'Red Plum': 5.98}.
    """
    return {k: v * FRUIT[k] for k, v in shoplist.iteritems() if k in FRUIT}


def get_total_cost(shoplist):
    """Returns the total cost of given quantities for shopping list items.
    Args:
        shoplist(dict): A dictionary with the key equal to an item name in
        the imported FRUIT dictionary, and the value equal to the quantity to
        purchase as an integer.
    Returns:
        A integer equal to the total cost of all items and given quantities that
        exist in the FRUIT dictionary.
    Example:
        >>> print shoplist
        {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4,
        'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4,
        'Peach': 24, 'Beet': 1})
        112.80000000000001
    """

    costs = get_cost_per_item(shoplist)
    return sum(costs.itervalues())
