

import subprocess
passwd = subprocess.run(['docker','exec','-it','-u','root',"round7",'grep',"%sudo",'/etc/sudoers'])
# text = subprocess.run(['cat','/home/dev/test.txt'],capture_output=True,text=True)
# #print(text.stdout)
# nameList = ["Alex","Dave","Gloria","Joey","King Julien","Kowalski","Marlene","Marty"
#             ,"Mason","Maurice","Melman","Mort","Nana","Private","Rico","Skipper"]
# i = 1
# for line in text.stdout.split('\n'):
#     if(str(i) in line and nameList[i-1] in line):
#         print(f'{nameList[i-1]} matches with order')
#         i += 1
#     elif(i <= 16):
#         print(f'{line} had a missed match')
#         break
        
    
#         if ((user in line) and (f'/home/{user}' in line) and ("/bin/bash" in line)):
#             awk = subprocess.run(['awk','-F:','{{print $5}}'],capture_output=True,text=True,input=line)
#             print(awk.stdout)
#             if((user in awk.stdout)):
#                 userFound = True
#                 print(user)
            
                
       
#     if(userFound == False):
#         errorUser.append(user)

# if(errorUser):
#     print("there is something wrong these ppl")
    
# else:
#     for user in userList:
#         child = pexpect.spawn(f'su - {user} ')
#         child.expect("Password:")
#         child.sendline("bruh")
#         try:
#             child.expect('\$')
#         except:
#             print("Error has occured")
#         else:
#             child.sendline('whoami')
#             child.expect('\$')
#             print (child.before.decode())



       
 
           
            
# #print(errorList)        

    
#         # else:
#         #     print(f'{user} was not found')
#         #     child = pexpect.spawn(f'su - {user}')
#         #     child.expect("Password:")
#         #     child.sendline("test")
#         #     try:
#         #         child.expect('\$')
#         #     except:
#         #         print("Error has occured")
#         #     else:
#         #         child.sendline('whoami')
#         #         child.expect('\$')
#         #         print (child.before.decode())


# # child.expect('Password:', timeout=120)
# # child.sendline('bruh')

# # child.expect('~$')

# # child.sendline("whoami")
# # child.expect('~$')
# # print (child.after)
