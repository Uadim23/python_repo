duration = int(input('Введите количество секунд: '))
sec = duration % 60
seconds = duration % 3600
minutes = seconds // 60
hour = duration // 3600
print(hour, "час", minutes, "мин", sec, "сек")
