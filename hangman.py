import random,math
words=['howling','jazz','emulator','explanation','remarkable','mysterious','algorithm','repertoire','frivilous','superficial','dementia','fuzzy','rhythm','cowboy']

print("Guess the blank letters")

def init_game():
    #word selection
    a=random.randint(0,len(words)-1)
    word=words[a]
    word2=list(word)

        
    #blank words calculation
    word2_length=len(word2)-1
    word2_len=math.ceil(len(word2)/2-1)
    blank_1=[]

   
    
    for i in range(word2_len):
        blank_1.append(random.randint(0,word2_length))
    
   

    
    blanks=len(blank_1)
    for j in range(blanks):
        
        word2[blank_1[j]]='_'
    
    word3=' '.join(word2)
    
    
    return word3,word,word2,blanks
   
    






def start_user_input(ans_word,word_list,blanks):
    ans_word=list(ans_word)
    f_ans = ''.join(ans_word)
    tries=5
    for i in range(6,0,-1):
        
        while blanks!=0 and tries!=0 and word_list!= ans_word:
            disp_list =' ' .join(word_list)
            #print(word_list)
            print(disp_list)
            u_input=input("Type a letter :")
            if u_input in ans_word:
                for j in range(len(ans_word)):
                    if u_input == ans_word[j] and word_list[j] != ans_word[j]:
                        word_list[j]=u_input
                        blanks -= 1
                        
                        
                        break
                        
                    else:
                        continue
                
            else:
                tries -= 1
                print("Error")
                print("%s tries left" % (tries))
                continue
    if blanks == 0:
        print("Good you answered correctly")
        print(f_ans)
        ret=input("retry? y/n")
        if ret == 'y' or ret == 'Y':
            start_game()
        else:
            print("bye")
            
    else:
        if tries == 0:
            print("out of tries")            
        print("Correct answer")
        print(f_ans)
        ret=input("retry? y/n")
        if ret == 'y' or ret == 'Y':
            start_game()
        else:
            print("bye")
            
        
        
    
    

    
def start_game():
    b_word,ans_word,word_list,blanks=init_game()
    print(b_word)
    start_user_input(ans_word,word_list,blanks)

start_game()
