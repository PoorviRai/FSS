from Sample import Sample
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


class Num:
    
    def __init__(self, mx):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = pow(10, 32)
        self.hi = pow(-10, 32)
        self._some = Sample(mx)
        self.w = 1
        
    def Nums(t, f):
        if f is None:
             f = lambda x: x 
             
        n = Num(0)
        
        for x in t:
             n.NumInc(f(x))
         
        return n
    
    def NumInc(self, x):
        if x == "?":
            return x
        
        self.n += 1
        self._some.SampleInc(x)
        d = x - self.mu
        self.mu += d/self.n
        self.m2 += d*(x - self.mu)
        
        if x > self.hi:
            self.hi = x
        if x < self.lo:
            self.lo = x
        
        if self.n >= 2:
            self.sd = pow(self.m2/(self.n - 1 + pow(10, -32)), 0.5)
            
        return x
    
    def NumDec(self, x):
        if x == "?":
            return x
        if (self.n == 1):
            return x
        
        self.n -= 1
        d = x - self.mu
        self.mu -= d/self.n
        self.m2 -= d*(x - self.mu)
        
        if self.n >= 2:
            self.sd = pow(self.m2/(self.n - 1 + pow(10, -32)), 0.5)
            
        return x
    
    def NumNorm(self, x):
        return x == "?" and 0.5 or (x - self.lo)/(self.hi - self.lo + pow(10, -32))
    
    def NumXpect(self, j):
        n = self.n + j.n + 0.0001
        
        return self.n/n * self.sd + j.n/n * j.sd
        
def close(x, y, c):
    if c is None:
        c = 0.01
    return abs((x-y)/x) < c

    
@O.k
def NumTest():
    n = Num.Nums([4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000], None)
    assert close(n.mu, 270.3, None)
    assert close(n.sd, 231.946, None)
    print(n.mu, n.sd)
    
if __name__== "__main__":
  O.report()
