import pandas as pd
import numpy as np

data = {'vendas': [100,200,300,400,500,600,700,800,900,1000]}

df=pd.DataFrame(data)

#operações
media = df['vendas'].mean()
mediana= df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

#resultados
print("media:", media)
print("mediana:", mediana)
print("desvio padrão:", desvio_padrao)
print("maximo:", maximo)
print("minimo:", minimo)