def exemplo01():
    num_a = float(input("Informe o primeiro numero: "))
    num_b = int(input("Informe o segundo numero: "))

    print('{} + {} = {}'.format(num_a, num_b, num_a+num_b))
    print(type(num_a))

def exemplo_none():
    variavel = 'None'
    print(variavel)
    print(type(variavel))

    print(variavel is None)

    print('-'*10)
    print(3 < 2)
    print(not (3 < 2))
    print('-'*10)


# if <condição>:
#    <comando>
# numero = int(input('Por favor, informe um número: '))
# if numero < 0:
#     print('O número informado é NEGATIVO!')
# elif numero > 0:
#     print('O número informado é POSITIVO!')
# else:
#     print('O número informado é NULO!')
#
# print('Fim do programa')

# Falso: 0, strings vazias, None, ou, False
# True: !0, strings não vazias, qualquer objeto, True
# tente implementar a mensagem que está no chat.
# nevando = 10
# temp = -1
# temp = input('Informme a temperatura')
# if temp < 0:
#     print('Está muito frio!! Quase congelando')
#     if nevando:
#         print('\tUtilize botas!')
#     print('Tome um chocolate bem quente!!')
#
# print('Até logo!!!')

# idade = int(input('Informe a idade:'))
# if idade > 12 and idade < 20:
#     print('Adolescente')
# else:
#     print('Não adoc')


