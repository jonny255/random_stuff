import os
import math
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

import best_payment_option_logic
import context_scoped_evaluation_engine



"""
personal bet with myself: total LOC will be approximately 7,000 LOC, though the range will be 5,000 to 10,000 LOC

what's the difference between building a financial instrument vs investment vehicle.
        I think investment vehicle ismore macro, like stocks, 
            TODO
    [x] build calculator for compound interest, compounded daily, but APY is also updated
        daily
    [ ] 

"""


class main:
        def compounding_frequency(self):
                self.daily_compounding = 365
                self.monthly_compounding = 12
                self.annually_compounding = 1

                print("Please select 'daily', 'monthly', or 'annually'.")
                compounding_frequency = input()

                if input == "daily":
                        compounding_frequency = self.daily_compounding
                elif input == "monthly":
                        compounding_frequency = self.monthly_compounding
                elif input == "annually":
                        compounding_frequency = self.annually_compounding
                else:
                        raise Exception("ERROR: Please select 'daily', 'monthly', or 'annually'.")
            
            
        def APY_calculator(self):
                
                # compound interest variables
                self.A = 0 # final amount
                self.P = 0 # initial principle balance
                self.r = 42 # interest rate
                self.t = 12 # number of time periods elapsed the amount of; time (usually in yrs) that the money is saved, invested, or borrowed
                self.n = self.daily_compounding # Amount of times the interest is compounded per time period (t)


                # PEMDAS = "Please Excuse My Dear Aunt Sally"

                # A = P * (1 + r / n) * pow(365, 12)
                self.nt = (self.n * self.t)
                self.A = self.P * math.pow((1 + self.r / self.n), self.nt)
            
        def intrate_calculator(self):
        #        r = n[(A/P)^(1/nt) - 1]
                r = (self.n) * [math.pow((self.A / self.P), self.nt)]


        # latest values of coins staked/to be staked.


        coin = ["AXS", "COMP", "AVS", "CRO", "CRV", "DAI"]

        for x in coin:
                print(coin)


        # Calculate the date 30 days before today's date
        dt_0 = date.today() - timedelta(30)

        # Print the current date using date.today()
        print('Current Date :', date.today())

        # Print the date calculated 5 days before the current date
        print('5 days before Current Date :', dt_0) 


        dt_30 = dt_0 - relativedelta(months=1)
        dt_90 = dt_0 - relativedelta(months=3)
        dt_180 = dt_0 - relativedelta(months=6)



            

                # actual rates percentage values
        def rate(self):
                APY = 42 # as of right now/today
                rate_0 = APY
                rate_30 = 46
                rate_90 = 48
                rate_180 = 51

                # Stock rate change calculator
        def rate_change(self):
                rate_change_30 = "rate_30 - rate_0"
                rate_change_90 = "rate_90 - rate_30"
                rate_change_180 = "rate_180 - rate_90"

                # Rate change tolerance calculator
        def tolerance(self):
                tolerance_30 = "rate_change_30 / APY"
                tolerance_90 = "rate_change_90 / APY"
                tolerance_180 = "rate_change_180 / APY"


                # Stock Percentage Calculator
        def stock_percentage_calculator(self):
                old_price = 0
                new_price = 0

                # Formula      
                # RoR = (latest price - initial price) / latest price
                
                RoR = (new_price - old_price) / new_price

                if old_price < new_price:
                        perc = RoR + 1
                        print(perc)
                elif old_price > new_price:
                        perc = RoR
                        print(perc)      # -0.032353984
                elif old_price == new_price:
                        perc = RoR



                a = old_price - new_price

                if new_price < old_price:
                        perc = a / old_price
                elif new_price > old_price:
                        perc = a * 3
                        



            # compound formula
            # A = P(1 + r / n)^(n * t)


                staking_pnt_USDC = 4.1 #%
                staking_pnt_ETH = 4.1 #%

            # nt = math.pow(n, t)


        def value_savings(self):
        #        cost_of_subscription_plan
                subscription_plan_cost = ""
        #       Basic Benefits
                CoinbaseOne_Basic_monthly = 4.99
                CoinbaseOne_Basic_annual = 49.99
                CoinbaseOne_Preferred_monthly = 49.99
                CoinbaseOne_Preferred_annual = 499.88
                CoinbaseOne_Premium_monthly = 299.99
                CoinbaseOne_Premium_annual = 2999.99
                
                print("Select Plan Below:")
                
                print("1a. Coinbase One Basic Monthly")
                print("1b. Coinbase One Basic Annual")
                
                print("2a. Coinbase One Preferred Monthly")
                print("2b. Coinbase One Preferred Annual")
                
                print("3a. Coinbase One Premium Monthly")
                print("3b. Coinbase One Premium Annual")



                if input() == "1a" or "Coinbase One Basic monthly":
                        benefits_package = CoinbaseOne_Basic_monthly
                elif input() == "1b" or "Coinbase One_Basic_annual":
                        benefits_package = CoinbaseOne_Basic_annual
                elif input() == "2a" or "CoinbaseOne_Preferred_monthly":
                        benefits_package = CoinbaseOne_Preferred_monthly
                elif input() == "2b" or "CoinbaseOne_Preferred_annual":
                        benefits_package = CoinbaseOne_Preferred_annual
                elif input() == "3a" or "CoinbaseOne_Premium_monthly":
                        benefits_package = CoinbaseOne_Premium_monthly
                elif input() == "3b" or "CoinbaseOne_Premium_monthly":
                        benefits_package = CoinbaseOne_Premium_annual

                def trading_fees(self):
                        trading_fees = "0"
                        trading_fee_tracker = 0
                        if trading_fee_tracker <= 500:
                                trading_fees = 0
                        else:
                                trading_fees = "0.02"
                        


                def CoinbaseOne_Basic(self):
                        trading_fees = "trading_fees"
                        earn_btc_back = 1.04 # Coming soon Coinbase One Card.
                        Account_protection = 1000
                        earn_usdc_rewards = 4.5 # Boosted rewards on your first 10k USDC

                        #### NOTE #### The 5% boost is of the APY, not in addition to the APY
                        earn_more_staking = 5 #% on eligible staking assets

                        member_sweepstakes = "like winning 1 BTC"
                        onchain_benefits = "With Base, Aerodrome, and more"

                def CoinbaseOne_Preferred(self):
                        trading_fees = "trading_fees" # $500/mo in trades, a spread applies
                        earn_btc_back = 1.04 # Coming soon Coinbase One Card.
                        Account_protection = 10000
                        earn_usdc_rewards = 0.045 # Boosted rewards on your first 30k USDC
                        earn_more_staking = 5
                        member_sweepstakes = "like winning 1 BTC"
                        onchain_benefits = "With Base, Aerodrome, and more"

                def CoinbaseOne_Premium(self):
                        trading_fees = "trading_fees" # $500/mo in trades, a spread applies
                        earn_btc_back = 4 # Coming soon Coinbase One Card.
                        Account_protection = 250000
                        earn_usdc_rewards = 1.045 # Boosted rewards; unlimited
                        earn_more_staking = 5
                        member_sweepstakes = "like winning 1 BTC"
                        onchain_benefits = "With Base, Aerodrome, and more"













        def number_crunching(self):

                def stake_stacking_lvl1(self):
                        ETH_AMT = 500
                        ETH_LTV_pct = 0.70  # Maybe include the borr_stETH here?
                        ETH_LTV_amt = 350
                        borr_stETH = 0.03       # 3% cost borrowing USDC from the stETH
                        stETH_APY = 1.0191
                        stETH = ETH_AMT * ETH_LTV_pct

                        # This section to potentially be broken off to its own; meant to crunch numbers between potential:risk ratio of staking
                        # additional eth to perform another round of stake stacking
                        if stETH > (stETH_APY * ETH_LTV_pct):
                                borr_stETH = 0.03       # 3% cost borrowing USDC from the stETH
                                USDC = stETH
                                USDC_APY = 1.0410
                                Total_APY = ((ETH_AMT * stETH_APY))
                        elif stETH < (stETH_APY * ETH_AMT):
                                foo = "bar"
                        else:
                                foo = "bar"

                def margin_call_monitor(self):
                        Liquidation_threshold = "0.7 - 0.8"
                        Leveraged_amt = 500
                        Current_price = 350
                        volatility = (Leveraged_amt - Current_price) / Leveraged_amt
                        
                        # FIXME         Values are wrong; need higher volatility to be monitored closer, rn it's the other way around.
                        if volatility <= 0.07:
                                update_interval = 30
                        elif 0.07 > volatility <= 0.12:
                                update_interval = 15
                        elif 0.0 < volatility < 0.07:
                                update_interval = 1
                        else:
                                update_interval = 60

                def trigger_margin_call(self):
                        add_more_collateral_amt = 200
                        ETH_AMT = 500
                        ETH_LTV_amt = 350
                        while (ETH_LTV_amt / ETH_AMT) >= 0.7:
                                print(ETH_AMT)
                                add_more_collateral_amt = 200
                                new_amt = ETH_AMT + add_more_collateral_amt
                                print("new amount: " + new_amt)
                        while not (ETH_LTV_amt / ETH_AMT) >= 0.7:
                                continue

                        # replay of crypto/defi loan
                def partly_repay_loan(self):
                        partly_repay_loan_amt = 20
                        ETH_AMT = 500
                        ETH_LTV_amt = 350
                        while (ETH_LTV_amt / ETH_AMT) >= 0.7:
                                print(ETH_AMT)
                                partly_repay_loan_amt = 20
                                new_amt = ETH_LTV_amt - partly_repay_loan_amt
                        while not (ETH_LTV_amt / ETH_AMT) >= 0.7:
                                continue

                        # Backtest rewards
                def backtest_rewards(self):
                        points_conversion = "pts * 0.01"
                        points = ""
                        reward_type = points
                        cashback = ""
                        reward_category = "gas"
                        timeframe = "JUN - OCT"

                        # Previous transactions that meet critera and 
                        previous_transactions = []

                        # match previous_transactions:
                        #         case 1 | 2 | 3 | 4 if 'x' == 4:
                                





                def living_off_interest(self):
                        foo = "bar"
                        apm = "Amount per millie"       # Move to json file
                        apy = 0.041                     # Move to json file
                        apm = 1000 * apy                # Move to json file
                        apm_mo = apm / 12               # Or $3.4137 / mo per every $1000 @ 4.1% | $6.375 @ 7.65% | $10/mo @ 12%


                def zeroize_bills(self):     #first minimize, then interest
                        def electricity():
                                bill1 = "electricity"           # Move to json file
                                utility_company = "CPS"         # Move to json file
                                kwh = 0
                                kwm = kwh / 60
                                whm = 16.67 # 1,000Wh / 60min = 16.67 watts/hr
                                tiers = {"tier 1" : "0.128", "tier 2" : "0.142", "tier 3" : "0.175"}
                                rate = 0.128 * kwh              # Move to json file
                                ratecostm = rate / 60
                                avg_kwh_3d = 0
                                avg_kwh_5d = 0
                                forecast_kwh_1d = 0
                                forecast_kwh_3d = 0
                                forecast_kwh_5d = 0
                                diff_btwn_1 = forecast_kwh_3d - forecast_kwh_1d
                                diff_btwn_2 = forecast_kwh_5d - forecast_kwh_3d
                                
                                def create_maxtrix():
                                # matrix table of kwh used per day, with current day, and predictions
                                # Another matrix with the solar/free energy product, pricing diff from CPS, etc
                                        kwh_used = {
                                                "Day 1" : "5",
                                                "Day 2" : "2",
                                                "Day 3" : "8", 
                                                "Day 4" : "7",
                                                "Day 5" : "2"
                                        }
#kwh_related = {
#    "kwh_used": {"fee_1": 2, "fee_2": 7, "fee_3": 3},
#    "kwh_produced":  {"fee_1": 1, "fee_2": 0, "fee_3": 6},
#    "estimated_kwh_gotaways":  {"fee_1": 4, "fee_2": 2, "fee_3": 0},
#}
                                        kwh_produced = {
                                                "Day 1" : "6",
                                                "Day 2" : "2",
                                                "Day 3" : "6", 
                                                "Day 4" : "6",
                                                "Day 5" : "4"
                                        }

                                        estimated_kwh_gotaways = {
                                                "Day 1" : "2",
                                                "Day 2" : "0",
                                                "Day 3" : "0", 
                                                "Day 4" : "3",
                                                "Day 5" : "2"
                                        }

                                        for x in kwh_used:
                                                total_kwh = x
                                        
                                maintenance_cost_YTD = 0
                                total_monthly_loan_amt = 0
                                total_monthly_loan_principle = 0
                                total_monthly_loan_interest = 0
                                capex = 5500
                                base = ""
                                loan_amortization = {"SunTan" : "28", "Signature Solar" : "21", "Battery Hookup" : "12"}
                                equip_lifespan = {"Hybrid Inverter" : "84", "PV array" : "180", "LFP 5.12KWh" : "180"}
                                Projected_MWh_Production_CY2025 = "3/yr or 250KWh/month"

                                green_kwh_cost = (
# base = total_monthly_loan_amt * 0.128
# amortized_monthly_cost_of_Capex = ((capex / 180 = 30.556))
# principle_loan_amt */+- base, capex <- will come back later to this
#
# Idea here is to stretch/spread the cost more inline with equip lifespan, without refi any of the loans
#
# 250KWh - (current usage) = -00(consumed) or +00 (gotaway) NOTE: to battery = consumed (AKA captured)
# -00KWh consumed = good
# +00KWh gotaway = price per kwh penalty
#
                                )

                                kwh_forecast_today = 17
                                kwh_battery_budget = 7
                                kwh_budget_today = 10
                                def Preassign_KWh_Capacity():
                                        appliances = {"fridge" : "1D = (.134 * kwh) * 8"}
                                        kitchen = {"coffee = ((kwm * 1.5) * 7.5minutes of use) = 0.1875kwh", "microwave = ((ratem * 1.5) * 7.5minutes of use) = 0.1875kwh"}
                                        homelab = {"homelab" : "(.35 * kwh) * 24"}
                                        ac = {"window unit in office" : "(1.1 * kwh) * 'x'"}
                                Expected_remaining_kwh_capacity = 3

                        def fuel():
                                fuel_type = ["gasoline", "diesel", "LNG", "electric", "hybrid", "alien-tech"]
                                fuel_alternatives = ["ethanol", "biogasoline", "custom redneck blend"]

                        def food():
                                greenhouse = "yes"
                                plants = ""
                                electricity_usage = ""
                                farmersmarket = ""
                        
                        def coupon_tracker():
                                groceries = ""


                        
                        def cellular_service():
                                mains = ["T-Mobile", "AT&T", "Verizon"]
                                alternatives = ["Mint (T-Mobile)", "cricket (AT&T)", "vongage?", "Metro"]



                def utility_payment_methods(self):
                        payment_options = ["debit", "checking", "credit"]

                                # CPS
                        def energy_provider():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02
                        
                                # T-Mobile
                        def phone_provider():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02

                                # SAWS
                        def water_utility():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02

                                # AT&T
                        def internet_provider():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02

                                # Buck-ees
                        def gas_station():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02

                                # Geico
                        def auto_insurance():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02

                                # Placeholder 1
                        def placeholder1():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02

                                # Placeholder 2
                        def placeholder2():
                                debit_fee = 0.00
                                checking_fee = 0.00
                                credit_card_fee = 0.02






                def best_payment_option_logic(self):
                        provider_type = "energy"
                        best_accts = {
                                "debit" : "9234",       # Funds Available
                                "checking" : "2475",    # Funds Available
                                "credit" : "2745",       # 1% cash back
                                "digital wallet/card" : "Gemini"        # Promotion: "Earn $200 in crypto if you spend $3000 in 90 days."
                        }

        #                if best_accts + energy_provider.utility_payment_methods == 2:
        #                        foo = "bar"



                        selected_acct = "Gemini"









                payment_method_fees = {
                        "energy_provider": {"Debit": 0.02, "Checking": 0.07, "Credit": 0.03},
                        "phone_provider": {"Debit": 0.01, "Checking": 0.00, "Credit": 0.06},
                        "water_provider": {"Debit": 0.04, "Checking": 0.02, "Credit": 0.00},
                }

                best_option = {
                        "Debit" : "9234",       # Funds Available
                        "Checking" : "2475",    # Funds Available
                        "Credit" : "2745",       # 1% cash back
                        "digital wallet/card" : "Gemini"        # Promotion: "Earn $200 in crypto if you spend $3000 in 90 days."
                }







# If you'll have dozens of providers and many fees:
#       Consider storing them in a CSV or JSON file and load them up dynamically.
#       Build your conditions dynamically from a list or config file.
#       Use pandas if you want full-blown matrix operations or comparisons.



















        # Synthetic CDO vs 


        def fractional_reserve_banking(self):
                # The Federal Reserve
                Initial_bal = 1000
                Reserved_pct = 10
                Amt_to_lend_pct = 90
                lent_amt_1 = 900
                amt_reserved = 100
                lent_amt_1_apy = 0.0191

                bal_2 = 900
                lent_amt_2 = 810
                amt_reserved = 90

                bal_3 = 729

                # define CDO
        def CDO():
                jameithealtcoin =  [
        #                BTC  : 25%
        #                ETH  : 20%
        #                USDT : 50%
        #                AAVE : 5%
                ]

                # define synthetic CDO
        def CDO_synthetic(self):
                asset_to_stake = CDO
                self.convert(asset_to_stake)
                # Use this CDO as a currency, and then stake it on eth; or could I create my own coin
                # that IS the CDO, have it ETH based, and then could I stake that for stETH and then
                # borrow USDC against that stETH?















"""









 







Over-leveraged Lending
Total amount:	$1,000		Pct Lent:	70%		APY:		RoR:		Total APY:		Reserved Amt:	30%	Total Reserved:
ETH:		$1,000		stETH:		$700		1.91%		$13.37		$13.37				$300.00		$300.00
stETH:		$700		USDC:		$490		4.1%		$20.09		$33.46				$210.00		$510.00
AAVE:		$490		CRO:		$343		2.4%		$8.23		$41.69				$147.00		$657.00
SOL:		$343		COMP:		$240		6.3%		$15.13		$56.82				$102.90		$759.90
IXP:		$240		DOGE:		$168		27%		$45.38		$102.20				$72.03		$831.93
														
														
Average Annual APY:	8.34%													
Average Annual Net:	$1,083.42													
								Max:			TLA Pct:	1.941177		
Total Annual RoR:	10.22%					41.71%								
Total Annual RoR Amt:	$102.20													
Total Reserved Pct:	83.19%													
														
Total Leveraged Amt:	$1,941													
TLA Pct:		194.12%													





                def best_payment_option_logic(utility_payment_methods, best_accts):
                        results = []

                        for provider_type, payment_fees in utility_payment_methods.items():
                                for fee_name, fee_value in payment_fees.items():
                                # Example: dynamic logic, e.g. sum Credit with each fee
                                        total = best_accts["Credit"] + fee_value

                                        results.append({
                                                "provider": provider_type,
                                                "fee": fee_name,
                                                "sum": total
                                        })

                        # Sort ascending by 'sum'
                        results.sort(key=lambda x: x["sum"])

                        return results
"""