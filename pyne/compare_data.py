"""this method compare two columns of results and errors, return
   ture if the two columns have the same results otherwise return
   false. Also return the list of absolute difference btw these 
   two columns"""
import math 
def compare(mode,val1,err1,val2,err2):
    return_type = True
    diff = 0
    try:
       mode = int(mode)
       val1 = float(val1)
       val2 = float(val2)
       err1 = float(err1)
       err2 = float(err2)
    except ValueError:
       print("that was not valid number")
       return 
    diff=abs(val1-val2)
    sigma_diff=math.sqrt(err1**2+err2**2)
    if mode ==1:
        #compare val1 and val2
        if val1!=val2:
           return_type= False 
    elif mode ==2:
        #compare diff with err1 or err2
        if diff  < err1 and diff  < err2:
           pass:
        else:
           return_type = False
    elif mode == 3:
        #compare sigma_diff with diff
        if diff > sigma_diff:
           return_type = False
    return return_type, diff
              
