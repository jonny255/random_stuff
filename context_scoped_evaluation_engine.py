



# - Make this data agnostic so it could be converted into a module.
# - One axis will represent the reward/incentive/cost-saving measure.
# - The other will represent the service fee, commission, cost, etc.
# - Might also want to introduce an instrument for quantifying the 'sunk cost fallacy' angle or the "how
# far out will it be and time spent to refuel at a particular gas station, in relation to price saved."




# Provider definitions (each has its own fee structure)
providers = {
    "fancy_restaurant": {
        "fees": {"credit_card": 3.0, "debit_card": 0.0, "cash": 0.0},
        "surcharge_type": "percent"  # could be "flat" later
    },
    "gas_station": {
        "fees": {"credit_card": 0.1, "debit_card": 0.0, "cash": 0.0},
        "surcharge_type": "per_gallon"
    },
    "electronics_store": {
        "fees": {"credit_card": 2.5, "debit_card": 1.0, "cash": 0.0},
        "surcharge_type": "percent"
    }
}

# Payment options (your cards / methods)
payment_options = {
    "visa_rewards": {"cashback": 0.03, "apr": 0.2499, "intro_apr": 0.0, "intro_months": 0},
    "amex_0apr":    {"cashback": 0.00, "apr": 0.2699, "intro_apr": 0.0, "intro_months": 18},
    "discover_all": {"cashback": 0.01, "apr": 0.2199, "intro_apr": 0.0, "intro_months": 12}
}



# Logic core — compute effective net cost per transaction
import pandas as pd

def compute_provider_matrix(provider_name, amount):
    p = providers[provider_name]
    results = []

    for method, fees in p["fees"].items():
        for card, attrs in payment_options.items():
            # Apply card reward or APR depending on context
            fee = fees if p["surcharge_type"] == "percent" else 0  # extend later
            rewards = amount * attrs["cashback"]
            interest = 0

            # Example APR logic: if not paid off immediately
            remaining_balance = max(0, amount - (amount / 3))  # simulate partial payoff
            monthly_rate = attrs["apr"] / 12
            interest = remaining_balance * monthly_rate * 3  # 3-month carry

            total_cost = amount + (amount * fee / 100) - rewards + interest
            results.append({
                "provider": provider_name,
                "method": method,
                "card": card,
                "fee_%": fee,
                "rewards_$": rewards,
                "interest_$": interest,
                "net_total_$": total_cost
            })

    df = pd.DataFrame(results)
    df["rank"] = df["net_total_$"].rank()
    return df.sort_values("net_total_$")

# Use it
print(compute_provider_matrix("fancy_restaurant", amount=400))



































"""

# matrix between when 5 cents off per gallon of gas gets surplused by 1.5%, 3%, 5%


1% vs 
3% 
0.05 & 5% = 1.00
0.10 & 

cost-saving deals
*5c off 





















"""