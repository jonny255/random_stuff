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
                        RoR = perc


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
                        trading_fees = ""
                        trading_fee_tracker = 0
                        if trading_fee_tracker <= 500:
                                trading_fees = 0
                        else:
                                trading_fees = dnr
                        


                def CoinbaseOne_Basic(self):
                        trading_fees = trading_fees
                        earn_btc_back = 1.04 # Coming soon Coinbase One Card.
                        Account_protection = 1000
                        earn_usdc_rewards = 4.5 # Boosted rewards on your first 10k USDC

                        #### NOTE #### The 5% boost is of the APY, not in addition to the APY
                        earn_more_staking = 5 #% on eligible staking assets

                        member_sweepstakes = "like winning 1 BTC"
                        onchain_benefits = "With Base, Aerodrome, and more"

                def CoinbaseOne_Preferred(self):
                        trading_fees = trading_fees # $500/mo in trades, a spread applies
                        earn_btc_back = 1.04 # Coming soon Coinbase One Card.
                        Account_protection = 10000
                        earn_usdc_rewards = 0.045 # Boosted rewards on your first 30k USDC
                        earn_more_staking = 5
                        member_sweepstakes = "like winning 1 BTC"
                        onchain_benefits = "With Base, Aerodrome, and more"

                def CoinbaseOne_Premium(self):
                        trading_fees = trading_fees # $500/mo in trades, a spread applies
                        earn_btc_back = 4 # Coming soon Coinbase One Card.
                        Account_protection = 250000
                        earn_usdc_rewards = 1.045 # Boosted rewards; unlimited
                        earn_more_staking = 5
                        member_sweepstakes = "like winning 1 BTC"
                        onchain_benefits = "With Base, Aerodrome, and more" 



        






        def number_crunching(self):

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

        borrowing against crypto assets = 18% ?
        lending 



        try
                sort 



        Synthetic CDO vs 


        def fractional_reserve_banking():
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

        def CDO():
                jameithealtcoin =  [
                        BTC  : 25%
                        ETH  : 20%
                        USDT : 50%
                        AAVE : 5%
                ]


        def CDO_synthetic(self):
                asset_to_stake = CDO
                self.convert(asset_to_stake)
                # Use this CDO as a currency, and then stake it on eth; or could I create my own coin
                # that IS the CDO, have it ETH based, and then could I stake that for stETH and then
                # borrow USDC against that stETH?










 







S"""






try:
  print(x)
except:
  print("An exception occurred")








"""