import sqlite3
import pandas as pd
import plotly.express as px
# Create your connection.
cnx = sqlite3.connect(r"C:\Users\Alunos\Desktop\pedro\Projeto-ds\unbook\db.sqlite3")

# Read table into DataFrame
users_df = pd.read_sql_query("SELECT * FROM app_cadastro_perfilusuario;", cnx)
professor_df = pd.read_sql_query("SELECT * FROM materias_professor;", cnx)
materias_df = pd.read_sql_query("SELECT * FROM materias_materia;", cnx)
turmas_df = pd.read_sql_query("SELECT * FROM materias_turma;", cnx)
comentario_df = pd.read_sql_query("SELECT * FROM materias_comentario;", cnx)

print(f'Coletamos  {len(professor_df)} professores e {len(materias_df)} materias com {len(turmas_df)} turmas diferentes no web scrapping')
print('--'*25)
print(f'Tivemos {len(users_df)} cadastros feitos, {len(comentario_df)} comentários feitos. Tivemos {turmas_df["numero_avaliacoes"].sum()} avaliaçõesde matérias')
print("-="*25)
print(comentario_df.columns)
texto = ''
for e in comentario_df.iterrows():
    texto += e[1]["texto"]

texto = texto.replace(" que", " ")

with open("texto_comentarios.txt", "w", encoding="utf-8") as fp:
    fp.write(texto)
  
#print(turmas_df.columns)





