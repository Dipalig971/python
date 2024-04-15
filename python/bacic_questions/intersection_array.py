#Write a program to find the intersection of two arrays.

def intersection(lst1,lst2):
         lst3=[value for value in lst1 if value in lst2]
         return lst3
lst1=[4,5,6,7,8,9,3,4,5,6,7,8]
lst2=[9,8,7,6,5,4,3,2,3,4,5,6]      
print(intersection(lst1,lst2))                                                                                                    