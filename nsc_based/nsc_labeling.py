# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:48:17 2021

@author: hanyeob
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objs as go


df = pd.read_csv(
    'https://raw.githubusercontent.com/hanyeob/fine_dust/master/nsc_total_based/scaled_data/nsc_scaled.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['tt'], y=df['CO2_outdoor'], mode='lines', name='CO2_outdoor'))
fig.add_trace(go.Scatter(
    x=df['tt'], y=df['CO2_classroom'], mode='lines', name='CO2_classroom'))
fig.add_trace(go.Scatter(
    x=df['tt'], y=df['PM2.5_outdoor'], mode='lines', name='CO2_classroom'))
fig.add_trace(go.Scatter(
    x=df['tt'], y=df['PM2.5_classroom'], mode='lines', name='CO2_classroom'))
fig.add_trace(go.Scatter(
    x=df['tt'], y=df['PM10_outdoor'], mode='lines', name='CO2_classroom'))
fig.add_trace(go.Scatter(
    x=df['tt'], y=df['PM10_classroom'], mode='lines', name='CO2_classroom'))
plot(fig)