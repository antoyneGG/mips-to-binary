opcode = {
        "addi"  : "001000",
        "addiu" : "001001",
        "andi"  : "001100",
        "beq"   : "000100",
        "bne"   : "000101",
        "lbu"   : "100100",
        "lhu"   : "100101",
        "ll"    : "110000",
        "lui"   : "001111",
        "lw"    : "100011",
        "ori"   : "001101",
        "slti"  : "001010",
        "sltiu" : "001011",
        "sb"    : "101000",
        "sc"    : "111000",
        "sh"    : "101001",
        "sw"    : "101011"
    }

def getOpcode(instruction):
    return opcode[instruction]

def validateItype(instruction):
    if(instruction in opcode.keys()):
        return True
    else:
        return False