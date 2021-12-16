import numpy as np

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])

stocks = np.array([140.49, 0.97, 40.68, 41.53, 55.7, 57.21, 98.2, 99.19, 109.96, 111.47, 35.71, 36.27, 87.85, 89.11, 30.22, 30.91])
print(stocks)
print("\n")

stocks_reshape1 = stocks.reshape(8, 2)
print(stocks_reshape1)
print("\n")

stocks_reshape_t = stocks.reshape(8, 2).T
print(stocks_reshape_t)
print("\n")
print(stocks_reshape_t[0, 0])  # 140.49
print("\n")

fall = np.greater(stocks_reshape_t[0], stocks_reshape_t[1])
print("fall")
print(fall)
print("\n")

print("sap_fall")
print(sap[fall])
