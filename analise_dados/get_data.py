import sqlite3
import pandas as pd
import plotly.express as px
# Create your connection.
cnx = sqlite3.connect('../unbook/db.sqlite3')

# Read table into DataFrame
users_df = pd.read_sql_query("SELECT * FROM app_cadastro_perfilusuario;", cnx)
professor_df = pd.read_sql_query("SELECT * FROM materias_professor;", cnx)
materias_df = pd.read_sql_query("SELECT * FROM materias_materia;", cnx)
turmas_df = pd.read_sql_query("SELECT * FROM materias_turma;", cnx)
comentario_df = pd.read_sql_query("SELECT * FROM materias_comentario;", cnx)

print(f'Coletamos  {len(professor_df)} professores e {len(materias_df)} com {len(turmas_df)} no web scrapping')
print('--'*25)
print(f'Tivemos {len(users_df)} cadastros feitos, {len(comentario_df)} comentários feitos')



