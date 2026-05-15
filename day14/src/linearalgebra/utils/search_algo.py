#create linear search algorithm and binary search algorithm to search for a name in the search_page_names.csv file and return the index of the name if found, otherwise return -1
import pandas as pd
from linearalgebra.configurations.conf import Config

def linear_search(file_name):
    #read the csv file and store it in a dataframe
    df = pd.read_csv(file_name)
    #get the names column from the dataframe
    names = df['search_page_name'].tolist()
    #get the name to search from the user
    name_to_search = input("Enter the name to search: ")
    step = 0
    #linear search algorithm
    #print order of complexity of linear search algorithm
    print("Linear search algorithm has a time complexity of O(n).") 
    for i in range(len(names)):
        step += 1
        if names[i] == name_to_search:
            return step, i
    return step, -1

def binary_search(file_name):
    #read the csv file and store it in a dataframe
    df = pd.read_csv(file_name)
    #get the names column from the dataframe
    names = df['search_page_name'].tolist()

    #sort the names list
    names.sort()
    #get the name to search from the user
    name_to_search = input("Enter the name to search: ")
    step = 0
    #binary search algorithm
    #print order of complexity of binary search algorithm
    print("Binary search algorithm has a time complexity of O(log n).")
    left, right = 0, len(names) - 1
    while left <= right:
        step += 1
        mid = left + (right - left) // 2
        if names[mid] == name_to_search:
            return step, mid
        elif names[mid] < name_to_search:
            left = mid + 1
        else:
            right = mid - 1
    return step, -1


if __name__ == "__main__":
    search_page_names = Config.search_page_path
    print("Linear Search:")
    steps, index = linear_search(search_page_names)
    if index != -1:
        print(f"Name found at index {index} in {steps} steps.")
    else:
        print(f"Name not found after {steps} steps.")
    print("\nBinary Search:")
    steps, index = binary_search(search_page_names)
    if index != -1:
        print(f"Name found at index {index} in {steps} steps.")
    else:
        print(f"Name not found after {steps} steps.")