def escreva(mensagem):
    tam = len(mensagem) + 2
    print(tam*'-')
    print(f'{mensagem.center(tam)}')
    print(tam*'-')

escreva('Vitor Hugo')
escreva('RANKING DE LISTAS')