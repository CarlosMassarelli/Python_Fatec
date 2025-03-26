ph=float(input('Digite um valor do PH: '))
if ph < 6.0:
    r= 'ácido'
elif ph < 7.0:
    r= 'levemente ácida'
elif ph == 7.0:
    r= 'neutra'
elif ph < 8.0:
    r= 'levemente alcalina'
else:
    r= 'alcalina'
print(f'O valor {ph} é uma solução {r}.')
# Fim

    
