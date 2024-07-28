from os import path

NUMBERS_FILE = path.join(path.dirname(__file__), "c-input.in")


def sheep_sleeper() -> list[str]:

    with open(NUMBERS_FILE) as file:
        T = int(file.readline())
        N_LIST = [int(line) for line in file.readlines()]

    if T < 1 or T > 100:
        raise ValueError(f"Infringed T constrains: 0 <= T <= 200; N = {T}")

    check_digits = set("0123456789")

    reults: list[str] = []
    for i in range(T):
        N = N_LIST[i]
        if N < 0 or N > 200:
            raise ValueError(f"Infringed T constrains: 1 <= T <= 100; T = {T}")
        if N == 0:
            reults.append("INSOMNIA")
        else:
            seen_digits = set()
            multiplier = 1
            while seen_digits != check_digits:
                product = N * multiplier
                seen_digits.update(str(product))
                multiplier += 1
            reults.append(str(product))
    return reults


if __name__ == "__main__":
    for case, output in enumerate(sheep_sleeper()):
        print(f"Case #{case+1}: {output}")
