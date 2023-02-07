from time import sleep

preço = float(input('Qual é o total da compra? R$'))
sleep(2)
print('ESTAMOS COM DESCONTO DEPENDENDO DA FORMA DE PAGAMENTO!\nESCOLHA SUA FORMA DE PAGAMENTO:'
      '\n1. À VISTA/DINHEIRO = 10% DE DESCONTO\n2. À VISTA NO CARTÃO = 5% DE DESCONTO\n'
      '3. EM ATÉ 2X NO CARTÃO = PREÇO FORMAL\n4. 3X OU MAIS NO CARTÃO = 20 % DE JUROS')
forma = int(input('Qual sua escolha? '))
sleep(2)
if forma == 1:
      print('Seu produto custará R${}'.format(preço * 0.9))
elif forma == 2:
      print('Seu produto custará R${}'.format(preço * 0.95))
elif forma == 3:
      print('Seu produto não terá desconto mas será parcelado em 2 vezes sem juros.')
elif forma == 4:
      print('Seu produto pode ser parcelado em + de 3 vezes e custará o total de R${}'.format(preço*1.2))
else:
      print('Opção inválida de pagamento.')
