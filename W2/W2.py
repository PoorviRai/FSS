import re,traceback

DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes
    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,
                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

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

def lines(s):
  "Return contents, one line at a time."
  return s.splitlines()
  
def rows(src):
  """Kill bad characters. If line ends in ',' 
   then join to next. Skip blank lines."""
   
  #remove comments
  l = []
  for line in src:
      l += [line.split('#', 1)[0]]
                       
  #list of elements with blank spaces removed. 
  a = list(filter(None, l))
  a = [x.strip() for x in a]                 
  
  # Concatenate elements ending with comma with the next 
  clean_data_list = []
  concat_str = ""
  for index, ele in enumerate(a):
      if ele.endswith(','):
          concat_str += ele
      elif a[index-1].endswith(','):
          concat_str += ele
          
      else:
          if concat_str:
              clean_data_list.append(concat_str)
          clean_data_list.append(ele)
          concat_str = ""
        
  src = clean_data_list
  return src


def cols(src):
    # Get the headers of the source as a list
    headers = src[0].split(',')
    
    # Get the indexes of the columns beginning with a '?' into a list
    index = [i for i,element in enumerate(headers) if element.startswith('?')]
    
    #remove those headers from the list
    for i in index:
        del headers[i]
    
    # create a list to store the elements without the data that begins with '?'
    rem_cols_list = []
    # Append the headers to the list
    rem_cols_list.append(headers)
    # iterate through the remaining data and remove elements with index equal to one we found
    for rec in src[1:]:
        rec_new = [element for i, element in enumerate(rec.split(',')) if i not in index]
        rem_cols_list.append(rec_new)
       
    src = rem_cols_list
    return src


def prep(src):
    #take indexes of elements with $ in first list
    index = [i for i,element in enumerate(src[0]) if element.startswith('$')]
    print(index)
    
    #converted elements with index equal to one found to float
    for rec in src[1:]:
        for i, ele in enumerate(rec):
            if i in index:
                rec[i] = float(ele)
    return src


def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)


if __name__== "__main__":
  O.report()
