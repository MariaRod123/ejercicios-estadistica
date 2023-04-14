# calculo de los rangos de las temperaturas máximas y mínimas

# rango de la máxima

temp_maxima = [
    15.6,
    13.8,
    15.2,
    20.4,
    20.5,
    20.6,
    23.7,
    24.5,
    12.6,
    13.2,
    15.3,
    15.8,
    15,
    14.5,
    17.4,
    21.6,
    22.8,
    20.8,
    21.8,
    15.4,
    14
]

rango_maxima = max(temp_maxima) - min(temp_maxima)
print("El rango de la temperatura máxima es : ", rango_maxima)

# rango de la mínima

temp_minima = [12.8,
               8.8,
               4.6,
               4.6,
               5.8,
               7.5,
               12,
               12.4,
               9.4,
               7.4,
               2.2,
               5.8,
               11,
               4.4,
               4.8,
               10.8,
               12.2,
               12.8,
               12.4,
               10.7,
               10.2
               ]

rango_minima = max(temp_minima) - min(temp_minima)
print("El rango de la temperatura minima es : ", round(rango_minima, 2))
