from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np

import streamlit as st

def perform_adfuller_test(series, confidence_level):
    """
    :param series: (Series) time series that we want to check
    :param confidence_level: (float) confidence level for the current test
    """
    result = adfuller(series, autolag='AIC')

    ADF_Statistic = result[0]
    p_value = result[1]
    stationary = p_value < confidence_level

    df = pd.DataFrame({'ASD Statistic' : [ADF_Statistic], 'p-value' : [p_value], 'stationary' : [stationary]})

    return df