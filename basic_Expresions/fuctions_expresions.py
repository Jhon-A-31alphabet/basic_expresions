import re
import random


def search_ontex(a,word)->str:
    p=re.search(a,word)
    print(p)

### those functions are equivalent as findall

def substring(val,val1)->None:
    return re.findall(val,val1)
def find_substring(fuction,val,val1):
    return fuction(val,val1)

#################################################


#funcion = substring
#resultado = find_substring(substring,"a","abddda")
#print(resultado)


def combine(iterable_1,iterable_2 :str)->str:
    
   
        a=[(x,y)for x in iterable_1 for y in iterable_2]
        return a


#to combine a string with a tuple#

def string_in(a,b :True)->True:

    if a in b:
        return True


def start_string(iterable :str,iterable_1 :str)->str: # if iterable has concidence with iterable_ return true
    #return true
    if re.match(iterable,iterable_1):
       return iterable
    return True

def select_element_list(a :str) ->str: #select random elemente in list.
    try:
        p = random.choice(a)
        if range(0,) in a:
            return p
    except:
        ValueError
    
    finally:
        pass

def match_A_Z(text :str)->str: #its going to search  at the begnning of the string
    p = re.compile("[A-Z]")
    r=p.match(text)
    return r

def match_a_z(text :str) ->str:
    try:
        p = re.findall("\D[a-z]",text)
        return p
    except:
        ValueError
    finally:
        pass


    




         









    



  




    



