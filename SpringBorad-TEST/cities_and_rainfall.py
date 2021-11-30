import os

def get_rainfall():
    city_map = {}
    print_result = False
    while print_result is False:
        city_name = input("Enter the City Name:  ")
        #print({(type(city_name))}, {city_name})
        if city_name != '':
            rain_quantity = input("Enter the quantity of rain: ")
            print(f"rain type {type(rain_quantity)}")
            if city_name in city_map:
                existing_quantity = city_map[city_name]
                print(f"type in dict {type(existing_quantity)}")
                new_quantity = int(existing_quantity) + int(rain_quantity)
                city_map[city_name] = new_quantity
            else:
                city_map[city_name] = rain_quantity
        else:
           print_result = True

    out = '\n'.join(': '.join((city, rain)) for (city, rain) in sorted(city_map.items()))
    print(type(out))
    print(out)
    #print(sorted(out))
    # output = ''
    # for k, v in city_map.items():
    #     output += k +" : "+str(v)+'\n'
    # return output
get_rainfall()




# #if __name__ == '__main__':
#        fptr = open('out.txt', 'w')
#        result = get_rainfall()
#        fptr.write(result + '\n')
#        fptr.close()



