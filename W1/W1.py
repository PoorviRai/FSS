import re,traceback
import temp
from collections import Counter
import random
import re
import math

def MathandTuples(a, b):
    return (a+b), (a-b), (a*b), (a/b)

def raise_to_three(base):
    return pow(base, 3)

def fib(n):
    f, s = 0, 1
    while f < n:
        print(f, end=' ')
        f, s = s, f+s
    print()

sum = lambda i, j : print("Sum = %s"%(i+j))

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)
    
def print_kwargs(**kwargs):
        print(kwargs)

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def displayStudent(self):
        print("Name : ", self.name,  ", ID: ", self.ID)
    

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f
@O.k
def testingFailure():
  """this one must fail.. just to
  test if the  unit test system is working"""
  assert 1==2

@O.k
def testingSuccess():
  """if this one fails, we have a problem!"""
  assert 1==1
  
@O.k
def testingWhitespaces():
    for i in range(5):
        print(i)
        if i%2 == 0:
            print("Divisible by 2")
        else: print("Indivisible by 2")
    print("End of loop")
    
@O.k
def testingModules():
    temp.abc()
    
@O.k
def testingArithmeticandTuplesTogether():
    x, y = 27, 5
    a, s, m, d = MathandTuples(x, y)
    print("a=%s and b=%s" %(x,y))
    print("\nAddition = %s \nSubtraction = %s \nMultiplication = %s \nDivision = %s"%(a, s, m, d))

@O.k
def testingFunctions():
    fib(10)
    sum(21, 34)

@O.k
def testingStrings():
    print('This works')
    print("\t This too")
    print("""\nI'm getting the hang of this.
I think.
Yay!""")
    
@O.k
def testingExceptions():
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Invalid entry")

@O.k
def testingLists():
    x = range(5)
    y = ["Poorvi", 10.4, True]
    z = [x, y]
    y.extend([7,8,9])
    print(*x)
    print(*y)
    print(*z)
    
@O.k
def testingDictionaryandCounter():
    score = {'Harry': 500, 'Ron': 450}
    score['Hermione'] = 780
    print(score)
    print(Counter(score))
    
@O.k
def testingSets():
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    bskt = set(basket)
    bskt.add('mango')
    print(bskt)
    
@O.k
def testingControlFlow():
    x = 0
    while x<=10:
        if x%2 == 0:
            print("%s is Even" %x)
        else: print("%s is Odd" %x)
        x+=1
        
@O.k
def testingTruthiness():
    a, b = 2, None
    print(a!=2)
    print(b == None)
    
@O.k
def testingSorting():
    x = [19, 45, 22, 5, 67, 888, 456, 239]
    y = sorted(x, reverse=True)
    x.sort()
    print(x, y)
    
@O.k
def testingListComprehensions():
    a = [x for x in range(5)]
    b = [x*x for x in a]
    pairs = [(x, y)
            for x in a
            for y in b]
    print(pairs)
    
@O.k
def testingIterators():
    cities = ["Mumbai", "Pune", "Kolkata", "Delhi", "Bangalore"]
    x = iter(cities)
    while x:
        try:
            city = next(x)
            print(city)
        except StopIteration:
            break
        
@O.k
def testingGenerator():
    i = 1
    while i<15:
        yield i
        i+=1
        
@O.k
def testingRandomness():
    x = [random.randrange(10, 25) for _ in range(7)]
    print(x)
    random.shuffle(x)
    print(x)
    print(random.choice(x))
    print(random.sample(x, 3))

@O.k
def testingRegularExpression():
    print([re.match("a", "cat"), re.search("a", "cat"),not re.search("c", "dog"), 5 == len(re.split("[ab]", "carbs")),"R-D-" == re.sub("[0-9]", "-", "R2D2")])

@O.k
def testingOOP():
    st1 = Student("Poorvi", 2002)
    st2 = Student("Sam", 2134)
    st1.displayStudent()
    st2.displayStudent()

@O.k
def testingFunctionaltools():
    print(raise_to_three(2))
    a = [1, 2, 3, 4]
    twicea = [raise_to_three(x) for x in a]
    print(twicea)
    twicea = map(raise_to_three, a)
    print(twicea)
    twicea = filter(raise_to_three, a)
    print(twicea)
    
@O.k
def testingEnumerate():
    names = ['Poorvi', 'Rai', 'Chetana', 'Salunke']
    print(list(enumerate(names)))
    print(list(enumerate(names, start = 1)))
    
@O.k
def testingZipandUnzip():
    words = ['apple', 'boat', 'cat', 'dog']
    alphabet = ['a for', 'b for', 'c for', 'd for']
    teach = zip(alphabet, words)
    pairs = [(1,2), (2,3), (4,5)]
    p, a = zip(*pairs)
    print(teach)
    print(pairs, p, a)
    
@O.k
def testingsArgsandKwargs():
    multiply(4)
    multiply(10, 9)
    multiply(2, 3, 4)
    print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
    print_kwargs(my_name="Sammy", your_name="Casey")

if __name__== "__main__":
  O.report()
