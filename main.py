import numpy as np
import pandas as pd

# Dados fictícios de funcionários
funcionarios = ["Ana", "Carlos", "Beatriz", "Daniel", "Eduarda"]
horas_trabalhadas = np.array([160, 150, 170, 140, 155])  # Horas no mês
taxa_hora = np.array([30, 28, 32, 25, 27])  # Valor por hora (R$)
descontos = np.array([200, 150, 250, 100, 180])  # Descontos fixos (R$)

# Cálculo dos salários
salario_bruto = horas_trabalhadas * taxa_hora
salario_liquido = salario_bruto - descontos

# Criar um DataFrame com os dados
df_folha = pd.DataFrame({
    "Funcionário": funcionarios,
    "Horas Trabalhadas": horas_trabalhadas,
    "Valor Hora (R$)": taxa_hora,
    "Salário Bruto (R$)": salario_bruto,
    "Descontos (R$)": descontos,
    "Salário Líquido (R$)": salario_liquido
})

# Exibir a folha de pagamento
print("\n📋 Folha de Pagamento\n")
print(df_folha)

# Salvar a folha de pagamento em CSV
df_folha.to_csv("folha_pagamento.csv", index=False)
print("\n✅ Folha de pagamento salva em 'folha_pagamento.csv'")
