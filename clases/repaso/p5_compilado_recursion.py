def bit_rec(n, exp):
    # Si 2 elevado a la exp es mayor o igual que n, retorna ese valor
    if 2**exp >= n:
        return 2**exp
    # Si no, llama recursivamente a la funcion aumentando exp en 1
    return bit_rec(n, exp+1)