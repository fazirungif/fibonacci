def get_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_list = [0, 1]
    for i in range(2, n):
        next_num = fib_list[i -1]+ fib_list[i -2]
        fib_list.append(next_num)
    return fib_list

def run_tests():
    tests = [
        (0, []),
        (1,[0]),
        (2, [0, 1]),
        (5, [0,1,1,2,3]),
        (8,[0,1,1,2,3,5,8,13]),
        (10, [0,1,1,2,3,5,8,13,21,34]),

    ]
    passed = 0
    failed = 0

    for n, expected in tests:
        result = get_fibonacci(n)
        if result == expected:
            print(f"Тест n={n}: ВЕРНО -> {result}")
            passed +=1
        else:
            print(f"Тест n={n}: НЕВЕРНО")
            print(f"Ожидалось: {expected}")
            print(f"Получено: {result}")
            failed += 1
    print(f"\n Итого: пройдено {passed}из {passed + failed} тестов")

run_tests()
