def main():
    candidatos = {
        1: 'Jean',
        2: 'Jonathan',
        3: 'José',
        4: 'Joyce',
        5: 'Nulo',
        6: 'Branco'
    }
    votos = {key: 0 for key in candidatos}

    print('=== Sistema de Votação ===')
    print('Digite o número do seu candidato:')
    for numero, nome in candidatos.items():
        print(f'[{numero}] - {nome}')
    print('[0] - Encerrar votação')

    while True:
        try:
            escolha = int(input('\nSeu voto: '))
            if escolha == 0:
                break
            if escolha in votos:
                votos[escolha] += 1
            else:
                print('Voto inválido. Tente novamente.')
        except ValueError:
            print('Valor inválido. Digite um número.')

    print('\nResultados da votação:')
    for numero, nome in candidatos.items():
        print(f'{nome}: {votos[numero]} votos')

    vencedor = max(range(1, 5), key=lambda x: votos[x])
    print(f'\nCandidato vencedor: {candidatos[vencedor]} com {votos[vencedor]} votos')


if __name__ == '__main__':
    main()
