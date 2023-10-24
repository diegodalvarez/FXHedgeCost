# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:53:42 2023

@author: Diego
"""

# A little confusing the JPY sovereign yiled is in collect data

import os
import pdblp
import pandas as pd
import datetime as dt

end_date = dt.date.today()
start_date = dt.date(year = 1970, month = 1, day = 1)

end_date_input  = end_date.strftime("%Y%m%d")
start_date_input = start_date.strftime("%Y%m%d")

parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
data_path = os.path.join(parent_path, "data")
ticker_path = os.path.join(data_path, "gilt_tickers.csv")
out_path = os.path.join(data_path, "yields.parquet")

gilt_tickers = (pd.read_csv(
    filepath_or_buffer = ticker_path).
    assign(name = lambda x: x.Description.str.split(" ").str[2]).
    query("name != 'Infl'").
    Security.
    drop_duplicates().
    to_list())

tickers = [*set(gilt_tickers)] + ["USGG10YR Index"]

con = pdblp.BCon(debug = False, port = 8194, timeout = 5_000)
con.start()

df_tmp = (con.bdh(
    tickers = tickers,
    flds = ["PX_LAST"],
    start_date = start_date_input,
    end_date = end_date_input).
    reset_index().
    melt(id_vars = "date"))

(df_tmp.to_parquet(
    path = out_path,
    engine = "pyarrow"))