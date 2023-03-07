##Password generating function with following conditions:

## at least one uppercase character

## at least one special character

import random

def create_password_generator_v2(pool: str):
    
    special=False
    
    ## iterating through the input
    for i in pool:
        
        ## check (omega) at least one special in input(pool)
        omega=i.isalnum()
        if not omega:
            special=True

            
    if not special:
        
        print('The input string must contain at least one special character(!#?$). Try update the input and re-run the fucntion')
        
    if special:
    
        def child_func(n: int):
            
            ## collecting alphabetic characters to apply Only on them the .upper() method
            isalpha_ls=[]
            
            for i in pool:
                alpha=i.isalpha()
                if alpha:
                    isalpha_ls.append(i)
            
            u=random.choice(isalpha_ls).upper()
            
            ## collecting not alphanumeric characters and picking one random
        
            notalnum_ls=[]
            
            for i in pool:
                isalnum=i.isalnum()
                if not isalnum:
                    notalnum_ls.append(i)
                    
            s=random.choice(notalnum_ls)
            
            ## creating a list of random character from input (pool)
            ## use list comprehension
            pw_ls=[i for i in range(n)]
            
            for i in range(n):
                pw_ls.append(random.choice(pool))
            
               
            r0=random.randint(0,n)
            r1=r0-random.randint(1,n)
            
            pw_ls[r0]=u
            
            pw_ls[r1]=s
            
            ##creating output string
            pw=''.join(pw_ls)
            #for i in pw_ls:
                 #pw+=i
            ## with return method
            ## return ''.join(pw_ls)


            return pw

        return child_func