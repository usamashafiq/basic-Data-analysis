import numpy as np
import pandas as pd
other_path = "path the file "
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(other_path,delimiter=',' )
df.columns = headers
df.to_csv()


df1 = df.replace('?', np.NaN)
df = df1.dropna(subset=["price"], axis=0)
print(df.head(10))
print(df.dtypes)
print(df.describe(include = "all"))

print(df[['length', 'compression-ratio']].describe())
print(df.info())
