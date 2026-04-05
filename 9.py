def get_diff_index(s1, s2):
    """Шукає індекс, де бінарні рядки відрізняються лише в одному біті."""
    diff_count = 0
    index = -1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
            index = i
    return index if diff_count == 1 else None

def quine_mccluskey(minterms, num_vars=4):
    # 1. Перетворення в бінарний формат
    groups = {}
    for m in minterms:
        b = bin(m)[2:].zfill(num_vars)
        ones = b.count('1')
        groups.setdefault(ones, set()).add(b)

    prime_implicants = set()
    
    while groups:
        new_groups = {}
        marked = set()
        keys = sorted(groups.keys())
        
        for i in range(len(keys) - 1):
            for s1 in groups[keys[i]]:
                for s2 in groups[keys[i+1]]:
                    idx = get_diff_index(s1, s2)
                    if idx is not None:
                        combined = list(s1)
                        combined[idx] = '-'
                        new_groups.setdefault(keys[i], set()).add("".join(combined))
                        marked.add(s1)
                        marked.add(s2)
        
        # Всі, що не склеїлися — первинні імпліканти
        for g in groups.values():
            for s in g:
                if s not in marked:
                    prime_implicants.add(s)
        groups = new_groups

    return sorted(list(prime_implicants))

def format_implicant(binary_str):
    """Перетворює 10-0 у x1!x2!x4"""
    res = []
    for i, char in enumerate(binary_str):
        if char == '1':
            res.append(f"x{i+1}")
        elif char == '0':
            res.append(f"!x{i+1}")
    return "".join(res)

# Твій варіант 25
minterms = [4, 5, 8, 9, 10, 11, 14, 15]
primes = quine_mccluskey(minterms)

print(f"Первинні імпліканти для F{minterms}:")
for p in primes:
    print(f"Код: {p}  ->  Вираз: {format_implicant(p)}")