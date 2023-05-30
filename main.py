def mergeList(num1, num2):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    num1 = [1, 3, 5, 7]
    num2 = [2, 4, 6, 8]
    merged = mergeList(num1, num2)
    print(f'The merged list is {merged}')

    num1 = [1, 2, 3, 4]
    num2 = [5, 6, 7, 8]
    merged = mergeList(num1, num2)
    print(f'The merged list is {merged}')

    num1 = [5, 10, 25, 75, 85]
    num2 = [45, 55, 60]
    merged = mergeList(num1, num2)
    print(f'The merged list is {merged}')


if __name__ == '__main__':
    main()
