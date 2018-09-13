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


class Sym:
    def __init__(self):
        self.counts = {}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None
        
    def Syms(t, f):
        if f is None:
             f = lambda x: x 
        
        s = Sym()
        for x in t:
            s.SymInc(f(x))
            
        return s
    
    def SymInc(self, x):
        if x == "?":
            return x
        
        self._ent = None
        self.n +=1
        old = self.counts.get(x) 
        new = old and old + 1 or 1
        self.counts[x] = new
        
        if new > self.most:
            self.most, self.mode = new, x
        
        return x
    
    def SymDec(self, x):
        self._ent = None
        
        if self.n > 0:
            self.n -= 1
            self.counts[x] -= 1
            
        return x
    
    def SymEnt(self):
        if not self._ent:
            self._ent = 0
            for x, n in self.counts.items(): 
                p = n/self.n
                self._ent -= p * math.log(p,2)
                
        return self._ent

def close(x, y, c):
    if c is None:
        c = 0.01
    return abs((x-y)/x) < c

    
@O.k
def SymTest():
    s = Sym.Syms([ 'y','y','y','y','y','y','y','y','y',
	        'n','n','n','n','n'], None)
    
    assert close(s.SymEnt(), 0.9403, None)
    print(s.SymEnt())
