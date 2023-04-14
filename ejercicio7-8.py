import statistics

lluvia_r3 = [2.1,
             0,
             0,
             0,
             0,
             0,
             0,
             4.5,
             0.1,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0.5,
             0,
             0,
             0]

# Acumulados de lluvia durante el período dado
acumulados_lluvia = sum(lluvia_r3)
print("Total lluvias acumuladas : ", round(acumulados_lluvia, 1))


# Mediana
mediana = statistics.median(lluvia_r3)
print("La mediana es:", mediana)

# Acumulado medio
acum_medio = acumulados_lluvia / len(lluvia_r3)
print("Acumulado medio es:", round(acum_medio, 1), "mm")

#Cantidad de dias con registro de 0 mm
cant_dias_secos = lluvia_r3.count(0)
print("Cantidad de dias sin precipitaciones: ", cant_dias_secos)

#Dias con registros de precipitacion mayor o igual  a 1 mm
dias_lluviosos = [lluvia_r3 for lluvia_r3 in lluvia_r3 if lluvia_r3 >= 1]
cantidad_dias_lluvia= len(dias_lluviosos)
print("Dias con precipitaciones mayor o igual a 1mm:", cantidad_dias_lluvia)


