

temp_maxima = {"01/09/2022": 15.6,
               "02/09/2022": 13.8,
               "03/09/2022": 15.2,
               "04/09/2022": 20.4,
               "05/09/2022": 20.5,
               "06/09/2022": 20.6,
               "07/09/2022": 23.7,
               "08/09/2022": 24.5,
               "09/09/2022": 12.6,
               "10/09/2022": 13.2,
               "11/09/2022": 15.3,
               "12/09/2022": 15.8,
               "13/09/2022": 15,
               "14/09/2022": 14.5,
               "15/09/2022": 17.4,
               "16/09/2022": 21.6,
               "17/09/2022": 22.8,
               "18/09/2022": 20.8,
               "19/09/2022": 21.8,
               "20/09/2022": 15.4,
               "21/09/2022": 14
               }


# Extremos absolutos de la maxima
max_temp = max(temp_maxima, key=temp_maxima.get)
maximo_absoluto = temp_maxima[max_temp]

print("El máximo absoluto de la temperatura máxima dentro del periodo considerado fue de", maximo_absoluto,"°C", "el día", max_temp)

#minimo de la maxima
min_temp = min(temp_maxima, key=temp_maxima.get)
minimo_absoluto = temp_maxima[min_temp]
print("El mínimo absoluto de la temperatura máxima dentro del periodo considerado fue de", minimo_absoluto,"°C", "el día", min_temp)



