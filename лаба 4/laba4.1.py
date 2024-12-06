from math import sqrt
from datetime import datetime, date, time


def checker_sqrt(number:int):
     
     if isinstance(number,(int,float))!=True:
          return(f'{number} не является числом')
     else:
          return (f'Корень из числа {number} равен {sqrt(number)}')
     
print(checker_sqrt(4))
print(f'Время {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')