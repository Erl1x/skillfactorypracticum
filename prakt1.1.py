depo_sum = float(input('Введите сумму вклада (рублей): '))  # ввод суммы депозита
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}  # процентные ставки в банках
banks = list(per_cent.keys())  # создание списка банков из словаря
percents = list(per_cent.values())  # создание списка процентных ставок из словаря

deposit = list()
deposit.append(int(depo_sum / 100 * float(percents[0])))
deposit.append(int(depo_sum / 100 * float(percents[1])))
deposit.append(int(depo_sum / 100 * float(percents[2])))
deposit.append(int(depo_sum / 100 * float(percents[3])))  # подсчёт заработка на вкладе

print(f'\nДоход по депозиту составит:\n{banks[0]} '
      f'банк - {deposit[0]} рублей\n{banks[1]} '
      f'банк - {deposit[1]} рублей\n{banks[2]} '
      f'банк - {deposit[2]} рублей\n{banks[3]} '
      f'банк - {deposit[3]} рублей\n')  # вывод на экран

max_deposit = max(deposit)  # максимальный заработок на депозите
print('Максимальная сумма, которую Вы можете заработать: {} рублей.'.format(max_deposit))
