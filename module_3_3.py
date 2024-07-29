def prim_params(a=1, b='строка', c=True):
    print(a, b, c)
    return a, b, c


values_list = [53, 'String', (4, 5, 6)]
values_dict = {'a': 53, 'b': "666", 'c': False}
values_list_2 = [54.32, 'Строка']

prim_params()
prim_params(b=25)
prim_params(c=[1, 2, 3])
prim_params(*values_list)
prim_params(**values_dict)
prim_params(*values_list_2, 42)
