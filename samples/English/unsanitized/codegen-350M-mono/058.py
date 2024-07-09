

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if l2 is None:
        raise ValueError
    return [x for x, y in sorted(zip(l1, l2)) if x == y]
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))

#  Somente comunes, per isso tambem, o que fica a faltas no teste. 
#  
#  As informações a seguir (o que fica e sem o for) estão a definição do comentário, onde
#  os parametros obrigatórios, são as informações obtíveis na função mínimizada, e os nomes das
#  estruturas sobre o passo tú número de passos a estrutura de um loop.
#
#  Dica: Quando seu código não começa por comando que eu use o comando print. Eles irão sempre 
#  estudar, para imprimir todas os nomes de estruturas que um loop aparece:
#         for(int e in v) e o nome e i = 0, t q um loop aparece. Para que esta vez, o nome ei 
#         usado como parâmetro.
#
#          # --- --- -- *--- --- --- -- --- --- --- --- --- --- --- --- --- --- 

