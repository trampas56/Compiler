#int counterFunctionCalls

def fibonacci(x):
#{  global counterFunctionCalls
    counterFunctionCalls = counterFunctionCalls + 1
    if x<=1:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
#}

def isPrime(x):
#{
      #int i
      def divides(x,y):
      #{   global counterFunctionCalls
           counterFunctionCalls = counterFunctionCalls + 1
           if y == (y//x) * x :
                return 1
           else :
                return 0
      #}
      global counterFunctionCalls
      counterFunctionCalls = counterFunctionCalls + 1
      i = 2
      while i<x:
      #{
           if divides(i,x)==1 :
                return 0
           i = i + 1
      #}
      return 1
#}

#def main
#int x,i

counterFunctionCalls = 0

x = int(input())
print(fibonacci(x))

i = 2
while i<=30 :
#{
   if isPrime(i)==1 :
       print(i)
   i = i + 1
#}
