# infra-es-do-flash
'''
informados em placas de trânsito e não consegue se lembrar de todos, já que algumas
placas estavam mal sinalizadas ou obstruídas e ele não é conhecido por ter uma super
memória.
Entrada
A primeira linha da entrada possui dois inteiros ‘N’ (1 <= N <= 10000) e ‘M’ (1 <= M <=
N) representando, respectivamente, a quantidade de placas vistas e a quantidade das
últimas placas memorizadas por flash. A segunda linha possui ‘N’ inteiros ‘L’ (20 <= L <=
120) representando os limites de velocidade informados nas placas. Placas mal sinalizadas
ou obstruídas terão valor igual a 0.
Saída
A saída consiste nas últimas ‘M’ placas vistas (memorizadas), desconsiderando as
placas obstruídas ou bloqueadas.
Entrada Saída
5 3
10 20 30 0 50
6 2
80 50 0 0 0 0
80 50
'''
r,c=input().split()
r=int(r)
c=int(c)
p=list(map(int,input().split()))
lista=[]
listar=[]
lista3=[]
for i in p:
    if i>0:
        lista.append(i)
listar=lista[::-1]
lista3=listar[0:c]
lista3.reverse()
print(*lista3)
