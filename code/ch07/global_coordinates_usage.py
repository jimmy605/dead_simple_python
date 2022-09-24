from global_coordinates import GlobalCoordinates

nsp = GlobalCoordinates(latitude=(37, 46, 32.6, "N"),
                        longitude=(122, 24, 39.4, "W"))

print(nsp.__repr__())
print(f"No Starch Press's offices are at {nsp}")
