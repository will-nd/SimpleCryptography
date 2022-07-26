# imports
import ngram_score as ns
import numpy as np
import math
import time
import tkinter
from tkinter import ttk
from pycipher import ColTrans
from string import ascii_letters
from itertools import permutations


#main class
class MainWindow(tkinter.Tk):
     #This is the main window, a child class of tkinter
    def __init__(self):
        super().__init__()\

        #The main window properties
        # main window title
        self.title("Simple Cryptography")
        # main window size
        self.geometry("1280x1000")
        # main window color
        self.configure(background = "light grey")

    def checkInt(str):
        if str[0] in ('-', '+'):
            return str[1:].isdigit()
        return str.isdigit()

    #function that returns text as capitals with
    #no whitespace or punctuation
    def only_letters(text):
        result = ""

        for i in range(len(text)):
            letter = text[i]
            if (letter.isalpha()):
                if (letter.isupper()):
                    result += letter
                elif (letter.islower()):
                    letter = letter.upper()
                    result += letter
            else:
                pass
        return(result)

    #Shift cipher encryption function
    def shift_encryption(plaintext, shift_key):
        encryption_result = ""

        #go through every character
        for i in range(len(plaintext)):
            letter = plaintext[i]
            #if letter do shift
            if (letter.isalpha()):
                if (letter.isupper()):
                    encryption_result += chr((ord(letter) + shift_key - 65) %26 +65)
                elif (letter.islower()):
                    encryption_result += chr((ord(letter) + shift_key - 97) %26 +97)
            #else just add character
            else:
                encryption_result += letter

        return(encryption_result)

    #Shift cipher decryption function
    def shift_decryption(ciphertext, shift_key):
        decryption_result = ""

        #go through every character
        for i in range(len(ciphertext)):
            letter = ciphertext[i]
            if (letter.isalpha()):
                if (letter.isupper()):
                    decryption_result += chr((ord(letter) - shift_key - 65) %26 +65)
                elif (letter.islower()):
                    decryption_result += chr((ord(letter) - shift_key - 97) %26 +97)
            else:
                decryption_result += letter

        return(decryption_result)

    #Columnar transposition encryption function
    def trans_encryption(plaintext, keyword):
        ciphertext = ''

        #sort keyword into alphabetical order
        srtd_key = sorted(keyword)

        #create unordered numbered list of keyword
        key_lst = list(range(len(keyword)))
        iter = 0
        for i in range(len(srtd_key)):
            for j in range(len(keyword)):
                if srtd_key[i] == keyword[j]:
                    if srtd_key[i-1] == keyword[j]:
                        pass
                    else:
                        key_lst[j] = iter
                        iter += 1

        #goes to i letter in numbered list fill in ciphertext
        #starting from that index in plaintext traverse plaintext
        #by len(keyword) and add letter to ciphertext
        for i in range(len(keyword)):
            ciphertext += plaintext[key_lst.index(i)::len(keyword)]

        return(ciphertext)

    #columnar transposition decryption function
    def trans_decryption(cipher, keyword):
        plaintext = ['_']*len(cipher)

        msg_len = len(cipher)
        key_len = len(keyword)
        srtd_key = sorted(keyword)

        #create unordered numbered list of keyword
        key_lst = list(range(len(keyword)))
        iter = 0
        for i in range(len(srtd_key)):
            for j in range(len(keyword)):
                if srtd_key[i] == keyword[j]:
                    if srtd_key[i-1] == keyword[j]:
                        pass
                    else:
                        key_lst[j] = iter
                        iter += 1

        #create list to obtain location of each letter
        num_loc = list(range(len(keyword)))
        x = 0
        for i in range(len(keyword) + 1):
            for j in range(len(keyword)):
                if key_lst[j] == i:
                    num_loc[x] = j
                    x += 1
        #where ciphertext starts from each time
        start = 0
        for i in range(len(keyword)):
            #essentially no of rows
            col_len = (int)(msg_len/key_len)
            #if condition: then is coulmn before null values
            #so column must be one longer than those that
            #would have null values
            if num_loc[i] < msg_len%key_len:
                col_len += 1
            #input character from index start to col_len in Ciphertext
            #into plaintext in increments of len(keyword)
            plaintext[num_loc[i]::key_len] = cipher[start:start+col_len]
            start += col_len

        return''.join(plaintext)

    #do every possible shift of ciphertext
    def brute_shift(ciphertext):
        fin_brute = [''] * 26

        for j in range(26):
            shift_result = ""
            #go through every character
            for i in range(len(ciphertext)):
                letter = ciphertext[i]
                if (letter.isalpha()):
                    if (letter.isupper()):
                        shift_result += chr((ord(letter) + (j+1) - 65) %26 +65)
                    elif (letter.islower()):
                        shift_result += chr((ord(letter) + (j+1) - 97) %26 +97)
                else:
                    shift_result += letter
            #list of all possible shifts of ciphertext
            fin_brute[j] = shift_result

        return(fin_brute)


    def fitness_test(ciphertext):
        fitness = ns.ngram_score('english_quadgrams.txt')
        fit_test = [''] * 26

        for j in range(26):
            shift_result = ""
            #go through every character
            for i in range(len(ciphertext)):
                letter = ciphertext[i]
                if (letter.isalpha()):
                    if (letter.isupper()):
                        shift_result += chr((ord(letter) + (j+1) - 65) %26 +65)
                    elif (letter.islower()):
                        letter = letter.upper()
                        shift_result += chr((ord(letter) + (j+1) - 65) %26 +65)
                else:
                    pass
            #gives fitness score of every possible shift of ciphertext
            fit_test[j] = fitness.score(shift_result)

        return(fit_test)

    def hack_result(ciphertext):
        fitness = ns.ngram_score('english_quadgrams.txt')
        fit_test = [''] * 26
        fin_brute = [''] * 26

        for j in range(26):
            shift_result = ""
            #go through every character
            for i in range(len(ciphertext)):
                letter = ciphertext[i]
                if (letter.isalpha()):
                    if (letter.isupper()):
                        shift_result += chr((ord(letter) + (j+1) - 65) %26 +65)
                    elif (letter.islower()):
                        letter = letter.upper()
                        shift_result += chr((ord(letter) + (j+1) - 65) %26 +65)
                else:
                    pass
            fin_brute[j] = shift_result
            fit_test[j] = fitness.score(shift_result)
        tmp = max(fit_test)
        index = fit_test.index(tmp)
        key = 26 - (fit_test.index(tmp) + 1)

        return("The best candidate with key: " + str(key) + "\n" + fin_brute[index])

    def key_test():
        perms = []
        for i in range(2, 8):
            key,value = i,math.factorial(i)
            perms.append((key,value))
        return("Testing possible keywords of length x with number of permutations y (x,y)\n" + str(perms))

    def key_search(ciphertext):
        fitness = ns.ngram_score('english_quadgrams.txt')
        fit_test = []
        trans_list = []
        key_list = []
        alphalist = ["A"]
        alpha7 = "BCDEFG"
        for i in range(len(alpha7)):
            alphalist.append(alpha7[i])
            perm = list(permutations(alphalist))
            for j in range(len(perm)):
                key = str(perm[j])
                key = key.replace("'", "")
                key = key.replace(", ", "")
                key = key.replace("(", "")
                key = key.replace(")", "")
                key_list.append(key)
                trans = ColTrans(key).decipher(ciphertext)
                trans_list.append(trans)
                fit_score = fitness.score(trans)
                fit_test.append(fit_score)
        tmp = max(fit_test)
        index = fit_test.index(tmp)
        return("The best candidate with key order: " + key_list[index] + "\n" + trans_list[index])



root = MainWindow()
if __name__ == "__main__":
    root.mainloop()
