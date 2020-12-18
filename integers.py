#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program prints integers in the range of 1000 and 2000


def main():
    # Function prints integers in the range of 1000 and 2000

    # Process and output
    print("The integers in the range of 1000 and 2000 are: ")

    for loop_counter in range(1000, 2000 + 1):
        print(loop_counter, end=" ")

        if loop_counter % 5 == 4:
            print("")


if __name__ == "__main__":
    main()
