

import pprint
import urllib.request
import requests

def parseFile(input):
    if input.startswith('http'):
#         uri=input
#         r = requests.get(uri).text
#         alllines= ''.join(r.split('\n'))
#         print(alllines)
#         buffer = r.read().decode('utf-8')
#         return myparser(buffer)
        print('This does not read http files')
        exit()
    else:
        return myparser(input)
    

      # use requests
#         uri=input
#         r=urllib.request.urlopen(uri)
# #         r = requests.get(uri).text
#         return myparser(r)
#         r = requests.get(uri).text
#         print(r)
# #         req = urllib.request.urlopen(uri)
# #         buffer = req.read().decode('utf-8')

#         \n'.join(r.split('\n')[:5]) 




def myparser(file):# eventually you will be passing a filename to this method as an arg...
    instructions=[]
    filename = file
    with open(filename) as f:
        N=int(f.readline())
        for line in f.readlines(): 
            values = line.strip().split(' ')
            firstword = values[0]
            if firstword=='turn':
                phrase = ' '.join(values[0:2])
                if phrase== 'turn on':
                    cmd='turn on'
                    x=values[2]
                    x2=x.split(',')
                    num1=x2[0]
                    num2=x2[1]
                    x3=values[4]
                    x4=x3.strip().split(',')
                    num3=x4[0]
                    num4=x4[1]
                elif phrase== 'turn off':
                    cmd = 'turn off'
                    x=values[2]
                    x2=x.split(',')
                    num1=x2[0]
                    num2=x2[1]
                    x3=values[4]
                    x4=x3.strip().split(',')
                    num3=x4[0]
                    num4=x4[1]
                else:
                    cmd= ''
                    num1=0
                    num2=0
                    num3=0
                    num4=0
            elif firstword=='switch':
                cmd = str(values[0])
                x=values[1]
                x2=x.split(',')
                num1=x2[0]
                num2=x2[1]
                x3=values[3]
                x4=x3.strip().split(',')
                num3=x4[0]
                num4=x4[1]
            else:
                cmd=''
                num1=0
                num2=0
                num3=0
                num4=0
            thisline=[cmd, num1, num2,num3,num4]
            instructions.append(thisline)
             
    return N, instructions



class LightTester:
     
    def __init__(self,N):
        self.size=N
        self.lights = [ [False]*N for i in range(N) ]
                     
        
    def printlights(self):
        pprint.pprint(self.lights)
        
    def turnon (self, a, b, c, d):
        self.x = int(a)
        self.y = int(b)
        self.z=int(c)
        self.q=int(d)
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        if self.z>self.size-1:
            self.z=self.size-1
        if self.q>self.size-1:
            self.q=self.size-1
        for i in range (self.x, self.z+1):
            for j in range (self.y, self.q+1):
                self.lights[i][j]=True
    

    def turnoff(self, a, b, c, d):
        self.x = int(a)
        self.y = int(b)
        self.z=int(c)
        self.q=int(d)
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        if self.z>self.size-1:
            self.z=self.size-1
        if self.q>self.size-1:
            self.q=self.size-1 
        for i in range (self.x, self.z+1):
            for j in range (self.y, self.q+1):
                self.lights[i][j]=False
                    
                    
    def switch(self, a, b, c, d):
        self.x = int(a)
        self.y = int(b)
        self.z=int(c)
        self.q=int(d)
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        if self.z>self.size-1:
            self.z=self.size-1
        if self.q>self.size-1:
            self.q=self.size-1
        for i in range (self.x, self.z+1):
            for j in range (self.y, self.q+1):
                if self.lights[i][j]==True:
                    self.lights[i][j]=False
                else:
                    self.lights[i][j]=True
    
    def count(self):
        count=0
        for i in range(self.size):
            for j in range(self.size):
                if self.lights[i][j]==True:
                    count=count+1
        return count
    
    def apply(self,instructions):
        for i in instructions:
            cmd=(i[0])
            num1=(i[1])
            num2=(i[2])
            num3=(i[3])
            num4=(i[4])
            if cmd=='turn on':
                self.turnon(num1,num2,num3,num4)
            elif cmd=='turn off':
                self.turnoff(num1,num2,num3,num4)
            elif cmd=='switch':
                    self.switch(num1,num2,num3,num4) 
            else:
                continue
    
           
                     

    
