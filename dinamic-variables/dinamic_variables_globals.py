import pandas_datareader as pdr

markets = {
    '^NKX':'Nikkei225',
    '^DJI':'DowJones',
    '^NDQ':'NASDAQ'
}

for market in markets:
    name = markets[market]
    globals()[name] = pdr.DataReader(market, 'stooq', '2020-01-01', '2020-01-10')

    #結果を確認
    print('name:',name)
    print(globals()[name])
    # print(vars()[name])#

#一つずつ変数を指定して表示する場合は以下の記述で問題ない
print('Nikkei225:', Nikkei225)
print('DowJones:', DowJones)
print('NASDAQ:',NASDAQ)

