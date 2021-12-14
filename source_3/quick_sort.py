def quick_sort (array, left, right) {
    if (left >= right){
        return
    }
    low = left
    high = right
    key = array[low]
    while (left < right){
        while (left < right and array[right] > key){
            right--
        }
        array[left] = array[right]
        while (left < right and array[left] <= key){
            left++
        }
        array[right] = array[left]
    }
    array[right] = key
    x = left - 1
    y = left + 1
    quick_sort(array, low, x)
    quick_sort(array, y, high)
}

a = [1, 2, 4, 3, 6, 5, 3, 7]
b = len(a) - 1
quick_sort(a, 0, b)

print(a)
