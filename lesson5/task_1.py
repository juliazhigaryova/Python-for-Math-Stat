# Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.


interval_1  = 80 + (1.96 * 16/256**0.5)
interval_2 =  80 - (1.96 * 16/256**0.5)

#  Ответ: [78.04, 81.96]
