import streamlit as st

from core.utils.financial_plots import *
from core.utils.financial_data import *
from core.utils.statistical_tests import *

st.title('FORECASTING')

ticker = 'AAPL'
company_name = 'APPLE'
close_prices = get_data(ticker)

st.plotly_chart(plot_historical_price(ticker,company_name,close_prices))

st.plotly_chart(plot_return_price(ticker,company_name,close_prices))

st.plotly_chart(plot_return_hist(ticker,company_name,close_prices))

st.markdown("""<h3>Is the signal stationary?</h3>""",unsafe_allow_html=True)
st.dataframe(perform_adfuller_test(close_prices, 0.05))

st.markdown("""<h3>Is the difference stationary?</h3>""",unsafe_allow_html=True)
return_prices = get_difference(close_prices)
st.dataframe(perform_adfuller_test(return_prices, 0.05))

st.markdown("""<h3>Test PACF</h3>""",unsafe_allow_html=True)
st.plotly_chart(plot_pacf(return_prices, nlags=100))

st.markdown("""<h3>Test ACF</h3>""",unsafe_allow_html=True)
st.plotly_chart(plot_acf(return_prices, nlags=100))
