#imports
import main as mn

#Combo box to choose Cipher
combo_box = mn.ttk.Combobox(values = ["Shift Cipher", "Transposition Cipher"])
combo_box.grid(row = 4, column = 0, padx = 35)
combo_box.current(0)

text_combo = mn.ttk.Combobox(values = ["User Input", "Short Text", "Long Text"])
text_combo.grid(row = 0, column = 0, padx = 35)
text_combo.current(0)

#move encrypted Text
def move_to_decrypt():
    empty_decrypt = "Error! The ciphertext box or key box is empty\n"
    empty_encrypt = "Error! The plaintext box or key box is empty\n"
    keylim = "Error! Please enter a keyword with length between 2 and 7 letters\n"
    source_text = encryption_box.get("1.0", mn.tkinter.END)
    shift_key_no = shift_key_box.get("1.0", mn.tkinter.END)


    if empty_decrypt in source_text:
        encryption_box.delete("1.0", mn.tkinter.END)

    elif (len(source_text) < 2) or (len(shift_key_no) < 2):
        decryption_box.insert("1.0", empty_encrypt)

    #elif (combo_box.get() == "Shift Cipher") and (mn.MainWindow.checkInt(shift_key_no) == False):
        #decryption_box.insert("1.0", "Error! Please enter int value for shift key" + shift_key_no[0])

    elif ((combo_box.get() == "Transposition Cipher") and ((len(shift_key_no) > 8) or  (len(shift_key_no) < 3))):
        decryption_box.insert("1.0", keylim)

    else:
        if (combo_box.get() == "Shift Cipher"):
            decryption_box.delete("1.0", mn.tkinter.END)
            decryption_box.insert("1.0", mn.MainWindow.shift_encryption(source_text, int(shift_key_no)))
            #delete after moving text
            encryption_box.delete("1.0", mn.tkinter.END)

        elif (combo_box.get() == "Transposition Cipher"):
            shift_key_no = shift_key_no[:-1]
            source_text = mn.MainWindow.only_letters(source_text)
            decryption_box.delete("1.0", mn.tkinter.END)
            decryption_box.insert("1.0", mn.MainWindow.trans_encryption(source_text, shift_key_no))
            #delete after moving text
            encryption_box.delete("1.0", mn.tkinter.END)

#move decrypted text
def move_to_encrypt():
    empty_decrypt = "Error! The ciphertext box or key box is empty\n"
    empty_encrypt = "Error! The plaintext box or key box is empty\n"
    source_text = decryption_box.get("1.0", mn.tkinter.END)
    shift_key_no = shift_key_box.get("1.0", mn.tkinter.END)

    if empty_encrypt in source_text:
        decryption_box.delete("1.0", mn.tkinter.END)

    elif (len(source_text) < 2) or (len(shift_key_no) < 2):
        encryption_box.insert("1.0", empty_decrypt)

    else:
        if (combo_box.get() == "Shift Cipher"):
            encryption_box.delete("1.0", mn.tkinter.END)
            encryption_box.insert("1.0", mn.MainWindow.shift_decryption(source_text, int(shift_key_no)))
            #delete after moving text
            decryption_box.delete("1.0", mn.tkinter.END)

        elif (combo_box.get() == "Transposition Cipher"):
            shift_key_no = shift_key_no[:-1]
            source_text = mn.MainWindow.only_letters(source_text)
            encryption_box.delete("1.0", mn.tkinter.END)
            encryption_box.insert("1.0", mn.MainWindow.trans_decryption(source_text, shift_key_no))
            #delete after moving text
            decryption_box.delete("1.0", mn.tkinter.END)

#move to cryptanalysis box
def break_cipher():
    empty_decrypt = "Error! The Ciphertext box is empty\n"
    empty_encrypt = "Error! The plaintext box or key box is empty\n"
    keylim = "Error! Please enter a keyword with length between 2 and 7 letters\n"
    fit_box_text = "Testing the fitness of each permutation"
    source_text = decryption_box.get("1.0", mn.tkinter.END)

    if empty_encrypt in source_text:
        decryption_box.delete("1.0", mn.tkinter.END)

    elif keylim in source_text:
        pass

    elif (len(source_text) < 2):
        cryptanalysis_box.insert("1.0", empty_decrypt)

    else:
        cryptanalysis_box.delete("1.0", mn.tkinter.END)
        if(combo_box.get() == "Shift Cipher"):
            cryptanalysis_box.insert("1.0", mn.MainWindow.brute_shift(source_text))
            fitness_box.delete("1.0", mn.tkinter.END)
            fitness_box.insert("1.0", mn.MainWindow.fitness_test(source_text))
            hacking_result_box.delete("1.0", mn.tkinter.END)
            hacking_result_box.insert("1.0", mn.MainWindow.hack_result(source_text))

        elif (combo_box.get() == "Transposition Cipher"):
            cryptanalysis_box.insert("1.0", mn.MainWindow.key_test())
            fitness_box.delete("1.0", mn.tkinter.END)
            fitness_box.insert("1.0", fit_box_text)
            hacking_result_box.delete("1.0", mn.tkinter.END)
            hacking_result_box.insert("1.0", mn.MainWindow.key_search(source_text))

def reset_boxes():
    encryption_box.delete("1.0", mn.tkinter.END)
    decryption_box.delete("1.0", mn.tkinter.END)
    cryptanalysis_box.delete("1.0", mn.tkinter.END)
    fitness_box.delete("1.0", mn.tkinter.END)
    hacking_result_box.delete("1.0", mn.tkinter.END)
    shift_key_box.delete("1.0", mn.tkinter.END)

def switch_text():
    encryption_box.delete("1.0", mn.tkinter.END)
    if(text_combo.get() == "Short Text"):
        with open("SomeoneLikeYou.txt", 'r') as f:
            encryption_box.insert("1.0", f.read())
    elif(text_combo.get() == "Long Text"):
        with open("mockingbird.txt", 'r') as f:
            encryption_box.insert("1.0", f.read())

title_label = mn.tkinter.Label(text = "Simple Crytpography", bg = "light grey", font = ("times", 20))
title_label.grid(row = 0, column = 1)

#encryption label
plaintext_label = mn.tkinter.Label(text = "Plaintext", font = ("times", 17), bg = "light grey")
plaintext_label.grid(row = 1, column = 0, sticky = mn.tkinter.W)

#encryption box
encryption_box = mn.tkinter.Text(height = 14, width = 52, font = ("times", 16), wrap = "word")
encryption_box.grid(row = 2, column = 0, sticky = mn.tkinter.W)

#decryption label
ciphertext_label = mn.tkinter.Label(text = "Ciphertext", font = ("times", 17), bg = "light grey", pady = 20)
ciphertext_label.grid(row = 1, column = 2, sticky = mn.tkinter.E)

#decryption box
decryption_box = mn.tkinter.Text(height = 14, width = 52, font = ("times", 16), wrap = "word")
decryption_box.grid(row = 2, column = 2, sticky = mn.tkinter.E)

#shift key label
shift_key = mn.tkinter.Label(text = "Key", font  = ("times", 17), bg = "light grey",)
shift_key.grid(row = 2, column = 1, sticky = mn.tkinter.N)

#shift key box
shift_key_box = mn.tkinter.Text(height = 2, width = 7)
shift_key_box.grid(row = 2, column = 1)

#encryption button
encryption_button = mn.tkinter.Button(text = "ENCRYPT", font = ("times", 15), width = 53, \
pady = 15, command = move_to_decrypt, bg = "light grey")
encryption_button.grid(row = 3, column = 0, sticky = mn.tkinter.W)

#decryption button
decryption_button = mn.tkinter.Button(text = "DECRYPT", font = ("times", 15), width = 53, \
pady = 15, command = move_to_encrypt, bg = "light grey")
decryption_button.grid(row = 3, column = 2, sticky = mn.tkinter.E)

#choose Cipher
choose_cipher_label = mn.tkinter.Label(text = "Choose Cipher: ", font = ("times", 15), bg = "light grey")
choose_cipher_label.grid(row = 4, column = 0, sticky = mn.tkinter.W, pady = 10)

#Cryptanalysis label
cryptanalysis_label = mn.tkinter.Label(text = "Cryptanalysis", font = ("times", 15), bg = "light grey")
cryptanalysis_label.grid(row = 5, column = 0, sticky = mn.tkinter.W, pady = 10)

#Cryptanalysis box
cryptanalysis_box = mn.tkinter.Text(height = 14, width = 52, font = ("times", 16), fg = "white", bg = "black", wrap = "word")
cryptanalysis_box.grid(row = 6, column = 0, sticky = mn.tkinter.W)

#Fitness label
fitness_label = mn.tkinter.Label(text = "Fitness", font = ("times", 15), bg = "light grey")
fitness_label.grid(row = 5, column = 1, pady = 10)

#Fitness box
fitness_box = mn.tkinter.Text(height = 14, width = 52, font = ("times", 16), fg = "white", bg = "black")
fitness_box.grid(row = 6, column = 1)

#Hacking result Label
hacking_result_label = mn.tkinter.Label(text = "Hacking result", font = ("times", 17), bg = "light grey", pady = 20)
hacking_result_label.grid(row = 5, column = 2, sticky = mn.tkinter.E)

#Hacking result box
hacking_result_box = mn.tkinter.Text(height = 14, width = 52, font = ("times", 16), fg = "white", bg = "black")
hacking_result_box.grid(row = 6, column = 2, sticky = mn.tkinter.E)

#Hack Button
hack_button = mn.tkinter.Button(text = "Break Cipher", font = ("times", 15), width = 50, \
pady = 15, command = break_cipher, bg = "light grey")
hack_button.grid(row = 3, column = 1)

#reset Button
reset_button = mn.tkinter.Button(text = "RESET", font = ("times", 15), width = 30, command = reset_boxes, bg = "light grey")
reset_button.grid(row = 0, column = 2, sticky = mn.tkinter.E)

#choose text
choose_text_label = mn.tkinter.Label(text = "Choose Text: ", font = ("times", 15), bg = "light grey")
choose_text_label.grid(row = 0, column = 0, sticky = mn.tkinter.W, pady = 10)

#switch text Button
switch_button = mn.tkinter.Button(text = "Choose", font = ("times", 15), width = 7, command = switch_text, bg = "light grey")
switch_button.grid(row = 0, column = 0, sticky = mn.tkinter.E)

#loop program
if __name__ == "__main__":
    mn.root.mainloop()
