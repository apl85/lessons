# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию



prices = [157.82, 463.51, 9, 5, 55, 66, 77.71, 77.66, 22.44, 65.77, 234.66, 23424.41, 234.23, 23.66, 76.73, 34.23, 345]
prices.sort()
prices.reverse()

for i in prices:
    result_rub = int(i)
    result_kop = (i - result_rub) * 100
    print(f'{result_rub} руб  {result_kop:02.0f} коп', end=', ')
