favorite_cars = ["dudge", "G-class", "porsche 911", "mustang", "BMW M4"]

print("list of favorite car names:")
for car in favorite_cars:
    print(car)

unliked_car_index = favorite_cars.index("BMW M4")
favorite_cars[unliked_car_index] = "skibidi Van"

print("\nUpdated list of favorite car names:")
for car in favorite_cars:
    print(car) 