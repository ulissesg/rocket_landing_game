
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


'''PROBLEMA: Se o numero for divisivel por 3, retorna 'fizz',
Se o numero for divisivel por 5, retorna 'buzz'
Se o numero for divisivel por 3 e por 5, retorna 'fizzbuzz
Senao retorna o proprio'''

'''div3: int -> string'''

def fizzbuzz(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return "fizzbuzz"
    if(n % 3 == 0):
        return "fizz"
    if (n % 5 == 0):
        return "buzz"
    if (n % 3 != 0) and (n % 5 != 0):
        return n


# #listando:
# for k in range(1000):
#     print(fizzbuzz(k))


class Test(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3),"fizz"   )
        self.assertEqual(fizzbuzz(5),"buzz"   )
        self.assertEqual(fizzbuzz(15),"fizzbuzz")
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(30), "fizzbuzz")

# unittest.main()


