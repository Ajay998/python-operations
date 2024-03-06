# with open("write_file2","w+") as f:
#     f.write("Two line")
#     print(f.read()) ############# It can read
#
# with open("write_file3","w") as f:
#     f.write("Two line")
#     print(f.read())           ############# It cant read

# person_data = ['Name: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
# # writing string and list of lines to a file
# fp = open("write_demo.txt", "w")
# fp.writelines(person_data)
# fp.close()

# gap = ""
# name = '\nEmma'
# address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
# # append to file
# with open("write_demo.txt", "a") as f:
#     f.write(gap)
#     f.write(name)
#     f.writelines(address)
