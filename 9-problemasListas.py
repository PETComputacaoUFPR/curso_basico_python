original = [[2,3], [4,5]]
copiaSuperficial = original.copy()
copiaSuperficial[1][0] = 2000

print(original)

import copy # para cópia profunda precisa desse import
original = [[2,3], [4,5]]
copiaProfunda = copy.deepcopy(original)
copiaProfunda[1][0] = 2000

print(original)