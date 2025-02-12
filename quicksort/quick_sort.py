import random


def partition(arr, low, high):
    pivot = arr[high]

    if len(arr) <= 1:
        return low
    i = low - 1

    for j in range(low, high):

        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)

    return i + 1


def swap(arr, firstIndex, secondSecondIndex):
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondSecondIndex]
    arr[secondSecondIndex] = temp


def quick_sort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def generate_random(max=100):
    return random.randint(1, max)


def generate_and_sort(count=20):
    for num in range(0, count):
        numbers = [generate_random() for i in range(1, count)]
        quick_sort(numbers, 0, len(numbers) - 1)
        print(numbers)


if __name__ == '__main__':
    generate_and_sort()
