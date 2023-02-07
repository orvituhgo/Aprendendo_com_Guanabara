teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Pedro'
teste[1] = 22
print(teste)
#para criar uma ligação
#galera.append(teste)
#para copiar deve ser galera.append(teste[:])
galera.append(teste[:])
print(galera)
#teste.clear limpa os dados da lista teste