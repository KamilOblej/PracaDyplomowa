from django.shortcuts import render, redirect

from camera.models import *

def listToString(s):  
    str1 = ""  
     
    for ele in s:  
        str1 += str(ele)
        str1 += " "   

    return str1  

def main(request):    
    ids = Temperature.objects.filter(temperature1__startswith='2')
    photosGt20 = Thermo.objects.filter(pk__in=ids)

    thermo_string = photosGt20[0].matrix
    thermo_list = list(thermo_string)
    thermo_array = []

    for i in range(len(thermo_list)):
        if not thermo_list[i].isdigit():
            continue
        else:
            if not thermo_list[i-1].isdigit():
                number_string = thermo_list[i]
                if not thermo_list[i+1].isdigit():
                    thermo_array.append(int(number_string))
                else:
                    continue
            else:
                number_string += thermo_list[i]
                if not thermo_list[i+1].isdigit():
                    thermo_array.append(int(number_string))
                else:
                    continue

    max_value = max(thermo_array)
    min_value = min(thermo_array)
    text1 = 'Max value: {}  Min value: {}'.format(max_value, min_value)

    # text1 = listToString(thermo_array)
    # text1 = str(len(photosGt20))
    # text1 = photosGt20[118].date_taken

    max_temperature = (max_value * 4 - 27316)/100 
    min_temperature = (min_value * 4 - 27316)/100
    text2 = 'Max temperature: {}  Min temperature: {}'.format(max_temperature, min_temperature)

    context = {
        'text1' : text1,
        'text2' : text2
    }

    return render(request, 'index2.html', context)
