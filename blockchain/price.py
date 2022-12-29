'''
Если мы хотим рассчитать цену криптовалюты, мы можем сделать это, взяв рыночную стоимость монеты и разделив ее на количество монет в обращении. 

Рыночная стоимость криптовалюты может быть рассчитана путем умножения цены монеты на объем монет, которые торгуются на рынке. 

BTC - общее предложение 21 000 000 монет * Текущая цена 16 500 долларов = рыночная капитализация 346 500 000 000 долларов
'''


def get_capitalize(all_money, price):
    return all_money * price


def calc_price(free_valute, in_wallets, miners, miners_price, difficult):
    print(free_valute * miners_price, in_wallets, (miners * difficult))
    price = (free_valute * miners_price) / in_wallets + (miners * difficult)

    return price

if __name__ == '__main__':
    all_valute = 10000
    free_valute = all_valute / 4
    in_wallets = all_valute - free_valute
    miners = 5 
    miners_price = 1
    difficult = 5