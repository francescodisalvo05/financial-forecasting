import yfinance as yf
import datetime


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


