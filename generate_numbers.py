import random

def generate_numbers():
    numbers = []
    while True:
        numbers = [random.randint(10, 140) for _ in range(20)]
        total = sum(numbers)
        if total == 2500:
            break
    return numbers

# 乱数の生成と合計の確認
numbers = generate_numbers()
print("Generated numbers:", numbers)
print("Sum:", sum(numbers))