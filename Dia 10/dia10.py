import pandas as pd
import numpy as np

#agrupanmento dos salarios por departamento
data={
 'nome': ['ana', 'josy', 'Maria', 'Pedro', 'Lucas', 'Carla'],
 'Departamento': ['TI', 'RH', 'TI', 'financeiro', 'TI', 'RH'],
 'salário': [5000,2500,5200,6000,4800,4700]
}

df = pd.DataFrame(data)

#filtragem dos funcionarios de TI
funcionarios_ti = df[df['Departamento'] == 'TI']
print(funcionarios_ti)

#media salarial
media_salaria = funcionarios_ti['salario' ].mean()

#exibindo o resultado
print(f"Média salarial dos funcionarios de TI: {media_salarial}")
