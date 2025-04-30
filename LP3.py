def selection_sort(array):
    size=len(array)

    for i in range(size-1):
        min_index=i;

        for j in range(i+1, size):
            if(array[j] < array[min_index]):
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

def print_array(array):
    for value in array:
        print(value, end=" ")
    print()

# Main execution
if __name__ == "__main__":
    data = [20, 12, 10, 15, 2]
    selection_sort(data)
    print("Sorted array in Ascending Order:")
    print_array(data)