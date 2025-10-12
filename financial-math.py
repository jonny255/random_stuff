import os
import math
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


"""
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

        def rate_change(self):
                rate_change_30 = "rate_30 - rate_0"
                rate_change_90 = "rate_90 - rate_30"
                rate_change_180 = "rate_180 - rate_90"

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



                try:
                        sort = ['a', 'd', 'b', 'e', 'f', 'g', 'y', 'd', "z", "d"]
                except:
                        pass


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
                                rate = 0.128 * kwh              # Move to json file
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
                                        foo = "bar"

                        def fuel():
                                fuel_type = ["gasoline", "diesel", "LNG", "electric", "hybrid", "alien-tech"]
                                fuel_alternatives = ["ethanol", "biogasoline", "custom redneck blend"]

                        def food():
                                greenhouse = "yes"
                        
                        def cellular_service():
                                mains = ["tmobile", "at&T", "verizon"]
                                alternatives = ["mint", "cricket", "vongage?", "metro"]















"""






try:
  print(x)
except:
  print("An exception occurred")








"""