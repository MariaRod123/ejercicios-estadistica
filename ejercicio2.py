import numpy as np

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

media_estadistica = np.mean(temperatura_media)
media= round(media_estadistica, 2)
print(" La media de la temperatura media es: ", media, "°C")