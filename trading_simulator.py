import pandas as pd

class TradingSimulator:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.position = 0
        self.transaction_history = []

    def simulate_trade(self, signal, market_data):
        if signal == 1:
            self.buy(market_data)
        elif signal == -1:
            self.sell(market_data)

    def buy(self, market_data):
        if self.balance >= market_data['close']:
            self.position = self.balance / market_data['close']
            self.balance = 0
            self.transaction_history.append(('Buy', market_data['close']))

    def sell(self, market_data):
        if self.position > 0:
            self.balance = self.position * market_data['close']
            self.position = 0
            self.transaction_history.append(('Sell', market_data['close']))

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.transaction_history

if name == "__main__":
    simulator = TradingSimulator()
    print(f"Начальный баланс: {simulator.get_balance()}")
    print("История сделок:", simulator.get_history())