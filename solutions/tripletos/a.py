import tripletos_pitagoricos as tp1
import tripletos_pitagoricos_v2 as tp2
import tripletos_pitagoricos_v3 as tp3

from timeit import repeat

def benchmark(func, *args, repeat_count=5):
    tempos = repeat(lambda: func(*args), number=1, repeat=repeat_count)
    return min(tempos)

TARGET = 1_000

t1 = benchmark(tp1.solve, TARGET)
t2 = benchmark(tp2.solve, TARGET)
t3 = benchmark(tp3.solve, TARGET)

print(f'Solução padrão     : {t1:.6f} segundos.')
print(f'Solução otimizada  : {t2:.6f} segundos.')
print(f'Solução otimizada++: {t3:.6f} segundos.')

