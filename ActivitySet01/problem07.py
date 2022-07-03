# Strings

text = "X-DSPAM-Confidence:    0.8475"
str = "X-DSPAM-Confidence:  0.8475" 
position=str.find(":")   
piece=str[position+1:]   
x=float(piece)            
print(x) 
  
 