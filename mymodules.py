import os
import json
import pandas as pd
import numpy
import csv




class main:
            # Build out this module, then move it to external library
        def dynamic_coin_risk_percentile(self):
                df = pd.read_csv('coinrisk.csv')
    #            with open("coinrisk.csv") as f:
    #                    print(f.read())

            # Coins that have already been screened as safe enough to buy either to trade or stake.
        def allowable_coins(self):
                a = ""


            # 
        def coins_pairs(self):
                df = pd.read_csv('all coins')
                df.corr() # Positive numbers good for going long on; negatives good for hedging/placing short positions on. Get close to |1|.


            # Determine voltility of coin
        def voltility(self):
                # First measure standard deviations and maybe also percentiles
                # Pricing last rolling 5 minutes at 15 second intervals
                pricing = []
                pricing = numpy.std(pricing)

                # Volume of trades covering same area
                volume = []
                volume = numpy.std(volume)

                # Decide what I want to do from here; percentiles, 



        def auto_insurance_stats(self):
        # First we must calculate what the global statistics are for us to be involved in an accident.
                vaac = pd.read_csv('vehicle_accidents_across_country.csv')
                cal = pd.read_csv('holidays_paydays_weekdays_weekends_observation_days.csv')
                weather = pd.read_csv('weather.csv')
                inclement_weather = pd.read_csv('inclement_weather.csv')
                census = pd.read_csv('census_demographics_data.csv')
"""
alpha value: level of significance between data to determine how close to extreme data has to be be for null hypothesis to be rejected
p value: how close to extreme the data actually is. P & alpha values are compared to establish the statistical significance

If p value <= alpha we reject the null hypothesis and say the data is statisically significant, otherwise we accpt the null hypo.

After the above is calculated, we'll still need to calculate the following:
    1.  Our driving behaviors
    2.  Driving history, incl 'near misses'
    3.  local weather, incl inclement weather events, types, times, and frequency
    4.  miles driven; what days of the week; and what time/timeranges

    5.  Crunch mulitple hypothetical coverage plans with quotes to reverse engineer auto insurance pricing algorithm
    6.  Once matrix has been built with consistent pricing strategy per coverage plan/premium/type/etc, compare with personal driving behavior
    7.  Based on that, we could then build a custom tailored plan where the coverage will be updated at least monthly based on statistical
        analysis of personal driving habits and local environment variables.
"""













