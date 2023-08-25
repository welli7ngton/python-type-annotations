# strings: str = "wellington"
# inteiros: int = 1234567
# _float: float = 1.23
# boleano: bool = True
# _set: set = {1, 2, 3}
# lista: list = [1, 2, 3]
# tupla: tuple = (1, 2, 3)
# dicionario: dict = {1: 2, 3: 4}


# def soma(x: int, y: int, z: float) -> float:
#     return x + y + z


# print(soma('a', 1, 2))

# lista_inteiros: list[int | str] = [1, 2, 3, 4, 5, "a"]
# lista_strings: list[str] = ['1', '2', '3', '4', '5']
# lista_tuplas: list[tuple] = [('1', 2,), (3.5, 4), (5, True)]
# lista_de_listas_de_inteiros: list[list[int]] = [[1, 2, 5], [2, 3, 4], [5]]

# dicionario: dict[str, int] = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# Alocação de tipos em variáveis
# ListaInteiros = list[int]  # Type Alias ou Generic ALias
# print(type(ListaInteiros))
# DictListasInteiros = dict[str, ListaInteiros]

# dicoinario_listas: DictListasInteiros = {
#     "a": [1, 2],
#     "b": [5, 4],
#     "c": [3, 7],
# }

# strings_e_int: str | int  # Union
# strings_e_int = "a"  # sem erro
# strings_e_int = 1  # sem erro

# lista: [str | int] = ["a", 1]

# def soma(x: int, y: float | None = None) -> float | bool:
#     if isinstance(y, float | int):
#         return x + y
#     return False


# print(soma(1, 2))


