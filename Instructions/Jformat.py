opcode = {
        "j"     : "000010",
        "jal"   : "000011" 
    }

def getOpcode(instruction):
    return opcode[instruction]

def validateJtype(instruction):
    if(instruction in opcode.keys()):
        return True
    else:
        return False

