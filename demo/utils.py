
# 斐波那契数列
def FibonacciSequence(n=100):
   a,b=0,1
   result=[]
   while a<n:
       result.append(a)
       a,b=b,a+b
   return result

def doubleNumber(n):
    return n*2

def openFile(filePath):
    readData = None
    with open(filePath,encoding="utf-8") as f:
        readData = f.read()
    return  readData