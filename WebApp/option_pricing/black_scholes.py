import math
from scipy.stats import norm

def calculate_option_price(option):
    S = option.underlying_price
    K = option.strike_price
    T = option.time_to_maturity
    r = option.risk_free_rate/100
    sigma = option.volatility/100

    # Calculate d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option.option_type == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option.option_type == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price
