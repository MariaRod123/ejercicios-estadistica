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

temp_minima =[ 12.8,
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

# Calculo de extremos absolutos para la Máxima
maxima = max(temp_maxima)
minima = min(temp_maxima)
print("Extremos absolutos para la máxima: ", maxima, "°C (máximo absoluto)", "y",  minima, "°C (mínimo absoluto)")

# Calculo de extremos absolutos para la Mínima
maximo_min = max(temp_minima)
minimo_min = min(temp_minima)
print("Extremos absolutos para la mínima: ", maximo_min, "°C (máximo absoluto)", "y",  minimo_min, "°C (mínimo absoluto)")
