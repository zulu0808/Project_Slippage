import os
import json
import pandas as pd
from web3 import Web3
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv 
load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
api = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version="v2")
#tickers = ['TSLA','ORCL','GME']
# conn represents CONNECTION to the remix
myContract = eb3.contract(address=0xCFdA6511801f3EC7C75F1750C0979A6fa1620486)