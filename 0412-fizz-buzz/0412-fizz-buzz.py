class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        L1=[]
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                L1.append("FizzBuzz")
            elif i%3 == 0:
                L1.append("Fizz")
            elif i%5 == 0:
                L1.append("Buzz")
            else:
                L1.append(str(i))
        return L1
n=5