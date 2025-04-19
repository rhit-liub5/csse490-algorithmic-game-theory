from marginal_value import calculate_marginal_value
from sample_valuations import SampleValuations

def local_bid(goods, valuation_function, price_vector, num_iterations=100):

    old = {g: valuation_function({g}) for g in goods}

    for iteration in range(num_iterations):
        new = old.copy() 
        for g in goods:
            mv = calculate_marginal_value(goods, g, valuation_function, old, price_vector)
            new[g] = mv
        print(f"Iteration {iteration + 1}: {new}")
        
        converged = True
        for g in goods:
            if abs(new[g] - old[g]) > 1e-3:
                converged = False
                break
        
        old = new.copy() 
        if converged:
            print("Convergence reached.")
            break

    return old

if __name__ == "__main__":
    goods = set(SampleValuations.SINGLE_ITEM_VALS.keys())
    price_vector = SampleValuations.generate_price_vector() 

    for valuation_func in [
        SampleValuations.additive_valuation,
        SampleValuations.complement_valuation,
        SampleValuations.substitute_valuation,
        SampleValuations.randomized_valuation
    ]:
        print(f"Running LocalBid with {valuation_func.__name__}:")
        optimized_bids = local_bid(goods, valuation_func, price_vector, num_iterations=100)
        print("Final bid vector:", optimized_bids, "\n")
