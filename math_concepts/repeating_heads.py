'''file_name'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=W0621
print(" ")

'''

Type of Question:
- math concept

Question:
- You’re considering a $100 bet with your friend. 
- If n consecutive fair coin flips 
result in all heads, then you win 
- else your friend wins. 
- Your friend agrees to let you attempt the bet 
as many times as you’d like. 
- Assuming you attempt the bet x times,
what's the probability that you’ll win the bet at least once? 
- As well, what should your winning payout ($100, $200, etc)
be to ensure that you at least break even 
given unlimited attempts of the bet?

Input:
- the number of consecutive coin flips (n)
- the number of bet attempts (x) 

Clarifying Questions / Insights:
- You can assume a fair coin.
- You shouldn't use any libraries.
- automatically round output values to the 4th decimal.
	
- If I knew / had this....
	-

Output:
- the probability that you win at least once
- your required winning payout
'''

'''
Algo Time: O() | # Space: O():
-
-
    - Input:
        -
        -
    - Output:
'''

# Time: O() | # Space: O()
def repeating_heads(n, x):
    bet_size = 100
    heads_chance = 1/2

    trail_win_chance = heads_chance ** n
    trail_lose_chance = 1 - trail_win_chance

    repeated_trail_lose_chance = trail_lose_chance ** x
    repeated_trail_win_chance = 1 - repeated_trail_lose_chance

    break_even_point = bet_size / repeated_trail_win_chance

    return [repeated_trail_win_chance*100, break_even_point]

n = 3
x = 5
print("n:", n)
print("x:", x)
print("repeating_heads:", repeating_heads(n, x))
print(" ")

n = 7
x = 87
print("n:", n)
print("x:", x)
print("repeating_heads:", repeating_heads(n, x))
print(" ")

n = 10
x = 1
print("n:", n)
print("x:", x)
print("repeating_heads:", repeating_heads(n, x))
print(" ")

# _recursion
# _iteration
print(" ")
