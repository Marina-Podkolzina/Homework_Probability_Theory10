import numpy as np
import pandas as pd
from statistics import mean
from scipy import stats
from scipy. stats import f_oneway
from statsmodels. stats.multicomp import pairwise_tukeyhsd


#Сформулируем нулевую гипотезу:
#H0: мю1 = мю2 = мю3   т.е. различия в среднем росте спортсменов нет.

#Альтернативная гипотеза:
#H1: мю1 != мю2 != мю3 т.е. различия в среднем росте спортсменов есть.

football=np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifting=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# Проверим условия применимости:
# Тест на нормальность Шапиро: 

stats.shapiro(football)
print(stats.shapiro(football))
print('_')
#pvalue=0.9495404362678528 > альфа 0.05 значит выборка имеет нормальное распределение

stats.shapiro(hockey)
print(stats.shapiro(hockey))
print('_')
#pvalue=0.7763139009475708 > альфа 0.05 значит выборка имеет нормальное распределение

stats.shapiro(weightlifting)
print(stats.shapiro(weightlifting))
print('_')
#pvalue=0.5051165223121643 > альфа 0.05 значит выборка имеет нормальное распределение

#Тест на однородность дисперсий Барлетт:

stats.bartlett(football, hockey, weightlifting)
print(stats.bartlett(football, hockey, weightlifting))
print('_')
#pvalue=0.7929254656083131 > альфа 0.05 значит выборки имеют однородность дисперсий

#Все выборки подходят под условия применимости,
#значит воспользуемся встроенным методом однофакторного дисперсионного анализа:

stats.f_oneway(football, hockey, weightlifting)
print(stats.f_oneway(football, hockey, weightlifting)) 
#statistic=5.500053450812596, pvalue=0.010482206918698693

#Получили значение pvalue=0.010482206918698693
#на уровне статистической значимости альфа = 0.05, 
# так как pvalue < альфа принимаем альтернативную гипотезу Н1.
#Значит различия в среднем росте спортсменов есть.

#Проведём Post hoc test Tukey:

#Так как в выборках разное колличество элементов,
# найдем среднее значение каждой выборки и добавим
# необходимое колличество раз.

football_mean = football.mean()
print (football_mean)# среднее значение 179.125
hockey_mean = hockey.mean()
print(hockey_mean)# среднее значение 178.66666666666666
weightlifting_mean = weightlifting.mean()
print(weightlifting_mean)# среднее значение 172.72727272727272

# Запишем выборки с добавленными значениями:

football1=np.array([173, 175, 180, 178, 177, 185, 183, 182, 179.1, 179.1, 179.1])
hockey1=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180, 178.6, 178.6])
weightlifting1=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

df= pd.DataFrame({'score':[173, 175, 180, 178, 177, 185, 183, 182,179.1, 179.1, 179.1,
                           177, 179, 180, 188, 177, 172, 171, 184, 180, 178.6, 178.6,
                           172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170],
                    'group': np.repeat(['football', 'hockey', 'weightlifting'],repeats= 11)})

tukey= pairwise_tukeyhsd (endog=df['score'],groups= df['group'],alpha= 0.05)
print(tukey)

#По данным в полученной таблице видно,
# что различия в среднем росте присутствуют между футболистами и штангистами,
# а так же между хоккеистами и штангистами.
# Между футболистами и хоккеистами разницы в среднем росте нет.