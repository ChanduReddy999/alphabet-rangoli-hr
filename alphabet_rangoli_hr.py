"""
alphabet rangoli using python (HackerRank)
"""

 '''method 1'''

# def print_rangoli(size):
#     # your code goes here
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     data = [alpha[i] for i in range(n)]
#     items = list(range(n))
#     items = items[:-1]+items[::-1]
#     for i in items:
#         temp = data[-(i+1):]
#         row = temp[::-1]+temp[1:]
#         print("-".join(row).center(n*4-3, "-"))
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
    
    
    '''method 2'''

# def print_rangoli(size):
#     # your code goes here
#     import string
#     design = string.ascii_lowercase
#     L = []
#     for i in range(n):
#         s = "-".join(design[i:n])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
#     print('\n'.join(L[:0:-1]+L))
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
