from pandas import DataFrame
from pandas import read_csv
from pandas import read_json
from pandas import read_excel

# If you import pandas as whole,
# all the modules in the package would be imported and increases the memory load
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
print(df5.shape)
# A DataFrame is not modified or on using set_index() method. It only process the data for displaying on the fly
# If you wish to save the data, you need to store it to another DataFrame variable
df5 = df5.set_index("ID")
# Or set 'inplace' parameter to True
# df5.set_index("ID",inplace=True)
print(df5)

print(" ---- ")
print(df5.index)
print(df5.columns)
print(type(df5.index), " ", type(df5.columns))
print()

df6 = read_json("../assets/sample.json")
print()
print(df6.set_index("ID"))

# Note on importing Excel
# Pandas may require the xlrd library as a dependency.
# If you get an error such as ModuleNotFoundError: No module named 'xlrd',
# you can fix that by installing xlrd: pip install xlrd

# Excel may have multiple sheets. sheet_name=0 identifies the first sheet in the Excel
df7 = read_excel("../assets/sample.xlsx", sheet_name=0)
print()
print(df7.set_index("ID"))

df8 = read_csv("../assets/sample-semi-colons.txt", sep=";")
print()
print(df8.set_index("ID"))

df9 = read_csv("http://pythonhow.com/supermarkets.csv")
print()
print(df9.set_index("ID"))

df10 = read_csv("../assets/sample.csv")
print()
print("  ----  Indexing and Slicing DataFrame  ----  ")
# We can do Positional Based / Label Based Indexing
# Observe the difference in slicing between loc() and iloc()

df10 = df10.set_index("ID")
# Label Based - df.loc()
print(df10.loc[4:6, "City":"Name"])
print(df10.loc[:,"City"])
print(df10["City"])

# Positional Based - df.iloc()
print(df10.iloc[4:6, 2:6])

print()
print("  ----  Deleting Columns and Rows of a DataFrame  ----  ")
# Param 1 specifies Column 'City' needs to be deleted. 0 for a row
print(df10.drop("City", 1))
# Similar to df.set_index(), df.drop() also works on the fly. To save the changes, save the result to a DataFrame Variable
df10 = df10.drop("City", 1)
df10 = df10.drop(3, 0)
print()
print(df10.index)
print(df10.columns)
print(df10.drop(df10.index[4:5], 0)) # df.index()
print(df10)
print(df10.drop(df10.columns[2:5], 1)) # df.columns()
print(df10)

print()
print("  ----  Adding and Modifying data of a DataFrame  ----  ")
print(df10.shape)
print(len(df10.index))
# Should pass values for all the Rows
df10["Rank"] = [4,3,2,5,1]
df10["Continent"] = df10.shape[0] * ["N. America"]
# Modifying an already existing column values
df10.loc[:,"State"]=["AR","MO","KA","NY","DC"]
print(df10)

# To Add a new row, we use a tweak with df.T
# Transpose columns to rows, add details, transpose again

df10_t = df10.T
print(df10_t)

df10_t[7] = ["3317 7th St", "FL","USA","Macy's",75,6,"N. America"]
df10 = df10_t.T

# .apply() method is used to modify all the row values of a particular column
def add_num(i):
    return i + 5
df10["Employees"]=df10["Employees"].apply(add_num)
print(df10)