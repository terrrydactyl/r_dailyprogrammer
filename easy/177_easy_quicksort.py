def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    smaller = []
    larger = []
    for num in numbers[1:]:
        if num < pivot:
            smaller.append(num)
        else:
            larger.append(num)
    return quicksort(smaller) + [pivot] + quicksort(larger)

print quicksort([2, 4, 2, 7, 1, 3, 4])
