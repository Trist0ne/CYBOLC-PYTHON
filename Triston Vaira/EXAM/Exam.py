# def q1(addr):
#     if int(addr[:2]) >= 224 and int(addr[:2]) < 240:
#         return(True)
#     else:
#         return(False)
    
# # def q1():
# #     lst = [*range(0, 1024, 1)]
# #     return(lst)

# # def q1(number):
# #     if number == "zero":
# #         return(int("0"))
# #     if number == "one":
# #         return(int("1"))
# #     if number == "two":
# #         return(int("2"))
# #     if number == "three":
# #         return(int("3"))
# #     if number == "four":
# #         return(int("4"))

# def q1():
#     user = input("Type your string: ")
#     new_string = ''.join(ch for ch in user if ch.isdigit())
#     print(int(new_string))

# def q1(first,middle,last,domain):
#     email = first + "." + middle[:0] + "." + last + "@" + domain + ".com"
#     return(email)
    
# q1(triston,rocky,vaira,gmail)

# def q1(infile,outfile):
#     with open(infile,'r') as firstfile, open(outfile,'w') as secondfile:
#         for line in firstfile:
#             secondfile.write(line)
            
# def q1(address):
#     username = address.split('@')[0]
#     first = username.split('.')[0]
#     middle = username.split('.')[1]
#     last = username.split('.')[2]
#     domain = address.split('@')[1]
#     domainname = domain.split('.')[0]
#     stuple = (first,middle,last,domainname)
#     return(stuple)

# def q1(strng):
#     all_freq = {}
#     for i in strng:
#         if i in all_freq:
#             all_freq[i] += 1
#         else:
#             all_freq[i] = 1
#     return(all_freq)

# def q1():
#     stuple = ("Vaira", "Vaira"[::-1])
#     return(stuple)

# def tcp_qotd_client(address, port):
#     s = socket.socket()
#     s.connect((address, port)) # blocks
#     s.sendall(b'never gonna give you up')
#     data = s.recv(16)224.0.0.0 to 239.255.255.255.
#     quote = bytearray()
#     while data:
#         print(quote)
#         quote.extend(data)
#         data = s.recv(16)
#     print(quote.decode('ascii'))
    
# import socket
# def q1(ip,port):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         s.connect((ip, int(port)))
#         s.shutdown(2)
#         return True
#     except:
#         return False
    
# def q1(*args, **kwargs):
#     sum = 0
#     for num in args:
#         sum += int(num)
#     for num in kwargs:
#         sum += int(num)
#     return sum

# def q1(address, port):
#     s = socket.socket()
#     s.connect((address, port)) # blocks
#     s.sendall(b'hello')
#     data = s.recv(16)
#     while da
    
# def __init__(self, year, make, speed):
    

# import ipaddress
# def q1(addr):
#     if is_multicast(addr) == True:
#         return(True)
#     else:
#         return(False)
    

# from netaddr import IPAddress
# def q1(addr):
#     if IPNetwork(addr).is_multicast() == True:
#         return(True)
#     else:
#         return(False)
    


def q1(addr):
    split = (tuple(int(n) for n in addr.split('.')))
    ip_range = [(224,0,0,0), (239,255,255,255)]
    if split > ip_range[0] and split < ip_range[1]:
        return(True)
    else:
        return(False)
q1("192.168.254.32")

import socket
def q1(address,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address,port))
    s.sendall(b'hello')
    data = s.recv(1024)
    s.close()
    return(data)


class car:
    def __init__(self):
        self.__speed = 0
    
    def setspeed(self, __speed):
        self.__speed = __speed

    def getspeed(self):
        return self.__speed

    def speedup(self):
        self.__speed +=1

    def slowdown(self):
        self.__speed -=1
    
    def stop(self):
        self.__speed = 0

    def get_speed(self):
        return str(self.__speed)
    
    def __str__(self):
        return("Current speed: " + car.get_speed(self))
        
        
        
        
