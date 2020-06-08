def mensagem_boas_vindas():
    print('\tSeja bem vindo ao fantástico mundo de Python!!')
    mensagem_boas_vindas2()


def mensagem_boas_vindas2():
    print('\tSeja bem vindo ao fantástico mundo de Python!!, NOVAMENTE...')


def mensagem_custom(nome):
    mensagem = 'Olá {} seja bem vindo'.format(nome)
    return mensagem


def add(a, b):
    return a + b


# MAIN
if __name__ == '__main__':
    print('Iniciando nosso código')
    mensagem_boas_vindas()
    print('Finalizando nosso código')
    print('Aqui deve aparecer o resultado da função custom: ')
    mensagem = mensagem_custom('Fabricio')
    print(mensagem)
    print('-' * 10)
    print(mensagem_custom('Miguel'))
    a = 10
    b = 20
    c = add(a, b)
    print('{} + {} = {}'.format(a, b, c))
