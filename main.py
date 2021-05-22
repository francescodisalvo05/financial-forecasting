import streamlit as st

from core.utils.financial_plots import *
from core.utils.financial_data import *

st.title('FORECASTING')

ticker = 'AAPL'
company_name = 'APPLE'
close_prices = get_data(ticker)

st.plotly_chart(plot_historical_price(ticker,company_name,close_prices))

st.plotly_chart(plot_return_price(ticker,company_name,close_prices))

st.plotly_chart(plot_return_hist(ticker,company_name,close_prices))