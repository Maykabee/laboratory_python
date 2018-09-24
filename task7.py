minutes = int (input("Введіть кількість хвилин "))
FullHours, Minutes = divmod(minutes, 60)
Hours = FullHours % 24
print ("З момента півночі пройшло {0} ч {1} хв.".format(Hours, Minutes))

