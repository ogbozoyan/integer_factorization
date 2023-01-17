#factrization 
import gmpy2
def factorization(a: int):
    if a<0:
        a *= -1
    divisers = []
    prime_multipluers = []
    temp = a
    i = a
    count = 0
    flag = 1
    j = 0

    if gmpy2.is_prime(a):
        return a
    for x in range(2,a):
        if i%x == 0:
            i = a/x
            divisers.append(x)
    prime_multipluers = [0]*len(divisers)
    while j<(len(divisers)):
        
       # print('---start for j---')
        if a%divisers[j] == 0:

         #   print('if %','a is ',a,'count is',count,'j is',j,'divisers[j] is' ,divisers[j])

            count += 1
            a = int(a/divisers[j])
            flag = 0 if a%divisers[j] == 0 else 1
       # print(prime_multipluers , 'prime_mul before')

        prime_multipluers[j] = count    

       # print(prime_multipluers,'prime_mul after')
        if flag == 1:
            count = 0
            j += 1

  #  print('----end for j---')
    res = f'Result : {temp} = '
    for y in range(len(prime_multipluers)):
        if prime_multipluers[y] == 0:
            res = f'{res}'
        else:
            res = res + str(divisers[y])+'^'+str(prime_multipluers[y])+' * '

    return res[:len(res)-3]
print(factorization(int(input())))
