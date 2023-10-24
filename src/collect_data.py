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
ticker_path = os.path.join(data_path, "tickers_reference.csv")
out_path = os.path.join(data_path, "fx_hc.parquet")

fx_hc = (pd.read_csv(
    ticker_path)
    [["Security"]].
    assign(filter_out = lambda x: x.Security.str[5]).
    query("filter_out == ['E', 'J']")
    ["Security"].
    to_list())


tickers = [
    "GJGB10 Index", "GECU10YR Index", "HOLDJN Index"] + fx_hc

tickers = [*set(tickers)]

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