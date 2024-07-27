from os import path

NUMBERS_FILE = path.join(path.dirname(__file__), "c-input.in")


def sheep_sleeper(T: int):
    if T < 1 or T > 100:
        raise ValueError("T must be >= 1 and <= 100")
    numbers = [int(w.strip()) for w in open(NUMBERS_FILE)]
    check_digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    results = []

    def check_for_one_test(test_number: int):
        seen_numbers = set()
        # If N can be equal to 0 as the exercise ask (0 ≤ N ≤ 200), the the examples given were wrong.
        # For example the 11 case, as it starts from 0, then just need to take N to 9 to reach all digits.
        # So the answer in 11 case must be 99 instead of 110.
        # Im using 1 <= N <= 200
        for N in range(1, 201):
            product = test_number * N
            for digit in set(str(product)):
                seen_numbers.add(int(digit))
            if check_digits.issubset(seen_numbers):
                return product
        return "INSOMNIA"

    # checking for all tests numbers
    for test_number in numbers[:T]:
        results.append(check_for_one_test(test_number))
    return results


if __name__ == "__main__":
    print(sheep_sleeper(100))
