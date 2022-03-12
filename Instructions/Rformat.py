functions = {
        "add"   : "100000",
        "addu"  : "100001",
        "and"   : "100100",
        "jr"    : "001000",
        "nor"   : "100111",
        "or"    : "100101",
        "slt"   : "101010",
        "sltu"  : "101011",
        "sll"   : "000000",
        "srl"   : "000010",
        "sub"   : "100010",
        "subu"  : "100011",
        "mult"  : "011000",
        "div"   : "011010",
        "multu" : "011001",
        "divu"  : "011011",
        "mflo"  : "010010",
        "mfhi"  : "010000",
        "sra"   : "000011"
    }

def validateRtype(instruction):
    if(instruction in functions.keys()):
        return True
    else:
        return False

def getFunction(instruction):
    return functions[instruction]