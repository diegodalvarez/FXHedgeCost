import pandas as pd

link = "https://www.worldometers.info/geography/how-many-countries-in-europe/"
df_raw = (pd.read_html(
    link)
    [0]
    [["Country"]])