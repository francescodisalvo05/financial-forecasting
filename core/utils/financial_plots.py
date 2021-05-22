import pandas as pd
import numpy as np

import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px

import streamlit as st

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

    fig.update_layout(title=f"{company_name} STOCK PRICES",
                      showlegend=True)

    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Price")

    return fig


def plot_return_price(ticker, company_name, close):
    """
    :param ticker: (str) ticker of the company
    :param company_name: (str) name of the company
    :param close: (Series) historical close prices
    :return: (Figure) plot of the return values
                      * they're the differences among consecutive
                        close prices
    """
    return_values = [ (close[i] - close[i-1])/close[i-1] for i in range(1,len(close))]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=close.index[1:], y=return_values, name=f"{ticker} - {company_name}"))

    fig.update_layout(title="RETURN")
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Return")

    return fig

def plot_return_hist(ticker, company_name, close):
    """
    :param ticker: (str) ticker of the company
    :param company_name: (str) name of the company
    :param close: (Series) historical close prices
    :return: (Figure) plot of the return values
                      * they're the differences among consecutive
                        close prices
    """
    return_values = [ (close[i] - close[i-1])/close[i-1] for i in range(1,len(close))]
    group_labels = ['Return value']

    bin_size = (np.max(return_values) - np.min(return_values) ) / 50

    fig = ff.create_distplot([return_values], group_labels, bin_size=bin_size)

    fig.update_layout(title="RETURN DISTRIBUTION")

    return fig
