'''
Name: Jordyn Kuhn
Date: 1/29/23
CRN: 23199
CIS 226: Advanced Python Programming
'''

#Class to handle the list and list related tasks
class List:
    #Initialize the class
    def __init__ (self):
        self.liste = []
        self.swapnum = 0
        self.iter = 0

    #resets the swap count and the iteration count
    def reset_counts(self):
        self.swapnum = 0
        self.iter = 0

    #prints the swap number
    def print_swap(self):
        print('Swaps: ' + str(self.swapnum))

    #Creates the list the user gave
    def create_list(self, str):
        self.liste = [int(i) for i in str.split(',')]

        return self.liste

    #Swaps the position of two numbers in an array
    def swap(self, array, num1, num2):
        self.swapnum += 1
        hold = array[num1]
        array[num1] = array[num2]
        array[num2] = hold

    #Merges two arrays
    def merge(self, arr1, arr2):
        mergelist = []
        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                mergelist.append(arr1[i])
                i += 1

            else:
                mergelist.append(arr2[j])
                j += 1
        
        if arr1:
            mergelist.extend(arr1[i:len(arr1)])

        if arr2:
            mergelist.extend(arr2[j:len(arr2)])

        return mergelist

    #Sorts a list using Merge Sort
    #Big O: O(n long(n))
    def sort_list(self, s = None, e = None):
        if s is None:
            s = 0
        
        if e is None:
            e = len(self.liste) - 1

        if e - s <= 0:
            return
        elif e - s == 1:
            if self.liste[s] > self.liste[s+1]:
                self.swap(self.liste, s, s+1)
            return
        else:
            m = s + int((e-s)/2)
            self.sort_list(s, m)
            self.sort_list(m+1, e)

            mergelist = self.merge(self.liste[s:m+1], self.liste[m+1:e+1])

            for i, value in enumerate(mergelist):
                self.liste[s+i] = value

            return self.liste

    #Searches a list using Linear Search
    #Big O: O(n)
    def search_list(self, num):
        s = 0
        e = len(self.liste) - 1
        index = -1

        while index < 0 and s <= e:
            self.iter += 1
            m = int((s+e)/2)
            
            if self.liste[m] == num:
                index = m
            elif self.liste[m] < num:
                s = m + 1
            else:
                e = m - 1

        print('Iterations: ' + str(self.iter))
        if index != -1:
            return 'Found at position ' + str(index)
        return 'Provided number not in list'
    

