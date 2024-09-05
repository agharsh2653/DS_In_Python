import decimal,math

number = 35.7834

#converting the number into decimal value


print(f"Rounded {decimal.Decimal(number)} upto 0 decimal place {decimal.Decimal(number).quantize(decimal.Decimal('0.'))}")

print(f"Rounded {number} upto  decimal place {math.ceil(number)}")

print(f"Rounded {number} upto 1 decimal place {math.ceil(number*10)/10}")

print(f"Rounded {number} upto 1 decimal place "+"{:+.0f}".format(number))