
#Write an algorithm that takes an array and
 #moves all of the zeros to the end, 
 #preserving the order of the other elements.

 def move_zeros(array):
    a=[0 for a in range(array.count(0))]
    b=[i for i in array if i!=0 ] 
    b.extend(a)
    return (b)