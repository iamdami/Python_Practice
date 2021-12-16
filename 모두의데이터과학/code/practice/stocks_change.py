import numpy as np

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])

stocks = np.array(
    [140.49, 0.97, 40.68, 41.53, 55.7, 57.21, 98.2, 99.19, 109.96, 111.47, 35.71, 36.27, 87.85, 89.11, 30.22, 30.91])
print(stocks)
print("\n")

stocks_reshape_t = stocks.reshape(8, 2).T
print(stocks_reshape_t)
print("\n")

stocks_reshape_t[1, 0] = np.nan
print("새 주식가격이 결측치라고 가정")
print(np.isnan(stocks_reshape_t))
print(type(np.isnan(stocks_reshape_t)))
print("\n")

stocks_reshape_t[np.isnan(stocks_reshape_t)] = 0
print(type(stocks_reshape_t[np.isnan(stocks_reshape_t)]))
print(stocks_reshape_t[np.isnan(stocks_reshape_t)])
print("결측치 수정")
print(stocks_reshape_t)
print("\n")


changes = np.where(np.abs(stocks_reshape_t[1] - stocks_reshape_t[0]) > 1.00,
                   stocks_reshape_t[1] - stocks_reshape_t[0], 0)
print("changes")
print(changes)
print("\n")

print("sap[np.nonzero(changes)]-using where")
print(sap[np.nonzero(changes)])
print("\n")

print("using bool index")
print(sap[np.abs(stocks_reshape_t[1] - stocks_reshape_t[0]) > 1.00])
