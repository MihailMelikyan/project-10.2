from threading import Thread
from time import sleep
from datetime import time

class Knight(Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} На нас напали !')
        enemies_count = 100
        day_count = 0
        while enemies_count > 0:
            enemies_count -= self.power
            day_count += 1
            if enemies_count < self.power:
                enemies_count == 0

            print(f'{self.name} сражается {day_count} осталось {enemies_count} воинов')
            sleep(1)
            print((f'{self.name} одержал победу за {day_count} дней'))

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все имеет начало и конец ,как и эти битвы.' )
