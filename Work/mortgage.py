# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra = 1000.0

while principal > 0:
    payment_with_extra = payment
    if month < 12:
        payment_with_extra += extra
    principal = principal * (1 + rate/12) - payment_with_extra
    total_paid = total_paid + payment_with_extra
    month += 1

print('Total paid', total_paid)
print('Total months', month)
