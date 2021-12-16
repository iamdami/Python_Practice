import numpy as np

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])

in1dTest = np.in1d(["aaa", "vvv", "MMM"], sap)
print("in1dTest")
print(in1dTest)
print("\n")

isinTest = np.isin(["aaa", "vvv", "MMM"], sap)
print("isinTest")
print(isinTest)
print("\n")

# return same
