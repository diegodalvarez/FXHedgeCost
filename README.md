# FX Hedge Cost
Analysis of International Hedging Costs for UST. The overall goal is to find how foreign UST holders are positioned in with their Treasury Holding. Historically the hedge cost for eliminating currency exposure has been negative, implying that sovereign investors particularly Japenese investors are losing money with their foreign UST portfolio. Since this is likely not the case it's assumed that the investors are foreging currency hedging. If the case is true then it would imply that currency dynamics now lead to selling or buying. 

## Sovereign Yields
![image](https://github.com/diegodalvarez/FXHedgeCost/assets/48641554/54f003ea-7006-4814-9518-0b634b91ebab)

## US Currency Hedging Cost
![image](https://github.com/diegodalvarez/FXHedgeCost/assets/48641554/72a3fd30-76b9-4bf6-9ea2-a6b1c7ea7c98)

## Comparing US Currency hedged yields, unhedged yields, and domestic yields
![image](https://github.com/diegodalvarez/FXHedgeCost/assets/48641554/d487e174-5421-4a40-975e-d3fc66e5d9de)

## Comparing hedged US Currency yield vs. Local sovereign yield (opportunity cost of covered carry)
![image](https://github.com/diegodalvarez/FXHedgeCost/assets/48641554/d699dfcf-0d0e-4842-b437-094b7c4b8f2d)

## Comparing opportunity cost of covered carry vs. Treasury Holding
![image](https://github.com/diegodalvarez/FXHedgeCost/assets/48641554/8cd78637-0b5a-4eea-921d-bb818a0e04a4)

## Repo layout
```bash
    FXHedgeCost
      └───notebook
          │   FXHedgeCost.ipynb
          │   FXHedgeCost10y.ipynb
          │   JPYHolder.ipynb
      └───src
          │   collectData.py

```

src files:
* ```collectData.py```: Collects data from Bloomberg Terminal

notebook Files:
* ```FXHedgeCost.ipynb```: Original file looking at hedge cost for overseas investors
* ```FXHedgeCost10y.ipynb```: Hedged and unhedged rate differential with Treasury Holding data
* ```JPYHolder.ipynb```: Analysis on JPY holdings and rate differential hedged and unhedged
