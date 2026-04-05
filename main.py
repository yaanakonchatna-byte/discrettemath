import pandas as pd
from sympy import symbols, Equivalent, And, Implies, Nand, simplify_logic

def solve_task_8():
    # 1. Визначаємо змінні та функцію
    A, B, C, D = symbols('A B C D')
    expr1 = Equivalent(A, And(B, C))
    expr2 = Implies(A, D)
    f_expr = Nand(expr1, expr2)

    # 2. Побудова карти Карно
    gray_code = [(0, 0), (0, 1), (1, 1), (1, 0)]
    labels = ["00", "01", "11", "10"]
    matrix = []
    for ab in gray_code:
        row = []
        for cd in gray_code:
            res = f_expr.subs({A: ab[0], B: ab[1], C: cd[0], D: cd[1]})
            row.append(int(bool(res)))
        matrix.append(row)

    kmap_df = pd.DataFrame(matrix, index=labels, columns=labels)
    kmap_df.index.name = 'AB \ CD'

    # 3. Мінімізація (Виправлено: 'knf' -> 'cnf')
    min_dnf = simplify_logic(f_expr, form='dnf')
    min_knf = simplify_logic(f_expr, form='cnf')

    # 4. Підрахунок складності (кількість змінних/літер)
    def count_literals(expr):
        # Рахуємо лише символи A, B, C, D у виразі
        s = str(expr)
        return sum(s.count(char) for char in "ABCD")

    complexity_dnf = count_literals(min_dnf)
    complexity_knf = count_literals(min_knf)

    # 5. Вивід результатів
    print("--- 1. КАРТА КАРНО ---")
    print(kmap_df)
    print("\n--- 2. МІНІМІЗАЦІЯ ---")
    print(f"мінДНФ: f = {min_dnf}")
    print(f"мінКНФ: f = {min_knf}")
    print("\n--- 3. ПОРІВНЯННЯ СКЛАДНОСТІ ---")
    print(f"Складність мінДНФ: {complexity_dnf} літер(и)")
    print(f"Складність мінКНФ: {complexity_knf} літер(и)")
    
    if complexity_dnf < complexity_knf:
        print("\nВисновок: мінДНФ є раціональнішою.")
    elif complexity_knf < complexity_dnf:
        print("\nВисновок: мінКНФ є раціональнішою.")
    else:
        print("\nВисновок: Обидві форми мають однакову складність.")

if __name__ == "__main__":
    solve_task_8()