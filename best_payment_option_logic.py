import pandas as pd
import re

# --- Step 1: Define base provider data ---
utility_providers = {
    "energy_provider": {"fee_1": 2, "fee_2": 7, "fee_3": 3},
    "phone_provider":  {"fee_1": 1, "fee_2": 0, "fee_3": 6},
    "water_provider":  {"fee_1": 4, "fee_2": 2, "fee_3": 0},
}

# --- Step 2: Define option logic (foo ↔ fee mapping) ---
best_option = {
    "foo1": {"bar": 3.5},   # e.g. 3.5 reward points or value
    "foo2": {"bar": 1.0},   # 1% cashback or equivalent
    "foo3": {"bar": 0.2},   # small promo
}

# --- Step 3: Convert providers to DataFrame ---
df = pd.DataFrame(utility_providers).T.reset_index().rename(columns={"index": "provider"})

# Flatten so each fee is its own row
melted = df.melt(id_vars=["provider"], var_name="fee", value_name="fee_value")

# --- Step 4: Map each fee_x to foo_x and bar_x dynamically ---
def extract_index(name):
    match = re.search(r"(\d+)", name)
    return match.group(1) if match else None

melted["fee_index"] = melted["fee"].apply(extract_index)
melted["foo"] = "foo" + melted["fee_index"]
melted["bar_value"] = melted["foo"].apply(lambda f: best_option.get(f, {}).get("bar", 0))

# --- Step 5: Calculate logic ---
# Example logic: effective cost = fee - reward
melted["net_effect"] = melted["fee_value"] - melted["bar_value"]

# Determine if reward outweighs fee or not
def decision(row):
    if row["net_effect"] < 0:
        return "profitable"
    elif row["net_effect"] == 0:
        return "neutral"
    else:
        return "loss"

melted["decision"] = melted.apply(decision, axis=1)

# --- Step 6: Find best option per provider ---
best_per_provider = (
    melted.loc[melted.groupby("provider")["net_effect"].idxmin()]
    .reset_index(drop=True)
    .sort_values("net_effect")
)

# --- Step 7: Optional pivot for overview ---
pivot = melted.pivot_table(
    index="provider",
    columns="fee",
    values="net_effect"
)

# --- Step 8: Display Results ---
print("=== Flattened Matrix ===")
print(melted)
print("\n=== Best Option per Provider ===")
print(best_per_provider)
print("\n=== Pivoted Matrix (net effects) ===")
print(pivot)





"""

# matrix between when 5 cents off per gallon of gas gets surplused by 1.5%, 3%, 5%


1% vs 
3% 
0.05 & 5% = 1.00
0.10 & 

cost-saving deals
*5c off 

"""


def best_payment_for_fuel(self):
    price_of_fuel = 2.85
    temp1 = 1
    temp2 = 3
    pts = 0
    pct = 3

    card1 = price_of_fuel - 0.10                            10/1.00
    card2 = price_of_fuel - 0.05                            5/1.00
    card3 = price_of_fuel * 0.95        # 5% Off            =       4.75
    card4 = price_of_fuel * 0.97        # 3% Off            =       
    card5 = price_of_fuel * 0.975       # 2.5% Off          =       
    card6 = price_of_fuel * 0.98        # 2% Off            =       
    card7 = price_of_fuel * 0.985       # 1.5% Off          =       
    card8 = price_of_fuel * 0.99        # 1% Off            =       
    
    if price_of_fuel <= 1.00:
        card1 = True
    else:
        card2 = True

    if temp1 <=  price_of_fuel >= temp2:




    if price_of_fuel >= 1.00:
        try:
            card3 = True

        except:
            print(Exception)
        


    avail_cards_95 = []
#    avail_cards_95 = [card_V, card_J, card_G]

    is card3 available at 0.95?


"""
    card1 <= price_of_fuel 
    pts <= 1 >= pct

"""



import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)















"""
      coinbaseOne basic monthly = 4.99
        coinbaseOne basic annual = 49.99
        potential_savings_prepay = 17%

        stock market index = 12% APY (Daily compounding included)
        annual inflation = 2.9%
        credit card interest = 14 - 32%
        credit card reward points = 

        personal loan interest (prosper, upstart, lendingclub) = 7 - 28%

        0% APR balance transfer promotion = 18 months
        0% APR purchase promotion = 18 months

        borrowing against crypto assets = 18% ? APR
        lending crypto assets = 12% APY

"""