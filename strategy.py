import MetaTrader5 as mt

NAME = '5003385418'
PASSWORD = 'of0tffun'
SERVER = 'MetaQuotes-Demo'

mt.initialize()
mt.login(NAME, PASSWORD, SERVER)

print('Sucessfully connected to MetaTrader 5')

symbol_info = mt.symbol_info_tick('EURUSD')._asdict()
print(symbol_info)
