real_estate_listing = open('213AnywhereAve.txt')
try:
    print(real_estate_listing.read())
finally:
    real_estate_listing.close()