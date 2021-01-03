import base64,time
import sys
banner = """
 \u001b[1;35m
 _____ ________   _______ _____ _____ _   _______ _      _      ___________ 
/  __ \| ___ \ \ / / ___ \_   _|  _  | | / /_   _| |    | |    |  ___| ___ \ 
| /  \/| |_/ /\ V /| |_/ / | | | | | | |/ /  | | | |    | |    | |__ | |_/ /
| |    |    /  \ / |  __/  | | | | | |    \  | | | |    | |    |  __||    / 
| \__/\| |\ \  | | | |     | | \ \_/ / |\  \_| |_| |____| |____| |___| |\ \ 
 \____/\_| \_| \_/ \_|     \_/  \___/\_| \_/\___/\_____/\_____/\____/\_| \_| 
                                                                            
                                                                           \u001b[0m
                               \u001b[1;34m-coded with <3 by Satyender Yadav\u001b[0m """



def get_data():
    print("  \u001b[32;1m[*] \u001b[37;1mEnter Your Cipher Text Here : \u001b[36;1m",end="")
    text = input()
    return text

print("  \n\n  \u001b[32;1m[*] \u001b[1;31mThis Tool Have These Options ")
print("   \u001b[32;1m|")
print("   \u001b[32;1m|--\u001b[37;1m[1] RSA")
print("   \u001b[32;1m|--\u001b[37;1m[2] Weignier RSA")
print("   \u001b[32;1m|--\u001b[37;1m[3] Base 64")
print("   \u001b[32;1m|--\u001b[37;1m[4] Base 32")
print("   \u001b[32;1m|--\u001b[37;1m[5] Ceaser Cipher Or Rot 13")
print("   \u001b[32;1m|--\u001b[37;1m[6] Morse Code")
print("   \u001b[32;1m|--\u001b[37;1m[7] Simple Reverse")
print("   \u001b[32;1m|--\u001b[37;1m[8] Rot 47")
print("   \u001b[32;1m|--\u001b[37;1m[9] Mobile Cipher")
print("   \u001b[32;1m|--\u001b[37;1m[10] NATO phonetic Cipher")
print("   \u001b[32;1m|--\u001b[37;1m[11] Brain Fuck Decoder")
print("   \u001b[32;1m|--\u001b[37;1m[12] Brute Force\n")







def base32(cipher): 
    
   try:
    base64_bytes = cipher.encode('ascii')
    message_bytes = base64.b32decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Base32")
    print("   \u001b[32;1m|")
    print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
    print("      \u001b[32;1m[!]\u001b[37;1m",message)
   except:
    print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Base32")
    print("   \u001b[32;1m|")
    print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
    print("      \u001b[32;1m[!]\u001b[37;1m This Not Base32")

#base64 
def base2x32(cipher): 
    
   try:
    base64_bytes = cipher.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Base64")
    print("   \u001b[32;1m|")
    print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
    print("      \u001b[32;1m[!]\u001b[37;1m",message)
   except:
    print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Base32")
    print("   \u001b[32;1m|")
    print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
    print("      \u001b[32;1m[!]\u001b[37;1m This Not Base64")

    

def morse_code(cipher):    
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-',' ':'/'

                     }
    cipher =cipher + ' '
    decipher = '' 
    citext = '' 
    try:
     for letter in cipher: 
  
        if (letter != ' '): 
  
           citext += letter 
  
     
        else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = '' 
     print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Morse Code")
     print("   \u001b[32;1m|")
     print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
     print("      \u001b[32;1m[!]\u001b[37;1m",decipher) 

    except:
     print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Morse Code")
     print("   \u001b[32;1m|")
     print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
     print("      \u001b[32;1m[!]\u001b[37;1m Cipher Code Wrong") 
        
   
def ceaser(cipher):
    rotted=""
    for i in range(len(cipher)):
        char = cipher[i]
        if char in  "1234567890!@#$%^&*()/><}{|\-*+_.= ?,":
            rotted += char
            continue
        elif char.isupper():
            rotted+=chr((ord(char)+13-65)%26+65)
        else :
            rotted+=chr((ord(char)+13-97)%26+97)
    print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Caesar Cipher / Rot13 ")
    print("   \u001b[32;1m|")
    print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
    print("      \u001b[32;1m[!]\u001b[37;1m",rotted)
    
def reverse(cipher):
    plain=""
    forward=""
    for i in range (len(cipher)-1,-1,-1):
         
             
         print(cipher[i])

def rot47(cipher):
   encrypt = "!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";
   decrypt = "PQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO";
   plain=""
   for i in range(len(cipher)):
     loc = encrypt.find(cipher[i])    
     plain+=decrypt[loc]
   print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Rot 47 ")
   print("   \u001b[32;1m|")
   print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
   print("      \u001b[32;1m[!]\u001b[37;1m",plain)  

def t9_mappings(cipher):
   t9_mapping = {
    "7777": "s",
    "9999": "z",
    "222": "c",
    "111": "@",
    "333": "f",
    "444": "i",
    "555": "l",
    "666": "o",
    "777": "r",
    "888": "v",
    "999": "y",
    "22": "b",
    "33": "e",
    "44": "h",
    "55": "k",
    "66": "n",
    "77": "q",
    "88": "u",
    "99": "x",
    "11": ":",
    "2": "a",
    "3": "d",
    "4": "g",
    "5": "j",
    "6": "m",
    "7": "p",
    "8": "t",
    "9": "w",
    "1": "_",
    "0": " ",
    "*": " ",
   }
   cipher+=' '
   plain=""
   citext=""
   for i in range(len(cipher)):
    if cipher[i] ==" ":
       plain += list(t9_mapping.values())[list(t9_mapping.keys()).index(citext)]
       citext=''
    else:
      citext+=cipher[i]
   print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Mobile Cipher ")
   print("   \u001b[32;1m|")
   print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
   print("      \u001b[32;1m[!]\u001b[37;1m",plain)  
      
def Phonetic_name(cipher):
    phonetic_names = {
           
            "Alfa":'a',
            "Alpha":'a',
            "Bravo":'b',
            "Charlie":'c',
            "Delta":'d',
            "Echo":'e',
            "Foxtrot":'f',
            "Golf":'g',
            "Hotel":'h',
            "India":'i',
            "Juliet":'j',
            "Kilo":'k',
            "Lima":'l',
            "Mike":'m',
            "November":'n',
            "Oscar":'o',
            "Papa":'p',
            "Quebec":'q',
            "Romeo":'r',
            "Sierra":'s',
            "Tango":'t',
            "Uniform":'u',
            "Victor":'v',
            "Whiskey":'w',
            "Xray":'x',
            "X-ray":'x',
            "Yankee":'y',
            "Zulu":'z',
            "(space)":' ',
            "One":'1',
            "Two":'2',
            "Three":'3',
            "Four":'4',
            "Five":'5',
            "Six":'6',
            "Seven":'7',
            "Eight":'8',
            "Nine":'9',
            "Hundred":"00",
            "Thousand":"000",
            "Dash":'-',
            "Stop":'.'
        }
    cipher+=" "
    plain=""
    citext=""
    for i in range(len(cipher)):
     if cipher[i] == ' ':
       plain += list(phonetic_names.values())[list(phonetic_names.keys()).index(citext)]
       citext=''
     else:
      citext+=cipher[i]
    print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Phonetic Name Cipher ")
    print("   \u001b[32;1m|")
    print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
    print("      \u001b[32;1m[!]\u001b[37;1m",plain)
def brute_force(cipher):
    base64(cipher)
    base32(cipher)
    ceaser(cipher)
    morse_code(cipher)
    rot47(cipher)
    t9_mappings(cipher)
    Phonetic_name(cipher)

def cleanup(code):
   return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def buildbracemap(code):
   temp_bracestack, bracemap = [], {}

   for position, command in enumerate(code):
    if command == "[": temp_bracestack.append(position)
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
   print("\n\n  \u001b[32;1m[*] \u001b[33;1mDecoding For Base64")
   print("   \u001b[32;1m|")
   print("   \u001b[32;1m|--[+] \u001b[37;1mPlain Text")
   print("      \u001b[32;1m[!]\u001b[37;1m",end='')
   return bracemap


# def brainfuck(cipher):
  

#   code     = cleanup(list(code))
#   bracemap = buildbracemap(code)

#   cells, codeptr, cellptr = [0], 0, 0

#   while codeptr < len(code):
#     command = code[codeptr]

#     if command == ">":
#       cellptr += 1
#       if cellptr == len(cells): cells.append(0)

#     if command == "<":
#       cellptr = 0 if cellptr <= 0 else cellptr - 1

#     if command == "+":
#       cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

#     if command == "-":
#       cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

#     if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
#     if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
#     if command == ".": sys.stdout.write(chr(cells[cellptr]))
#     if command == ",": cells[cellptr] = ord(getch.getch())
      
#     codeptr += 1



more = "y"
while (more == 'y'):
 option=input("  \u001b[32;1m[*]\u001b[37;1m Chose Your Option : \u001b[36;1m")
 print("   \u001b[32;1m|")
 cipher = get_data()

 if option in ['1','rsa','RSA','Rsa'] :
  pass
 elif option in ['2','weignier','weignier rsa']:
    pass
 elif option in ['3','base64','base 64']:
    base2x32(cipher)
 elif option in ['4','base32','base 32']:
    base32(cipher)
 elif option in ['5','Ceaser cipher','Rot 13']:
    ceaser(cipher)
 elif option in ['6','Morse code','morse code']:
    morse_code(cipher)
 elif option in ['7','simple reverse']:
    reverse(cipher)
 elif option in ['8','rot 47','Rot 47']:
    rot47(cipher)
 elif option in ['9','Mobile ','mobile cipher']:
    t9_mappings(cipher)
 elif option in ['10','NATO','phonetic cipher']:
    Phonetic_name(cipher)
 elif option in ['11','Brain Fuck']:
    brainfuck(cipher) 
 elif option in ['12','Brute Force']:
    brute_force(cipher) 
 else:
    print("   \u001b[32;1m|")
    print("  \u001b[32;1m[*] \u001b[31;1mEnter The Right Choice :(")
    print("   \u001b[32;1m|")
    continue
 more = input("\n\n  \u001b[32;1m[*] \u001b[37;1mWant To Play More ( y or n ) : \u001b[36;1m")
 if (more == 'y'):
     print("   \u001b[32;1m|")
 
                                                                   
    

