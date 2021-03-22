from camera.models import *

def main():    
    ids = Temperature.objects.filter(temperature1__startswith='2')
    photosGt20 = Thermo.objects.filter(pk__in=ids)

    thermo_string = photosGt20[0].matrix
    thermo_list = list(thermo_string)
    thermo_array = []

    for i in thermo_list:
        if i.isdigit():
            thermo_array.append(int(i))

    max_value = max(thermo_array)
    min_value = min(thermo_array)
    print('Max value: {}  Min value: {}'.format(max_value, min_value))

    max_temperature = (max_value * 4 - 27316)/100 
    min_temperature = (min_value * 4 - 27316)/100
    print('Max temperature: {}  Min temperature: {}'.format(max_temperature, min_temperature))

if __name__ == '__main__':
    main()