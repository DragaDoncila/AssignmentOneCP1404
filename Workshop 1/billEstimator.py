TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Bill Estimator 2.0")

tariff = input("Which tariff- 11 or 31? ")
while tariff != "11" and tariff != "31":
    print("That is not a valid tariff.")
    tariff = input("Which tariff- 11 or 31? ")

daily_use_kWh = float(input("Please enter your daily kWh use: "))
billing_period_days = int(input("How many days in your billing period: "))

if tariff == "11":
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
# cents_kWh = int(input("Please enter the cost of your kWh in cents: "))

bill_estimate_dollars = (tariff * daily_use_kWh * billing_period_days)

print("Estimated bill amount: $", bill_estimate_dollars, sep="")
