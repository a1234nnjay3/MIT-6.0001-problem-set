#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 17:44:21 2018

@author: Stanley
"""

annual_salary = int(input("Enter your annual salsry: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ​"))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:​ "))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
num_month = 0
monthly_salary = annual_salary/12

while portion_down_payment*total_cost > current_savings:
    num_month +=1
    current_savings = current_savings*(1+(r/12)) + monthly_salary*portion_saved
    if num_month%6==0:
        monthly_salary = monthly_salary*(1+semi_annual_raise)
        
print("Number of months:", num_month)
