# A = P(1 + R/100) t
principal = 10000
rate = 10.25
time = 5
Amount = principal * (pow((1 + rate / 100), time))
CI = Amount - principal
print("Compound interest is", CI)
