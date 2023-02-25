def rot13(l):
  #"rotate by 13 places" substitution cipher
  alfabet = 'abcdefghijklmnopqrstuvwxyz'
  if l in alfabet :
    for j in alfabet:
      if l==j:
        if alfabet.index(j) >= 13 :
          return alfabet[alfabet.index(j)-13]
        else:
          return alfabet[alfabet.index(j)+13]
  else:
    return l
 
 
def main():
  res = []
  #Input: text that we want to code
  text = input("Input : ")
  for x in text:
    l=rot13(x.lower())
    if(x.isupper()):
      res.append(l.upper())
    else:
      res.append(l)
  print("Result :",''.join(res))




if __name__=="__main__":
  main()
