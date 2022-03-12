fiveCycles = ["lbu", "lhu", "lw"]

threeCycles = ["beq", "bne", "j", "jal"]

def cyclesCounter(instruction):

    if(instruction in fiveCycles):

        return 5

    elif(instruction in threeCycles):

        return 3

    else:
        
        return 4
