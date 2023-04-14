import statistics

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

mediana = statistics.median(temp_maxima)
print("la mediana de las temperaturas maximas es:", mediana)

#Mediana de las mínimas
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

mediana_min = statistics.median(temp_minima)
print("la mediana de las temperaturas mínimas es:", mediana_min)

#Mediana de las temperaturas medias

temperatura_media = [14.2,
                     11.3,
                     9.9,
                     12.5,
                     13.15,
                     14.05,
                     17.85,
                     18.45,
                     11,
                     10.3,
                     8.75,
                     10.8,
                     13,
                     9.45,
                     11.1,
                     16.2,
                     17.5,
                     16.8,
                     17.1,
                     13.05,
                     12.1]

mediana_med = statistics.median(temperatura_media)
print("la mediana de las temperaturas medias es:", mediana_med)

