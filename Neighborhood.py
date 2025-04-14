import numpy as np


def neighbor(array, i, j):

    if i == 0 and j == 0:
        top_left = "999"
        top_middle = "999"
        top_right = "999"

        middle_left = "999"
        middle_right = array[i + 1][j]

        bottom_left = "999"
        bottom_middle = array[i][j + 1]
        bottom_right = array[i + 1][j + 1]


    elif j == 0:
        top_left = "999"
        top_middle = array[i][j - 1]
        top_right = array[i + 1][j - 1]

        middle_left = "999"
        middle_right = array[i + 1][j]

        bottom_left = "999"
        bottom_middle = "999"
        bottom_right = "999"

    elif i == 0 and j == len(array) - 1:
        top_left = "999"
        top_middle = "999"
        top_right = "999"

        middle_left = array[i-1][j]
        middle_right = "999"

        bottom_left = array[i - 1][j + 1]
        bottom_middle = array[i][j + 1]
        bottom_right = "999"

    elif i == (len(array) - 1) and j ==(len(array) - 1):
        top_left = array[i - 1, j - 1]
        top_middle = array[i][j - 1]
        top_right = "999"

        middle_left = array[i-1][j]
        middle_right = "999"

        bottom_left = "999"
        bottom_middle = "999"
        bottom_right = "999"

    elif i == (len(array) - 1):
        top_left = array[i - 1, j - 1]
        top_middle = array[i][j - 1]
        top_right = "999"

        middle_left = array[i-1][j]
        middle_right = "999"

        bottom_left = array[i - 1][j + 1]
        bottom_middle = array[i][j + 1]
        bottom_right = "999"

    elif i == 999:
        top_left = '999'
        top_middle = array[i][j - 1]
        top_right = array[i + 1][j - 1]

        middle_left = '999'
        middle_right = array[i + 1][j]

        bottom_left = '999'
        bottom_middle = array[i][j + 1]
        bottom_right = array[i + 1][j + 1]

    elif j == (len(array) - 1):
        top_left = array[i - 1, j - 1]
        top_middle = array[i][j - 1]
        top_right = array[i + 1][j - 1]

        middle_left = array[i - 1][j]
        middle_right = array[i + 1][j]

        bottom_left = "999"
        bottom_middle = "999"
        bottom_right = "999"

    elif j == "999":
        top_left = "999"
        top_middle = "999"
        top_right = "999"

        middle_left = array[i - 1][j]
        middle_right = array[i + 1][j]

        bottom_left = array[i - 1][j + 1]
        bottom_middle = array[i][j + 1]
        bottom_right = array[i + 1][j + 1]
    else:
        top_left = array[i-1,j-1]
        top_middle = array[i][j-1]
        top_right = array[i+1][j-1]

        middle_left = array[i-1][j]
        middle_right = array[i+1][j]

        bottom_left = array[i-1][j+1]
        bottom_middle = array[i][j+1]
        bottom_right = array[i + 1][j + 1]


    moore_neighborhood = (
        int(top_left), int(top_middle), int(top_right), int(middle_left), int(middle_right), int(bottom_left),
        int(bottom_middle), int(bottom_right))
    return moore_neighborhood



def main():
    arr = np.arange(81).reshape(9,9)
    print(arr)
    print(neighbor(arr,0,0)) # change to test

if __name__ == '__main__':
    main()
