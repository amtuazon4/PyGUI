import grab_lexeme

lexemeArr = []

def check_syntax(lexemeArr):
    testing_list = []

    for i in lexemeArr:
        # print(i)
        testing_list.append(i)

    # for i in testing_list:
    #     print(i)

    
    
    while(True):
        change = False
        index = 0
        
        # print("-----------------------------------------")
        # for i in testing_list:
        #     print(i)


        # ---------------------------------------
        for i in testing_list:
            #Literals
            if(i[1] in ["NUMBR Literal", "NUMBAR Literal", "YARN Literal", "TROOF Literal"]):
                del testing_list[index]
                testing_list.insert(index, "literal")
                change = True
            elif(i[1] == "String Delimiter" and (index+2) < len(testing_list)):
                if(testing_list[index+1] == "literal" and testing_list[index+2][1] == "String Delimiter"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "literal")
                    change = True

            #Variable Identifier
            elif(i[1] == "Variable Identifier"):    
                del testing_list[index]
                testing_list.insert(index, "varident")
                change = True

            #Operations
            elif(i[0] in ["SUM OF", "DIFF OF", "PRODUKT OF", "QUOSHUNT OF", "MOD OF", "BIGGR OF", "SMALLR OF", "BOTH SAEM", "DIFFRINT"] and (index+3)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "expr"] and testing_list[index+2][0] == "AN" and testing_list[index+3] in ["literal", "varident", "expr"]):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "expr")
                    change = True

            #Print statement
            elif(i[0] == "VISIBLE" and (index+1)<len(testing_list)):
                if(testing_list[index+1] in ["expr", "literal", "varident"]):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "expr")
                    change = True
                
            #Input statement
            elif(i[0] == "GIMMEH" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "varident"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "expr")
                    change = True

            #Variable assignment
            elif(i == "varident" and (index+2)<len(testing_list)):
                if(testing_list[index+1][0] == "R" and testing_list[index+2] in ["literal", "varident", "expr"]):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "expr")
                    change = True

            #Variable initialization 
            elif(i[0] == "I HAS A" and (index+2)<len(testing_list)): # ***
                if(testing_list[index+1] == "varident" and testing_list[index+2][0] != "ITZ"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "varinit")
                    change = True
            elif(i[0] == "I HAS A" and (index+4)<len(testing_list)):
                if(testing_list[index+1] == "varident" and testing_list[index+2][0] == "ITZ" and testing_list[index+3] in ["literal", "expr"]):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "varinit")
                    change = True

            # Boolean operations
            elif(i[0] in ["BOTH OF", "EITHER OF", "WON OF"] and (index+3)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "expr"] and testing_list[index+2][0] == "AN" and testing_list[index+3] in ["literal", "varident", "expr"]):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "boolop")
                    change = True
            elif(i[0] == "NOT" and (index+1)<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "expr"]):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "boolop")
                    change = True
            elif(i == "boolop" and (index+3)<len(testing_list)):
                if(testing_list[index+1][0] == "AN" and testing_list[index+2] in ["boolop", "infstatement"] and testing_list[index+3][0] == "MKAY"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "infstatement")
                    change = True
            elif(i[0] in ["ANY OF", "ALL OF"] and (index+2)<len(testing_list)):
                if(testing_list[index+1] == "infstatement" and testing_list[index+2][0] == "MKAY"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "expr")
                    change = True

            #Sting concatenation
            elif(i[0] == "SMOOSH" and index+3<len(testing_list)):
                if(testing_list[index+1] in ["literal", "varident", "concats"] and testing_list[index+2][0] == "AN" and testing_list[index+3] in ["literal", "varident"]):
                    del testing_list[(index+1):(index+4)]
                    testing_list.insert((index+1), "concats")
                    change = True

            #Typecasting
            elif(i[0] == "MAEK" and (index+3)<len(testing_list)):
                if(testing_list[index+1] == "varident" and testing_list[index+2][0] == "A" and testing_list[index+3][1] == "TYPE Literal"):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "expr")
                    change = True
            elif(i[0] == "MAEK" and (index+2)<len(testing_list)):
                if(testing_list[index+1] == "varident" and testing_list[index+2][1] == "TYPE Literal"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "expr")
                    change = True

            #if-else
            elif(i[0] == "YA RLY" and (index+2)<len(testing_list)):
                if(testing_list[index+1] in ["expr", "ifelseStatement"] and testing_list[index+2] == "expr"):
                    del testing_list[(index+1):(index+3)]
                    testing_list.insert((index+1), "ifelseStatement")
                    change = True
            elif(i[0] == "YA RLY" and (index+2)<len(testing_list)):
                if(testing_list[index+1] == "expr" and testing_list[index+2][0] in ["OIC", "NO WAI"]):
                    del testing_list[index+1]
                    testing_list.insert((index+1), "ifelseStatement")
                    change = True
            elif(i[0] == "NO WAI" and (index+2)<len(testing_list)):
                if(testing_list[index+1] == "expr" and testing_list[index+2][0] == "OIC"):
                    del testing_list[index+1]
                    testing_list.insert((index+1), "ifelseStatement")
                    change = True
            
            elif(i[0] == "O RLY?" and (index+3)<len(testing_list)):
                if(testing_list[index+1][0] == "YA RLY" and testing_list[index+2] == "ifelseStatement" and testing_list[index+3][0] == "OIC"):
                    del testing_list[index:(index+4)]
                    testing_list.insert(index, "ifelse")
                    change = True
            
            elif(i[0] == "O RLY?" and (index+5)<len(testing_list)):
                if(testing_list[index+1][0] == "YA RLY" and testing_list[index+2] == "ifelseStatement" and testing_list[index+3][0] == "NO WAI" and testing_list[index+4] == "ifelseStatement" and testing_list[index+5][0] == "OIC"):
                    del testing_list[index:(index+6)]
                    testing_list.insert(index, "ifelse")
                    change = True
            
            
            
            

            #Comment
            elif(i[0] == "OBTW" or i[1] == "comment" or i[0] == "TLDR" or i[0] == "BTW"):
                del testing_list[index]
                change = True

            #Invalid
            elif(i[1] == "Invalid"):
                print("Invalid Syntax")
                return(False)
            index += 1

        if(change == False):
            print("Phase 1 Complete (No Statement Introduction)") 
            break

    for i in testing_list:
        print(i)


    # ---------------------------------------            
    # loop statements and inf boolean operations
    while(True):
        change = False
        index = 0

        for i in testing_list:
            
            if(i[0] == "SMOOSH" and (index+1)<len(testing_list)):
                if(testing_list[index+1] == "concats"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "expr")
                    change = True
            
            index += 1

        if(change == False):
            print("Phase 2 Complete (Loops and other big structs)") 
            break
    
    # for i in testing_list:
    #     print(i)
    
            
    # ---------------------------------------            
    
    while(True):
        change = False
        index = 0

        # print("-----------------------------------------")
        # for i in testing_list:
        #     print(i)
        
        
        for i in testing_list:
            #Chunky parts
            if(i == "statement" and (index+1) < len(testing_list)):
                if(testing_list[index+1] == "statement"):
                    del testing_list[index:(index+2)]
                    testing_list.insert(index, "statement")
                    change=True
            elif(i in ["varinit", "statement2"]):
                del testing_list[index]
                testing_list.insert(index, "statement")
                change = True
            elif(i in ["print", "input", "varassign", "ifelse", "expr", "case", "loop"]):
                del testing_list[index]
                testing_list.insert(index, "statement2")
                change = True
            
            elif(i[0] == "HAI" and len(testing_list) == 3):
                if(testing_list[index+1] == "statement" and testing_list[index+2][0] == "KTHXBYE"):
                    del testing_list[index:(index+3)]
                    testing_list.insert(index, "program")
                    change = True
                    print(True)

                    # for i in testing_list:
                    #     print(i)
                    return(True)
            index += 1

        # if(len(testing_list)==1):
        #     print(True) # to be changed to return later
        #     return True
        #     break
        if(change == False):
            
            print("Phase 3 Complete (finishing touches)")
            # for i in testing_list:
            #     print(i)
            
            print(False) 
            return(False)
            break






def lex_analyze(lexemeArr, the_long_string):
    lexemeArr.clear()

    lines = the_long_string.split("\n")

    lines2 = []
    for line in lines:
        if(line != ""):
            lines2.append(line.strip())    

    for i in range(0, len(lines2)):
        while(lines2[i] != ''):
            grab_lexeme.get_lexemes(lexemeArr, lines2, lines2[i], i)
    
    # for i in lexemeArr:
    #     print(i)

    check_syntax(lexemeArr)

x = """HAI

	I HAS A choice
	I HAS A input

	BTW if w/o MEBBE, 1 only, everything else is invalid
	VISIBLE "1. Compute age"
	VISIBLE "2. Compute tip"
	VISIBLE "3. Compute square area"
	VISIBLE "0. Exit"

	VISIBLE "Choice: "
	GIMMEH choice

	BOTH SAEM choice AN 1
	O RLY?
		YA RLY
			VISIBLE "Enter birth year: "
			GIMMEH input
			VISIBLE DIFF OF 2022 AN input
OBTW
	BTW uncomment this portion if you have MEBBE
	BTW else, this portion should be ignored

		MEBBE BOTH SAEM choice AN 2
			VISIBLE "Enter bill cost: "
			GIMMEH input
			VISIBLE "Tip: " PRODUCKT OF input AN 0.1
		MEBBE BOTH SAEM choice AN 3
			VISIBLE "Enter width: "
			GIMMEH input
			VISIBLE "Square Area: " PRODUCKT OF input AN input
		MEBBE BOTH SAEM choice AN 0
			VISIBLE "Goodbye"
TLDR
		NO WAI
			VISIBLE "Invalid Input!"
	OIC

	DIFFRINT BIGGR OF 3 AN choice AN 3
	O RLY?
		YA RLY
			VISIBLE "Invalid input is > 3."
	OIC

KTHXBYE"""


y = """BOTH SAEM choice AN 1
	O RLY?
		YA RLY
			I HAS A monde
			GIMMEH input
			VISIBLE DIFF OF 2022 AN input"""

z = "SMOOSH monde AN \"bruh\" AN 123"
a = "ANY OF NOT x AN BOTH OF y AN z AN EITHER OF x AN y MKAY"
b = "BOTH SAEM x AN BIGGR OF x AN y"
c = "MAEK var1 YARN"
d = """O RLY?
		YA RLY
			VISIBLE "Enter birth year: "
			GIMMEH input
            VISIBLE DIFF OF 2022 AN input
        NO WAI
            VISIBLE bruh
	OIC
    I HAS A MONDE
    I HAS A MONDE
    I HAS A MONDE
    I HAS A MONDE
    I HAS A MONDE"""
e = """GIMMEH bruh
GIMMEH bruh
GIMMEH bruh
GIMMEH bruh
GIMMEH bruh
SUM OF x AN Y
SUM OF x AN Y
SUM OF x AN Y
SUM OF x AN Y
I HAS A MONDE
"""
lex_analyze(lexemeArr, e)