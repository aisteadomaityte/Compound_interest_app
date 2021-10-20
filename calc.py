def monthly_compounding(initial, monthly, years, annual_rate):
    sum = initial
    months = years * 12
    annual_rate = annual_rate/100
    #iterate through months
    for month in range(int(months)):
        #apply annual rate to current balance
        sum = sum * (1 + annual_rate/12)
        #add monthly contribution
        sum = sum + monthly
    return sum