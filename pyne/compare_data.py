def compare_data(mode, val1, err1, val2, err2):     
   return_type= True
   diff= 0
   try:
      mode=int(mode) 
      val1=float(val1)
      val2=float(val2)
      err1=float(err1)
      err2=float(err2)
   except ValueError:
      print("that was not valid number..")
      return 
   if mode ==1:
       #compare val1 and val2
       if val1!=val2:
          return_type= False
   elif mode ==2:
       #compare val2 with val1 and err1
       if val1+err1 >= val2 >= val1-err1:
          pass
       else:
          return_type=False
   elif mode ==3:
       #compare val1 with val2 and err2
       if val2+err2 >= val1 >= val2-err2:
          pass
       else:
          return_type=False
   else: 
         print("error: mode type is not supported. ")
         return
  
   diff=abs(val1-val2)
   return return_type, diff
             
       
