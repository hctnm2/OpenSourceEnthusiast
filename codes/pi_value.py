from decimal import Decimal, getcontext

getcontext().prec = 1000
# max possible digits = 1000


def pi_d(n_d: int) -> Decimal:
    k = Decimal(1)

    # Initialize sum
    s = Decimal(0)

    for i in range(1000000):
        # increase value inside the range to increase accuracy of the value of pi

        # even index elements are positive
        if i % 2 == 0:
            s += 4 / k
        else:

            # odd index elements are negative
            s -= 4 / k

        # denominator is odd
        k += 2
    return round(s, n_d)


if __name__ == "__main__":
    num = int(input("\nEnter the num of digits (0-999): "))
    final_result = pi_d(num)
    print(f"Values of pi to the {num} decimal places is :\n\n {final_result} \n")
