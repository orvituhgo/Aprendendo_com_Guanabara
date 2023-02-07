
#o código abaixo faz com que ocorra tratamento de erros, isto é:
#caso o usuário não digite de maneira adequada será retornado um comando especifico para aquela situação
try:
    s = int(input('digite um número'))
except:
    print('Valor inválido')
#except SyntaxError
#except IndexError
    #entre outros
else:
    print(s)

    #usar os comandos acima para tratar erros


'''
#Aula 21 - Topícos

#Interactive help

### help()
função para ajuda, pode ser digitada no prompt
abrirá manuaias das funções, bibliotecas e tudo mais
quit() para sair

### help(print)
outra forma de usar
 
### print(input.__doc__)
outra forma de usar

#docstrings

basicamente uma string de documentação como as strings mostradas pelo comando help()
no entanto é possível criar docstring para funções criadas pelo "def" como se fosse para
explicar numa biblioteca criada por terceiro
Para criar essa documentação começa diretamente depois do comando def como abaixo dentro
das três aspas duplas'''

def contador(i,f,p):
    """
    -> Faz um contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
    
    '''

#argumentos opcionais

para demonstrar um argumento opcional deve-se declarar ele na definição da função, estes serão a opção caso não sejam
declarados nenhuma parâmetro formal (para múltiplos paramentos informar "*num") as funções existentes em python quase
 sempre possuem argumentos opcionais basta verificar com o interactive help:
'''
def contador(i,f,p=0):
    """
    -> Faz um contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

'''
#escopo das variáveis

escopo global: é quando a variável é declada sem indentação a nenhuma função in built ou terceiras, portanto poderá ser
chamda por qualquer função
escopo local: quando uma variável é crianda dentro de uma função por "def", se o valor existir no escopo global e no
escopo local, a variavel utilizará as duas de formas diferentes, a local como parametro para função e a global como
parametro de funções no bloco de comando

'''
def soma(b):
    a = 8
    b += 4
    c = 2
    print(a)
    print(b)

a = 5
soma(b) # B será 4 + 5 (do A global) e o print(a) mostrará 8 (do A local)

''' caso precise usar o valor global digie como abaixo (global [variavel]) assim o A global assumirá o valor que você 
definir dentro da função, no entanto o parâmetro ainda sim será substuido pelo valor da variavel global antes do comando 
(globa [variável])'''

def soma(b):
    global a
    a = 8
    b += 4
    c = 2
    print(a)
    print(b)

a = 5
soma(b) # B será 4 + 5 (do A global) e o A global será assumirá o valor do A local e o print(a) mostrará 8 (do A global substituido)

'''
#retorno de resultados

basta adicionar return ao inves de imprimir(print), assim a função poderá retornar aquele valor podendo até mesmo retornar
um valor verdade, caso um if seja respeitado pode retornar true ou false como for definido na codagem

'''

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
'''
# assim a função soma(a, b, c) será igual a valor, então se imprimir: print(soma(a,b,c)) = mostrará o valo da soma 
'''
r1 = soma(1, 2, 3)
print(r1) #retornará 6 (1 + 2 + 3)