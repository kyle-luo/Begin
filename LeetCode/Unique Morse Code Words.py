#International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

#For convenience, the full table for the 26 letters of the English alphabet is given below:

#[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

#Return the number of different transformations among all words we have.

#Example:
#Input: words = ["gin", "zen", "gig", "msg"]
#Output: 2
#Explanation:
#The transformation of each word is:
#"gin" -> "--...-."
#"zen" -> "--...-."
#"gig" -> "--...--."
#"msg" -> "--...--."

#There are 2 different transformations, "--...-." and "--...--.".

def uniqueMorseRepresentations(words):
    umwords = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    newlist = []
    for word in words:
        translate = ''
        for x in word:
            translate += umwords[atoz.index(x)]
        newlist.append(translate)
    newlist = set(newlist)
    return len(newlist)


uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])