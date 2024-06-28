import sqlite3
import pandas as pd
import plotly.express as px
# Create your connection.
cnx = sqlite3.connect('../unbook/db.sqlite3')

# Read table into DataFrame
users_df = pd.read_sql_query("SELECT * FROM app_cadastro_perfilusuario;", cnx)
turmas_df = pd.read_sql_query("SELECT * FROM materias_turma;", cnx)

print(len(users_df))
print(turmas_df.head(10))
print(turmas_df.columns)
print(len(turmas_df))

codigos = turmas_df["materia_id"].apply(lambda x: x[:3])
print("-="*15)
print(codigos)

fig = px.histogram(codigos, x='materia_id', title='Histogram of Parsed Strings', log_y=True)

# Show the plot
fig.show()

