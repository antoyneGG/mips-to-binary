from tcpu import cyclesCounter
from Registers.conversions import BinToHex, DecimalToBin, checkNum
from sys import stdin
from translator import translation

def program(mips, clock):
    
    try:

        labels = {}

        lines = []

        tcpu = 0

        flag = False

        lastLabel = ""

        lastLoopCounter = 0

        loops = []
        
        PC = 4194304

        instruction = mips[0].replace(',', ' ').replace('(', ' ').replace(')', ' ').split()

        s = 0

        while(instruction != []):

            line = []

            if(len(instruction) == 1 and instruction[0][-1] == ':'):

                labels[instruction[0][:-1]] = BinToHex(DecimalToBin(PC))

                lastLabel = instruction[0][:-1]

                flag = True

            else:

                tcpu += cyclesCounter(instruction[0])

                if(flag):

                    lastLoopCounter += cyclesCounter(instruction[0])

                if(instruction[0] == "beq" or instruction[0] == "bne"):

                    tcpu += 3
                    
                if(instruction[0] == "j" or instruction[0] == "jal" and instruction[1] == lastLabel):

                    tcpu -= lastLoopCounter

                    loops.append(lastLoopCounter)

                    flag = 0

                    lastLoopCounter = 0

                elif(instruction[0] == "j" or instruction[0] == "jal" or instruction[0] == "jr"):

                    flag = 0

                    lastLoopCounter = 0

                line.append(instruction)

                line.append(BinToHex(DecimalToBin(PC)))

                PC += 4
                lines.append(line)

            s += 1

            instruction = mips[s].replace(',', ' ').replace('(', ' ').replace(')', ' ').split()

        #print(labels)
        #print(tcpu)

        binary = []

        for i in range(len(lines)):

            if(lines[i][0][0] == "beq" or lines[i][0][0] == "bne" and not checkNum(lines[i][0][3])):

                if(lines[i][0][3] in labels.keys()):

                    lines[i][0][3] = labels[lines[i][0][3]]

                else:

                    raise ValueError("ERROR: Label en instruccion " + lines[i][0][0] + " inexistente")

            elif(lines[i][0][0] == "j" or lines[i][0][0] == "jal" and not checkNum(lines[i][0][1])):

                if(lines[i][0][1] in labels.keys()):

                    lines[i][0][1] = labels[lines[i][0][1]]

                else:

                    raise ValueError("ERROR: Label en instruccion " + lines[i][0][0] + " inexistente")

            binary.append(translation(lines[i][0], lines[i][1]) + '\n')

        #print(lines)
        #print(binary)
        for i in binary:

            print(i)

        tcpu = tcpu/clock

        tcpu = "Tcpu = " + str(tcpu)

        if(len(loops) == 1):

            loops[0] = loops[0]/clock

            tcpu += " + " + str(loops[0]) + "n"

        elif(len(loops) > 1):

            for i in range(len(loops)):

                loops[i] = loops[i]/clock

                tcpu += " + " + str(loops[i]) + "n" + str(i + 1)

        return binary, tcpu

    except TypeError as error:

        print(error)
        
        return str(error), ''
    
    except ValueError as error:

        print(error)

        return str(error), ''
    