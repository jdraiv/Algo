#Caesars Cipher

import string

def rot13(str):
    alphabet = list(string.ascii_lowercase)
    result = ""
    
    for l in str.lower():
        
        if l == " ":
            result += l
            
        else:
            if l in alphabet:
                
                l_index = alphabet.index(l) + 13

                if l_index >= len(alphabet):
                    result += alphabet[l_index - len(alphabet)]

                else:
                    result += alphabet[l_index]
            else:
                result += l
        print(result.upper())
        
rot13("QBA'G RIRE GRYY NALOBQL NALGUVAT. VS LBH QB, LBH FGNEG ZVFFVAT RIRELOBQL")
rot13("JUB JNAGF SYBJREF JURA LBH'ER QRNQ? ABOBQL")
rot13("GUR YBARYVRFG ZBZRAG VA FBZRBAR'F YVSR VF JURA GURL NER JNGPUVAT GURVE JUBYR JBEYQ SNYY NCNEG, NAQ NYY GURL PNA QB VF FGNER OYNAXYL.")
rot13("AB NZBHAG BS SVER BE SERFUARFF PNA PUNYYRATR JUNG N ZNA JVYY FGBER HC VA UVF TUBFGYL URNEG.")
rot13("NATEL, NAQ UNYS VA YBIR JVGU URE, NAQ GERZRAQBHFYL FBEEL, V GHEARQ NJNL.")
rot13("FB JR ORNG BA, OBNGF NTNVAFG GUR PHEERAG, OBEAR ONPX PRNFRYRFFYL VAGB GUR CNFG.")
