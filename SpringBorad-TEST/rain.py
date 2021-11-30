def get_rainfall():
    city_map = {}
    print_result = False
    while print_result is False:
        city_name = input("Enter the City Name: ")
        print(f"city name {city_name}")
        if city_name != '\n':
            rain_quantity = input("Enter the quantity of rain: ")
            print(rain_quantity)
            if city_name in city_map:
                existing_quantity = city_map[city_name]
                new_quantity = int(existing_quantity) + int(rain_quantity)
                city_map[city_name] = new_quantity
            else:
                city_map[city_name] = rain_quantity
        else:
            print("display result")
            print_result = True
    print(city_map)
    for k, v in city_map.items():
        print(k, v)
