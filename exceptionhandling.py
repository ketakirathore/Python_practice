#nested try in try
#a = 10
#b = 2
#try:   (execution)
#    print(a/ b)   (output requied)
#    try:
 #       f = open("abc.txt",'r')
  #      f.write("hello ")
#        print("file is updated")
#    except Exception as e :
#        print(e)    
#except Exception as e :  ( except the exception in e) = e = error
#    print(e)
#finally:
#    print("always execute")  = it always run the program


#a = 10
#b = 0
#try:
#  print(a/b)
#except:
#  print("division by 0 not allowed")  
#note = try is for checking the error if the error occured it still run the next excution in except.
#packages/module
    
#to get exact error
#a = 10
#b= 0
#try :
#  print (a/b)
#except Exception as e :
 # print(e)  
 # output = division by zzero 