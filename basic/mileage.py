kms = input("How many kilometers did you cycle today?\n")
# 1 km = 1.60934 miles
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride is {miles} miles")
