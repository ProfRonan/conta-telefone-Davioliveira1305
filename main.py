"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    ligacoes = int(input('Digite o número de ligações feitas no mês: '))
    a = 200
    b = float(200 + (ligacoes - 100) * (0.60))
    c = float(230 + (ligacoes - 150) * (0.50))
    d = float(255 + (ligacoes - 200) * (0.40))
    if ligacoes <= 100:
      print(f'O valor devido é R$ {a:.2f}.')
    elif ligacoes > 100 and ligacoes <= 150:
      print(f'O valor devido é R$ {b:.2f}.')
    elif ligacoes > 150 and ligacoes <= 200:
      print(f'O valor devido é R$ {c:.2f}.')
    else:
      print(f'O valor devido é R$ {d:.2f}.')

if __name__ == '__main__':
    main()
