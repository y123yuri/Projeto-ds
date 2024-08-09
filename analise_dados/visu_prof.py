import pandas as pd
import plotly.express as px


df = pd.read_excel(r"C:\Users\Alunos\Desktop\pedro\Projeto-ds\analise_dados\excel\tabela_prof.xlsx")

fig = px.histogram(df, x="aval_apoio", title='histograma avalição apoio', ).update_layout(xaxis_title="avaliação apoio", 
                   yaxis_title="quantidade de professores")

fig.show()

fig = px.histogram(df, x="aval_dificuldade", title='Histograma avaliação dificuldade', 
                    ).update_layout(xaxis_title="avaliação dificuldade",
                   yaxis_title="quantidade de professores")
fig.show()
fig = px.histogram(df, x="aval_didatica", title='Histograma avaliação didática', ).update_layout(yaxis_title="quantidade de professores",
                   xaxis_title="avaliação didática")
fig.show()
fig = px.histogram(df, x="total_avaliadores", title='histograma quantidade de avalições por professor',).update_layout(yaxis_title="quantidade de professores", 
                   xaxis_title="quantidade avaliadores")

fig.show()
