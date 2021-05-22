import pandas as pd
import numpy as np

import plotly.graph_objects as go

def plot_historical_price(ticker,company_name, close):
    """
    :param ticker: (str) ticker of the company
    :param company_name: (str) name of the company
    :param close: (Series) historical close prices
    :return: (Figure)
    """
    rolling_mean = close.rolling(window=30).mean()
    rolling_std = close.rolling(window=30).std()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=close.index, y=close, name=f"{ticker} - {company_name}"))
    fig.add_trace(go.Scatter(x=rolling_mean.index, y=rolling_mean, name=f"Rolling mean"))
    fig.add_trace(go.Scatter(x=rolling_std.index, y=rolling_std, name=f"Rolling std"))

    fig.update_layout(showlegend=True)

    return fig
