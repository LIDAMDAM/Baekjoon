import sys
input = sys.stdin.readline

pokemon_count, question_count = map(int, input().strip().split())

pokemon_dict_k = {}
pokemon_dict_v = {}
for key in range(1, pokemon_count+1):
    value = input().strip()
    pokemon_dict_k[key] = value
    pokemon_dict_v[value] = key


question_list = [input().strip() for _ in range(question_count)]
result = []

for i in range(question_count):
    if question_list[i].isdigit(): result.append(pokemon_dict_k[int(question_list[i])])
    else: result.append(pokemon_dict_v[question_list[i]])

print('\n'.join(map(str, result)))