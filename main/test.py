# # import pexpect

# # child = pexpect.spawn('su - user')
# # child.expect("Password:")
# # child.sendline("bruh")
# # try:
# #     child.expect('\$')
# # except:
# #     print("Error has occured")
# # else:
# #     child.sendline('whoami')
# #     child.expect('\$')

# #     print (child.before.decode())

# import pexpect
# import subprocess
# userList = ["dev","user"]
# errorUser = []
# passwd = subprocess.run(['cat','/etc/passwd'],capture_output=True,text=True)
# for user in userList: 
    
    
#     userFound = False
#     for line in passwd.stdout.split('\n'):
        
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
