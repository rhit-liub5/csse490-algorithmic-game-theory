def calculate_marginal_value(goods, selected_good, valuation_function, bids, prices):

    all = set()
    for good in goods:
        if good == selected_good:
            continue
        if bids.get(good, 0) > prices.get(good, 0):
            all.add(good)
    
    value_with = valuation_function(all.union({selected_good}))
    value_without = valuation_function(all)
    
    marginal_value = value_with - value_without
    return marginal_value
