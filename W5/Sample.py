import random
import math
import re,traceback

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



class Sample:
    
    def __init__(self, maximum):
        self.max = maximum
        self.rank = 1
        
        self.n = 0
        self.sorted = False
        self.some = []
        
    def SampleInc (self, x):
        self.n += 1
        length = len(self.some)
        
        if length < self.max:
            self.sorted = False
            self.some.append(x)
        elif random.uniform(0,1) < length/self.n:
            self.sorted = False
            self.some[math.floor(random.uniform(0, 1)*length)] = x
        
        return x
    
    def SampleSorted (self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
            
        return self.some
    
    def nth (self, n):
        s = self.SampleSorted()
        return s[min(len(s), max(1, math.floor(0.5 + len(s)*n)))]
    
    def nths (self, ns):
        if ns is None:
            ns = [0.1, 0.3, 0.5, 0.7, 0.9]
        out = []
        for _, n in enumerate(ns):
            out.append(self.nth(n))
        
        return out
    
    def SampleLt (s1, s2):
        return s1.nth(0.5) < s2.nth(0.5)

def close(x, y, c):
    if c is None:
        c = 0.01
    return abs((x-y)/x) < c

@O.k
def SampleTest():
    random.seed(1)
    s = []
    
    for i in range(5, 10):
        s.append(Sample(pow(2, i)))
        
    for i in range(1, 1000):
        y = random.random()
        for t in s:
            t.SampleInc(y)
            
    for t in s:
        print(t.max, t.nth(0.5))
        assert close(t.nth(0.5), 0.5, 0.33)
        

if __name__== "__main__":
  O.report()
        