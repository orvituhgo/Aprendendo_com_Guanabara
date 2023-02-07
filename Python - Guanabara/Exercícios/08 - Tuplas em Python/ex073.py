tabela = ('Palmeiras', 'Internacional', 'Fluminense',
          'Corinthians', 'Flamengo', 'Athletico-PR',
          'Atlético-MG', 'Fortaleza', 'São Paulo',
          'América-MG', 'Botafogo', 'Santos', 'Goiás',
          'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC',
          'Atlético-GO', 'Avaí', 'Juventude')
print(f'Os 20 primeiros time do brasileirão são:')
for pos, time in enumerate(tabela):
    print(f'posição {pos+1} - {time}')
print('Os 5 primeiros times são')
for pos, time in enumerate(tabela[:5]):
    print(f'posição {pos+1} - {time}')
print('Os times organizado em ordem alfabética são:')
for time in sorted(tabela):
    print(f'{time}')
print(f"O Cuiabá está na posição {tabela.index('Cuiabá')+1}")
