amountRS = float(input('say how many amount you have in your wallet in Brazilian currency: '))
amountUS = amountRS/3.27
print('So you have {:.3f} and you can buy {:.3f} dollars now.'.format(amountRS, amountUS))
