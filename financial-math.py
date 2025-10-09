import os
import pylance
import math






            TODO
    [ ] build calculator for compound interest, compounded daily, but APY is also updated
        daily
    [ ] 


# compound interest variables
int A = [final amount]
int P = [initial principle balance]
int r = [interest rate]
int t = [number of time periods elapsed] # the amount of time (usually in yrs) that the money is saved, invested, or borrowed
int n = [] # Amount of times the interest is compo8unded per time period (t)



# latest values of coins staked/to be staked.
list[T]: [AXS, COMP, AVS, CRO, CRV, DAI]
coin = "coin"
APY = 00.00 # as of right now/today

# actual rates percentage values
rate_0 = APY
rate_30 = ""
rate_90 = ""
rate_180 = ""

rate_change_30 = sum(rate_30 - rate_0)
rate_change_90 = sum(rate_90 - rate_30)
rate_change_180 = sum(rate_180 - rate_90)

tolerance_30 = sum(rate_change_30 / APY)
tolerance_90 = sum(rate_change_90 / APY)
tolerance_180 = sum(rate_change_180 / APY)






# compound formula
A = P(1 + r / n)^nt






