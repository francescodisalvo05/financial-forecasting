from statsmodels.tsa.arima_model import ARIMA
import plotly.graph_objects as go
import streamlit as st

def make_prediction(time_series):
    """
    :param close:
    :param p:
    :param d:
    :param q:
    :return:
    """

    n = int(len(time_series) * 0.8)
    train = time_series.iloc[:n]
    test = time_series.iloc[n:]

    model = ARIMA(train, order=(2,2,2))
    results = model.fit(disp=0)
    #summary = results.summary()[1]

    steps = len(test)
    fc, A, B = results.forecast(steps)

    st.dataframe(fc)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_series.index, y=time_series, name=f"Stock"))
    fig.add_trace(go.Scatter(x=time_series[n:].index, y=fc, name=f"Stock"))

    return fig








