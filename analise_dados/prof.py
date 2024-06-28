import sqlite3
import pandas as pd
import plotly.express as px

def notas_prof(linha):
    print(linha)
    index = linha.index
    global turmas
    turma_prof = turmas[turmas["professor_id"] == linha.nome]
    df ={}
    aval_didatica = 0
    aval_apoio = 0
    aval_dificuldade = 0
    total = 0

    print(turma_prof.columns)
    for i, turma in turma_prof.iterrows():
        quant_avaliadores = turma.numero_avaliacoes
        aval_apoio += turma.avaliacao_apoio_aluno * quant_avaliadores
        aval_dificuldade += turma.avaliacao_dificuldade * quant_avaliadores
        aval_didatica += turma.avaliacao_didatica * quant_avaliadores
        total += quant_avaliadores

    if total>0:
        linha.aval_apoio = (aval_apoio //total)/2
        linha.aval_dificuldade = (aval_dificuldade //total)/2
        linha.aval_didatica = (aval_didatica //total)/2
        linha.total_avaliadores = total
        # df["aprovacao"] = ((int(ob_prof.aprovacoes.count())*100)//total)
    else:
        linha.aval_apoio = 0
        linha.aval_dificuldade =0
        linha.aval_didatica = 0
        linha.total_avaliadores = total
        # context["aprovacao"] = 0

# Create your connection.
cnx = sqlite3.connect('../unbook/db.sqlite3')

# Read table into DataFrame
prof_df = pd.read_sql_query("SELECT * FROM materias_professor;", cnx)
turmas = pd.read_sql_query("SELECT *  FROM materias_turma;", cnx)
print(turmas.columns)
prof_df["aval_apoio"] = pd.NA
prof_df["aval_dificuldade"] = pd.NA
prof_df["aval_didatica"] = pd.NA
prof_df["total_avaliadores"] = pd.NA

prof_df.apply(notas_prof, axis=1)


#print(turma_prof.head(100))

print(prof_df.head(100))
prof_df.to_excel("tabela_prof.xlsx")

