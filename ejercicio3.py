
temp_minima = {
"01/09/2022":	12.8,
"02/09/2022":	8.8,
"03/09/20222":	4.6,
"04/09/2022":	4.6,
"05/09/2022":	5.8,
"06/09/2022":	12,
"08/09/2022":	12.4,
"09/09/2022":   9.4,
"10/09/2022":	7.4,
"11/09/2022":	2.2,
"12/09/2022":	5.8,
"13/09/2022":	11,
"14/09/2022":	4.4,
"15/09/2022":	4.8,
"16/09/2022":	10.8,
"17/09/2022":	12.2,
"18/09/2022":	12.8,
"19/09/2022":	12.4,
"20/09/2022":	10.7,
"21/09/2022":	10.2

}

# máximo absoluto de la mínima
maxima_temp = max(temp_minima, key=temp_minima.get)
maximo_absoluto = temp_minima[maxima_temp]

print("El máximo absoluto de la Mínima fue de", maximo_absoluto,"°C", "el día", maxima_temp)

#minimo de la maxima
minima_temp = min(temp_minima, key=temp_minima.get)
minimo_absoluto = temp_minima[minima_temp]
print("El mínimo absoluto de la Mínima fue de", minimo_absoluto,"°C", "el día", minima_temp)