# python3
import os

def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve O(n) and not O(n2)
    for i in range(n//2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    n = len(data)
    min_index = i
    l = 2*i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2*i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    input_string = input()
    input_split = input_string.split('\r\n')
    
  
    choice = input_split[0]
    if choice == "I":
        # input from keyboard
        n = input_split[1]
        data = list(map(int, input_split[2].split()))

    elif choice == "F":
        fileName = input_split[1]
        if os.path.isfile("tests/" + fileName):
            with open("tests/" + fileName, 'r') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
        else:
            print(f"File '{fileName}' does not exist.")
            return
    else:
        print("Invalid input character entered.")
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == int(n)

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
