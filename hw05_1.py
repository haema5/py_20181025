# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше
# среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
#
# Примечание: 4 квартала - это 4 разных прибыли ;-)

enterprises = {}
profit_sum = 0

n = int(input('Укажите кол-во предприятий: '))
for i in range(n):
    ent_name = input(f'\nНазвание {str(i + 1)}-го предприятия: ')
    for k in range(4):
        ent_profit = float(input(f'Прибыль {str(i + 1)}-го предприятия за {str(k + 1)}-й квартал: '))
        if k == 0:
            enterprises[ent_name] = ent_profit
        else:
            enterprises[ent_name] += ent_profit
    profit_sum += enterprises[ent_name]

profit_avrg = profit_sum / n
print(f'\nСредняя прибыль предприятий за год: {profit_avrg:.2f}')

print('\nПредприятия с прибылью выще среднего:')
for i in enterprises:
    if enterprises[i] > profit_avrg:
        print(f'\t- {i} ({enterprises[i]:.2f})')

print('\nПредприятия с прибылью ниже среднего:')
for i in enterprises:
    if enterprises[i] < profit_avrg:
        print(f'\t- {i} ({enterprises[i]:.2f})')
