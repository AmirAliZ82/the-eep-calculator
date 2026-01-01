import numpy as np
# from math import e

print('Welcome to the EEP Calculator v01 developed by Zillucci, AmirAli.')
tp = input('What type of process you require?\nPlease write one of the following:\nF_P\nP_F\nF_A\nA_F\nP_A\nA_F\nP_G\nA_G\nF_G\nMore advanced ones:\nie\nrg\ni_F_P\ni_F_A\ni_P_A\nn_F_P\nn_F_A\nn_P_A\nP_A_g\nF_A_g: ')

#1. F_P_def
def F_P(i, n, P):
    F = P*(1+i)**n
    print('The F_value is: ' + str(F))

#2. P_F_def
def P_F(i, n, F):
    P = F/(1+i)**n
    print('The P_value is: ', {P})

#3. F_A_def
def F_A(i, n, A):
    F = A*((1+i)**(n)-1)/i
    print('The F_value is: ' + str(F))

#4. A_F_def
def A_F(i, n, F):
    A = F*i/((1+i)**(n)-1)
    print('The A_value is: ' + str(A))

#5. P_A_def
def P_A(i, n, A):
    P = A*((1+i)**(n)-1)/(i*(1+i)**n)
    print('The P_value is: ' + str(P))

#6. A_P_def
def A_P(i, n, P):
    A = P*(i*(1+i)**n)/((1+i)**(n)-1)
    print('The A_value is: ' + str(A))

#7. P_G_def
def P_G(i, n, G):
    P = ((G/i)*((((1+i)**(n)-1)/(i*(1+i)**n))-n/(1+i)**n))
    print('The P_value is: ' + str(P))

#8. A_G_def
def A_G(i, n, G):
    A = G*((1/i)-((n)/((1+i)**(n)-1)))
    print('The A_value is: ' + str(A))

#9. F_G_def
def F_G(i, n, G):
    F = G*((1/i)*(((1+i)**(n)-1)/i)-n)
    print('The F_value is: ' + str(G))

#10. ie_def
def ie(i, n):
    ie = ((1+i/n)**n)-1
    print('The Effective Annual Interest Rate is: ' + str(ie))

#11. rg_def
def rg(n, r1, r2, r3, r4, r5):
    rg = ((1+r1)*(1+r2)*(1+r3)*(1+r4)*(1+r5))**(1/n)-1
    print('The Geometric Mean is: ' + str(rg))


#12. i_F_P_def
def i_F_P(n, F, P):
    i = (F/P)**(1/n)-1
    print('The Interest Rate is: ' + str(i))

#13. i_F_A_def
def i_F_A(n, F, A, ac):
    g = []
    t = []
    r = 10 ** ac

    for a in range (1, r):
        i = 1 - 10**(-ac) * a
        result = A*((1+i)**(n)-1)/i
        if result > F:
            t.append(i)
            t.append(result)
            # print(t)
            g.append(t)
            t = []
            g = g[-1]
            continue
        else:
            break
    print(g)

    # print('The Estimated Interest Rate is: ' + str(g[0]))


#14. i_P_A_def
def i_P_A(n, P, A, ac):
    g = []
    t = []
    r = 10 ** ac

    for a in range (1, r + 1):
        i = 10**(-ac) * a
        result = A*((1+i)**(n)-1)/(i*(1+i)**n)
        if result > P:
            t.append(i)
            t.append(result)
            # print(t)
            g.append(t)
            t = []
            g = g[-1]
            continue
        else:
            break
    print(g)

    print('The Estimated Interest Rate is: ' + str(g[0]))


#15. n_F_P_def
def n_F_P(i, F, P):
    n = (np.log(F/P))/(np.log(1+i))
    print('The Number of interest periods is: ' + str(n))

#16. n_F_A_def
def n_F_A(i, F, A):
    n = (np.log(((F*i)/A)+1))/(np.log(1+i))
    print('The Number of interest periods is: ' + str(n))

#17. n_P_A_def
def n_P_A(i, P, A):
    n = (-1*np.log(1-(P*i/A))/np.log(1+i))
    print('The Number of interest periods is: ' + str(n))

#18. P_A_g_def
def P_A_g(n, i, g, A):
    if i != g:
        P = A*(1-((1+g)**n)*((1+i)**-n))/(i-g)
    else:
        P = n*A*((1+i)**-1)
    print('The P_value is: ' + str(P))

#19. F_A_g_def
def F_A_g(n, i, g, A):
    if i != g:
        F = A*((((1+i)**n)-((1+g)**n))/(i-g))
    else:
        F = n*A*((1+i)**n-1)
    print('The F_value is: ' + str(F))

#1. F_P
if tp == 'F_P':
    F_P(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    P = float(input('Determine P: '))  
    )

#2. P_F
elif tp == 'P_F':
    P_F(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    F = float(input('Determine F: '))  
    )

#3. F_A
elif tp == 'F_A':
    F_A(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    A = float(input('Determine A: '))  
    )

#4. A_F
elif tp == 'A_F':
    A_F(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    F = float(input('Determine F: '))  
    )

#5. P_A
elif tp == 'P_A':
    P_A(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    A = float(input('Determine A: '))  
    )

#6. A_P
elif tp == 'A_P':
    A_P(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    P = float(input('Determine P: '))  
    )   

#7. P_G
elif tp == 'P_G':
    P_G(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    G = float(input('Determine G: '))  
    )   

#8. A_G
elif tp == 'A_G':
    A_G(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    G = float(input('Determine G: '))  
    )   

#9. F_G
elif tp == 'F_G':
    F_G(
    i = float(input('Determine i: ')),
    n = float(input('Determine n: ')),
    G = float(input('Determine G: '))  
    )   

#10. ie
elif tp == 'ie':
    ie(
    i = float(input('Determine nominal i: ')),
    n = float(input('Determine n: ')), 
    )

#11. rg
elif tp == 'rg':
    rg(
    n = float(input('Determine n: ')), 
    r1 = float(input('Determine nominal r1: ')),
    r2 = float(input('Determine nominal r2: ')),
    r3 = float(input('Determine nominal r3: ')),
    r4 = float(input('Determine nominal r4: ')),
    r5 = float(input('Determine nominal r5: '))
    )

#12. i_F_P
elif tp == 'i_F_P':
    i_F_P(
    n = float(input('Determine n: ')),
    F = float(input('Determine F: ')),
    P = float(input('Determine P: '))
    )

#13. i_F_A
elif tp == 'i_F_A':
    i_F_A(
    n = float(input('Determine n: ')),
    F = float(input('Determine F: ')),
    A = float(input('Determine A: ')),
    ac = int(input(f'Determine the number of decimal places: '))      
    )

#14. i_P_A
elif tp == 'i_P_A':
    i_P_A(
    n = float(input('Determine n: ')),
    P = float(input('Determine P: ')),
    A = float(input('Determine A: ')),
    ac = int(input(f'Determine the number of decimal places: '))
    )

#15. n_F_P
elif tp == 'n_F_P':
    n_F_P(
    i = float(input('Determine i: ')),
    F = float(input('Determine F: ')),
    P = float(input('Determine P: '))
    )

#16. n_F_A
elif tp == 'n_F_A':
    n_F_A(
    i = float(input('Determine i: ')),
    F = float(input('Determine F: ')),
    A = float(input('Determine A: '))
    )

#17. n_P_A
elif tp == 'n_P_A':
    n_P_A(
    i = float(input('Determine i: ')),
    P = float(input('Determine P: ')),
    A = float(input('Determine A: '))
    )

#18. P_A_g
elif tp == 'P_A_g':
    P_A_g(
    n = float(input('Determine n: ')),       
    i = float(input('Determine i: ')),
    A = float(input('Determine A: ')),
    g = float(input('Determine g: '))
    )

#19. F_A_g
elif tp == 'F_A_g':
    F_A_g(
    n = float(input('Determine n: ')),       
    i = float(input('Determine i: ')),
    A = float(input('Determine A: ')),
    g = float(input('Determine g: '))
    )

else:
    print('The process is unsupported.')
    # ta = input('Do you want try again? Y, N? ')
    #     if ta == 'Y' or 'y':
    #         pass           
    # if ta == 'N' or 'n':
    #     exit()