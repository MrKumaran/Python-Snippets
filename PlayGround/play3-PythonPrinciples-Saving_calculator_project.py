greeting = "Hello "
name = "Bob"

# Yearly Income
hourly_wage = 20
hours_per_week = 40
income_per_week = hourly_wage * hours_per_week
weeks_per_year = 48
income_per_year = income_per_week * weeks_per_year

# Yearly Spending
spend_per_week = 400
spend_per_year = spend_per_week * 52

# Yearly Savings
savings_per_year = income_per_year - spend_per_year

# Displaying Details
print(greeting+name)
print(name + "'s yearly income is:")
print(income_per_year)
print(name + "'s yearly spend is:")
print(spend_per_year)
print(name + "'s yearly savings:")
print(savings_per_year)

