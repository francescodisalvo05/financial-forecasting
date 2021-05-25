import yfinance as yf

import datetime

import pandas as pd


def get_data(ticker=None, start=None):
    """
    :param ticker:  (str) ticker of the stock
    :param start:   (str) interval that the user want to show
    :return: (Series) historical prices for the selcted stock in the
                      selected time interval
    """
    if not start:
        today = datetime.datetime.now()
        start = today - datetime.timedelta(days=720)

    if not ticker:
        return  None
    else:
        return yf.download(ticker, start=start)['Adj Close']

def get_difference(close):
    """
    :param close: (Series) close prices for the selcted stock
    :return: (Series) close differences (close[t]-close[t-1]
    """
    return pd.Series([(close[i] - close[i-1])/close[i-1] for i in range(1,len(close))])


