import pandas as pd
import plotly.express as px


df = pd.read_excel("tabela_prof.xlsx")

fig = px.histogram(df, x="aval_apoio", title='Histogram of Parsed Strings')

fig.show()

fig = px.histogram(df, x="aval_dificuldade", title='Histogram of Parsed Strings')
fig.show()
fig = px.histogram(df, x="aval_didatica", title='Histogram of Parsed Strings')
fig.show()
fig = px.histogram(df, x="total_avaliadores", title='Histogram of Parsed Strings')
fig.show()
