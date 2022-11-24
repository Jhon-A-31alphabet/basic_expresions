import re
import random


def search_on_tex(a,word)->str:
    p=re.search(a,word)
    print(p)

### this fuction is equivalent to findall
def substring(val:str,val1:str)->str:
    return re.findall(val,val1)



#################################################


#funcion = substring
#resultado = find_substring(substring,"a","abddda")
#print(resultado)


def combine(iterable_1,iterable_2 :str)->str:
    
   
        a=[(x,y)for x in iterable_1 for y in iterable_2]
        return a
        #to combine a string with a tuple#



def string_in(a,b :True)->True: #return true if a is in b.If a not in b return none

    if a in b:
       print(True)
       return True
    else:
        print(None)
        return None
        


def start_string(iterable :str,iterable_1 :str)->str: # if iterable has concidence with iterable_ return true
    #return true
    if re.match(iterable,iterable_1):
       return iterable
    
    return True

def select_element_list(a :str) ->str: #select random elemente in list.
    try:
        p = random.choice(a)
        return p

    except:
        ValueError
    
    finally:
        pass

def match_A_Z(text :str)->str: #its going to search  at the begnning of the string.
    try:
        p = re.compile("[A-Z]")
        r=p.match(text)
        return r
        
    except:
        ValueError

def match_a_z(text :str) ->str:#its going to search  at the beginning of the string to.
    try:
        p = re.compile("[a-z]")
        r=p.match(text)
        return r
    except:
        ValueError






         









    



  




    



