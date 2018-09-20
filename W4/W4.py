from Sym import Sym
from Num import Num
import re

class Data:
    
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.classc = None 
        self.rows = {}
        self.name = {}
        self._use = {}
        self.indeps = []

        
    def independent(self, c):
        return c not in self.w and self.classc != c
    
    def dependent(self, c):
        return not self.independent(c)
    
    
    def header(self, cells):
        
        for c0, x in enumerate(cells):
            
            if not "?" in x:
                c = len(self._use)
                self._use[c] = c0
                self.name[c] = x
                a = re.match('[<>$]',x)
                if a:
                    #print ("match")
                    self.nums[c] = Num(0)
                    #print(self.nums[c])
                else:
                    self.syms[c] = Sym()
                    #print(self.syms[c])
                
                if re.match('<', x):
                    self.w[c] = -1
                elif re.match('>', x):
                    self.w[c] = 1
                elif re.match('!', x):
                    self.classc = c
                else:
                    self.indeps.append(c)
                    
        return self
    
    def row(self, cells):
        r = len(self.rows)
        self.rows[r] = {}
        
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            
            if x != "?":
                if c in self.nums:
                    x = float(x)
                    self.nums[c].NumInc(x)
                else:
                    self.syms[c].SymInc(x)
            
            self.rows[r][c] = x
            
        return self
    
    def rows(file):
        data = Data()
        with open(file) as src:
            first = True
            line = src.readline()
            while line:
                line = re.sub('([ \n\r\t]|#.*)', "", line)
                cells = line.split(',')
                if len(cells) > 0:
                    if first:
                        first = False
                        data.header(cells)
                    else:
                        data.row(cells)
                line = src.readline()
        return data
    
    
    def display(self):
        print("\n\t          \t\t n\t mode\t frequency")
        for i, sym in self.syms.items():
            print(i, "\t", self.name[i].ljust(15), "\t", sym.n, "\t", sym.mode, "\t", sym.most)
    
        print("\n\t          \t\t n\t\t mu\t sd")
        for i, num in self.nums.items():
            print(i, "\t", self.name[i].ljust(15), "\t", num.n, "\t", '%10.2f'%(num.mu), "\t", '%.2f'%(num.sd))

    
if __name__== "__main__":
  data_1 = Data.rows("weather.csv")
  data_2 = Data.rows("weatherLong.csv")
  data_3 = Data.rows("auto.csv")
  
  print ("\n\n\nweather.csv")
  data_1.display()
  
  print ("\n\n\nweatherLong.csv")
  data_2.display()
  
  print ("\n\n\nauto.csv")
  data_3.display()
