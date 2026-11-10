print('{:=^40}'.format(' LOJAS PREÇO BAIXO '))
comp = float(input('Preço das compras : R$'))
print('''formas de pagamento 
[1] à vista dinheiro/cheque" 
[2] à vista cartão " 
[3] 2x no cartão" 
[4] 3x ou mais no cartão ''')
opc =int(input('Qual é a sua opçâo :'))
if opc == 1 :
    avista = comp - ( comp * 10 / 100)
    print('Sua compra foi de {:.2f} reias e teve um desconto de 10 % e fica por {:.2f} reais.'.format(comp,avista)) 
elif opc == 2 :
    cartao = comp - ( comp * 5/100)
    print(' SUa compra foi de {:.2f} reais e teve um desconto de 5 % e ficara no valor de {:.2f} reais.'.format(comp,cartao))
elif opc == 3 :
    print(' sua compra não teve desconto e ficará no valor de {:.2f} reais. '.format(comp))
elif opc == 4 :
    vezes = int(input('Quantas parcelas ? '))
    juros = comp + (comp *20/100)
    parcelas = juros / vezes
    print('sua compra foi no valor de {:.2f} reais  parcelada em {}x ficará no valor de {} reias com 20 % de juros. '.format(comp,opc,parcelas)) 
else:
    print('Opção incorreta tente novamente !')