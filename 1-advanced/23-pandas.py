from pandas import DataFrame
from pandas import read_csv

# If you import pandas as whole, 
# all the modules in the package would be imported that load more into memory
# If import pandas is used, then you can use pandas.DataFrame
# import pandas

# Data Frame - Special Object that holds the data
# It is made up of Series (columns)
df1 = DataFrame([[2, 4, 6, 8], [10, 20, 30, 40]])
print(df1)
print(type(df1))

# Output
# The first row values are the column headers
# The first column values are the indexes
#     0   1   2   3
# 0   2   4   6   8
# 1  10  20  30  40

# We can name the values using columns and index
# However naming Indexes in a real wolrd DB application may be not needed
df2 = DataFrame([
    [5, 25], [10, 100], [15, 225], [20, 400],
    [25, 625]],
    columns=["Number", "It's Square"]
)
print()
print(df2)

df3 = DataFrame([
    [1, 'Alpha', 50, "123-456"],
    [2, 'Beta', 75],
    [3, "Charlie", None, "123-123"]],
    columns=["ID", "Name", "Score", "Mobile"]
)
print()
# Using set_index method as we already have a "ID" Series on the data
print(df3.set_index("ID"))

# Output
# ID-2 doesn't have a Mobile and the output displays by itself as None
#        Name  Score   Mobile
# ID
# 1     Alpha   50.0  123-456
# 2      Beta   75.0     None
# 3   Charlie    NaN  123-123


df4 = DataFrame([
    [100, 10.59, 20, 4],
    [200, 7.99, 15, 3],
    [300, 20.00, 30, 2]],
    columns=["ID", "Price", "Max_Order", "Order_Qty"],
    index=["Item1", "Item2", "Item3"]
)
print()
print(df4)

print("\n", "Mean of each column in df4 :")
print(df4.mean())

print()
print(type(df4.mean()))

print("\n", "Mean of entire DataFrame df4 :")
print(df4.mean().mean())

print("\n", "A DataFrame is made up of Series. Order_Qty series for the items in df4 : ")
print(df4.Order_Qty)

# Setting header to None
df5 = read_csv("../assets/sample.csv", header=None)
print()
print(df5)

df5 = read_csv("../assets/sample.csv")
print()
print(df5.set_index("ID"))

# Note on importing Excel
# Pandas may require the xlrd library as a dependency.
# If you get an error such as ModuleNotFoundError: No module named 'xlrd', 
# you can fix that by installing xlrd: pip install xlrd

