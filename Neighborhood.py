import numpy as np


def neighbor(array, i, j):

    if i == 0 and j == 0:
        top_left = '999'
        top_middle = '999'
        top_right = '999'

        middle_left = '999'
        middle_right = array[i + 1][j]

        bottom_left = '999'
        bottom_middle = array[i][j + 1]
        bottom_right = array[i + 1][j + 1]


    elif i == 0 and j == len(array[0]) - 1:
        top_left = '999'
        top_middle = array[i][j - 1]
        top_right = array[i + 1][j - 1]

        middle_left = '999'
        middle_right = array[i + 1][j]

        bottom_left = '999'
        bottom_middle = '999'
        bottom_right = '999'

    elif i == len(array) - 1 and j == 0:
        top_left = '999'
        top_middle = '999'
        top_right = '999'

        middle_left = array[i-1][j]
        middle_right = '999'

        bottom_left = array[i - 1][j + 1]
        bottom_middle = array[i][j + 1]
        bottom_right = '999'

    elif i == (len(array) - 1) and j ==(len(array[0]) - 1):
        top_left = array[i - 1, j - 1]
        top_middle = array[i][j - 1]
        top_right = '999'

        middle_left = array[i-1][j]
        middle_right = '999'

        bottom_left = '999'
        bottom_middle = '999'
        bottom_right = '999'

    elif i == (len(array) - 1):
        top_left = array[i - 1, j - 1]
        top_middle = array[i][j - 1]
        top_right = '999'

        middle_left = array[i-1][j]
        middle_right = '999'

        bottom_left = array[i - 1][j + 1]
        bottom_middle = array[i][j + 1]
        bottom_right = '999'

    elif i == 0:
        top_left = '999'
        top_middle = array[i][j - 1]
        top_right = array[i + 1][j - 1]

        middle_left = '999'
        middle_right = array[i + 1][j]

        bottom_left = '999'
        bottom_middle = array[i][j + 1]
        bottom_right = array[i + 1][j + 1]

    elif j == (len(array[0]) - 1):
        top_left = array[i - 1, j - 1]
        top_middle = array[i][j - 1]
        top_right = array[i + 1][j - 1]

        middle_left = array[i - 1][j]
        middle_right = array[i + 1][j]

        bottom_left = '999'
        bottom_middle = '999'
        bottom_right = '999'

    elif j == 0:
        top_left = '999'
        top_middle = '999'
        top_right = '999'

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

        moore_neighborhood = {
            int(top_left):(i-1,j-1),
            int(top_middle): (i,j-1),
            int(top_right):(i+1,j-1),
            int(middle_left):(i-1,j), int(middle_right):(i+1,j), int(bottom_left):(i-1,j+1),
        int(bottom_middle):(i+1,j), int(bottom_right):(i+1,j+1)


        }

        return moore_neighborhood.keys(), moore_neighborhood.values()







def main():
    arr = np.arange(81).reshape(9,9)
    print(arr)
    states, locations = neighbor(arr,7,7) # change to test
    print(states)
    print(locations)

if __name__ == '__main__':
    main()
