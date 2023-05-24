
dct = {'a':'ah',
       'e':'eh',
       'i': 'ee',
       'o':'oh',
       'u': 'oo',
       'ai':'eye',
       'ae':'eye',
       'ao':'ow',
       'au':'ow',
       'ei':'ay',
       'eu':'eh-oo',
       'iu':'ew',
       'oi':'oyo',
       'ou':'ow',
       'ui':'ooey',
       'aw':'w',
       'iw':'v',
       'ew':'v',
       'uw':'w',
       'ow':'w'}

def converting(word):
    i = 0
    conv = []
    while i < len(word):
        char = word[i]
        if i < len(word)-1:
            chars = char + word[i + 1]
            if chars in dct:
                pron = dct[chars] + "-"
                i+=2
            elif char in dct:
                pron = dct[char] + "-"
                i+=1
            else:
                pron = char
                i+=1
        else:
            if char in dct:
                pron=dct[char]
            else:
                pron=char
            i+=1
        conv+=pron
    return "".join(conv)

def isValid(word):
    hwletters = "a,e,i,o,u,p,k,h,l,m,n,w ,\'"
    for letter in word:
        if letter not in hwletters:
            print(letter, "is not a valid hawaiian character")
            return False
    return True
    
def main():
    word = 'yes'
    while word!="N" and word != "NO":
        word = input("Enter a Hawaiian word to be pronounced.\n")
        word = word.lower()
        isValid(word)
        print(converting(word).capitalize())
        word = input("Do you want to enter another word? Y/YES/N/NO\n")
            
main()
