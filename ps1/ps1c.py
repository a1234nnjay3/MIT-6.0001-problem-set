#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 17:44:21 2018

@author: Stanley
"""

annual_salary = int(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
monthly_salary = annual_salary/12

low = 0
high = 10000
portion_saved = (high+low)//2.0

current_savings = 0
num_month = 0
num_step = 0
while num_month <36:
    num_month +=1
    current_savings = current_savings*(1+(r/12)) + monthly_salary*1
    if num_month%6==0:
        monthly_salary = monthly_salary*(1+semi_annual_raise)

if current_savings < portion_down_payment*total_cost:
    print("It is not possible to pay the down payment in three years.")
else:
    current_savings = 0
    num_month = 0
    monthly_salary = annual_salary/12
    while num_month <36:
        num_month +=1
        current_savings = current_savings*(1+(r/12)) + monthly_salary*portion_saved/10000
        if num_month%6==0:
            monthly_salary = monthly_salary*(1+semi_annual_raise)
          
    while abs(portion_down_payment*total_cost - current_savings) >= 100:
        if portion_down_payment*total_cost > current_savings:
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (high+low)//2.0
        num_step +=1
        
        num_month = 0
        current_savings = 0
        monthly_salary = annual_salary/12
        while num_month <36:
            num_month +=1
            current_savings = current_savings*(1+(r/12)) + monthly_salary*portion_saved/10000
            if num_month%6==0:
                monthly_salary = monthly_salary*(1+semi_annual_raise)
    print("Best savings rate:", portion_saved/10000)
    print("Steps in bisection search:​", num_step)
