import pandas_datareader as pdr

markets = (
    '^NKX',#Nikkei225
    '^DJI',#DowJones
    '^NDQ'#NASDAQ
)

data_list = []
for market in markets:
    data = pdr.DataReader(market, 'stooq', '2020-01-01', '2020-01-10')
    data_list.append(data)

print('data_list[0]:', data_list[0])
print('data_list[1]:', data_list[1])
print('data_list[2]:', data_list[2])
