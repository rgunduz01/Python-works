def perfect_num(n):
 return n==sum([i for i in range(1,n)if n%i==0])


#According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
#Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
#Türkçesi: Eğer sayının kendisi hariç bölenlerinin toplamı kendisine eşitse  o  "Perfect Number"dır.
#Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
#The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
#This is followed by the perfect numbers 496 and 8128