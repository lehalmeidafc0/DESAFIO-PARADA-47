import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame com os dados da planilha
data = {
    "Dias da semana": ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"],
    "Matérias": ["Português", "Matemática", "História", "Geografia", "Química", "Inglês"],
    "Alunos presentes": [29, 25, 28, 24, 22, 18],
    "Alunos com falta": [1, 5, 2, 7, 9, 13]
}

df = pd.DataFrame(data)

# Calculando as médias
media_presentes = df["Alunos presentes"].mean()
media_faltas = df["Alunos com falta"].mean()

# Identificando o dia com maior presença e maior falta
dia_maior_presenca = df.loc[df["Alunos presentes"].idxmax()]["Dias da semana"]
dia_maior_falta = df.loc[df["Alunos com falta"].idxmax()]["Dias da semana"]

# Visualizações
df.plot(x="Dias da semana", y=["Alunos presentes", "Alunos com falta"], kind="bar", figsize=(10, 6))
plt.title("Comparação de Presença e Faltas por Dia da Semana")
plt.ylabel("Número de Alunos")
plt.show()

print(f"Média de alunos presentes por dia: {media_presentes:.2f}")
print(f"Média de alunos com falta por dia: {media_faltas:.2f}")
print(f"Dia com maior presença: {dia_maior_presenca}")
print(f"Dia com maior falta: {dia_maior_falta}")
