

import pprint


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
                    x4=x3.split(',')
                    num3=x4[0]
                    num4=x4[1]
                elif phrase== 'turn off':
                    cmd = 'turn off'
                    x=values[2]
                    x2=x.split(',')
                    num1=x2[0]
                    num2=x2[1]
                    x3=values[4]
                    x4=x3.split(',')
                    num3=x4[0]
                    num4=x4[1]
                else:
                    print('this should not print')
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
                x4=x3.split(',')
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
           
                     
def main():
    file = "smalltest.txt"
    info = myparser(file)
    N=info[0]
    instructions=info[1]
    print(N)
    lights=LightTester(N)
    print()  
    lights.printlights()
    
