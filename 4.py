class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []  # Приватный атрибут для хранения истории операций


    # ВЫВОД ТЕКУЩЕГО БАЛАНСА
    @property
    def balance(self):
        return self._balance

    #ПОПОЛНЕНИЕ БАЛАНСА
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction(f"Пополнение: +{amount}")
            print('\n',f"Успешно внесено {amount}. Текущий баланс: {self._balance}")
        else:
            print('\n',"Сумма пополнения должна быть положительной")

    #СНЯТИЕ С БАЛАНСА
    def withdraw(self, amount):
        if amount <= 0:
            print('\n',"Сумма снятия должна быть положительной")
        elif amount > self._balance:
            print('\n',"Недостаточно средств на счете")
        else:
            self._balance -= amount
            self._log_transaction(f"Снятие: -{amount}")
            print('\n',f"Успешно снято {amount}. Текущий баланс: {self._balance}")

        #Логируем
    def _log_transaction(self, message):
        self._transactions.append((message, self._balance))
        #Получаем логи
    def get_transaction_history(self):
        return self._transactions.copy()  # Возвращаем копию, чтобы защитить оригинальный список

    # Создаем банковский счет с начальным балансом 1000
account = BankAccount(1000)

    # Проверяем начальный баланс через геттер
print(f"Начальный баланс: {account.balance}",'\n','-'*30)

    # Пробуем внести деньги
account.deposit(500)
account.deposit(-100)  # Неправильная сумма

    # Пробуем снять деньги
account.withdraw(200)
account.withdraw(2000)  # Недостаточно средств
account.withdraw(-100)  # Неправильная сумма

    # Проверяем баланс
print('\n',f"Текущий баланс: {account.balance}")

    #история операций
print("\nИстория операций:")
for transaction in account.get_transaction_history():
    print(f"{transaction[0]} | Баланс: {transaction[1]}")