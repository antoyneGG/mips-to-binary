from Registers.conversions import DecimalToBin, HexToBin, HexToDecimal, checkHex, checkNum
from Registers.registers import getRegister, validateRegister
from Instructions import Jformat
from Instructions import Iformat
from Instructions import Rformat

Rtype1 = ['sll', 'srl', 'sra']
Rtype2 = ['jr']
Rtype3 = ['div', 'divu', 'mult', 'multu']
Rtype4 = ['mfhi', 'mflo']

Itype1 = ['beq', 'bne']
Itype2 = ['lbu', 'lhu', 'lui', 'sw', 'sb', 'sh', 'sc', 'lw', 'll']

def validate(instruction):
    if(Rformat.validateRtype(instruction)):
        return 1
    elif(Iformat.validateItype(instruction)):
        return 2
    elif(Jformat.validateJtype(instruction)):
        return 3
    else:
        raise TypeError("ERROR: Instruccion " + instruction + " invalida")

def translateR(line):
    ins = line[0]
    opcode = "000000"
    rs = "00000"
    rt = "00000"
    rd = "00000"
    shamt = "00000"
    funct = Rformat.getFunction(ins)
    if(len(line) <= 4):
        if(ins in Rtype1):
            if(len(line) == 4):
                if(validateRegister(line[2]) and validateRegister(line[1]) and not validateRegister(line[3])):
                    rt = getRegister(line[2])
                    rd = getRegister(line[1])
                    shamt = line[3]
                    if(checkHex(shamt)):
                        shamt = HexToBin(shamt)
                    elif(checkNum(shamt)):
                        shamt = DecimalToBin(shamt)
                    else:
                        raise TypeError("ERROR: Shamt invalido")
                    shamt = shamt.zfill(5)
                    if(len(shamt) > 5):
                        raise TypeError("ERROR: Shamt superior a 5 bits")
                else:
                    raise TypeError("ERROR: Argumentos invalidos para " + ins)
            else:
                raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)
        elif(ins in Rtype2):
            if(len(line) == 2):
                if(validateRegister(line[1])):
                    rs = getRegister(line[1])
                else:
                    raise TypeError("ERROR: Argumentos invalidos para " + ins)
            else:
                raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)
        elif(ins in Rtype3):
            if(len(line) == 3):
                if(validateRegister(line[1]) and validateRegister(line[2])):
                    rs = getRegister(line[1])
                    rt = getRegister(line[2])
                else:
                    raise TypeError("ERROR: Argumentos invalidos para " + ins)
            else:
                raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)
        elif(ins in Rtype4):
            if(len(line) == 2):
                if(validateRegister(line[1])):
                    rd = getRegister(line[1])
                else:
                    raise TypeError("ERROR: Argumentos invalidos para " + ins)
            else:
                raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)
        else:
            if(validateRegister(line[1]) and validateRegister(line[2]) and validateRegister(line[3])):
                rd = getRegister(line[1])
                rs = getRegister(line[2])
                rt = getRegister(line[3])
            else:
                raise TypeError("ERROR: Argumentos invalidos para " + ins)
        translated_line = opcode + rs + rt + rd + shamt + funct
        #print(len(translated_line))
        #print(translated_line)
        return translated_line
    else:
        raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)

def translateI(line, address):
    ins = line[0]
    opcode = Iformat.getOpcode(ins)
    rs = "00000"
    rt = "00000"
    immediate = "0000000000000000"
    if(len(line) == 4 or len(line) == 3):
        if(ins in Itype1):
            if(validateRegister(line[1]) and validateRegister(line[2]) and not validateRegister(line[3])):
                rs = getRegister(line[1])
                rt = getRegister(line[2])
                immediate = line[3]
                if(checkHex(immediate)):
                    immediate = HexToDecimal(immediate)
                    address = HexToDecimal(address)
                    immediate = DecimalToBin(str(int((immediate - (address + 4))/4)))
                elif(checkNum(immediate)):
                    immediate = DecimalToBin(immediate)
                else:
                    raise TypeError("ERROR: Immediate en formato incorrecto")
                immediate = immediate.zfill(16)
                if(len(immediate) > 16):
                    raise TypeError("ERROR: Immediate superior a 16 bits")
            else:
                raise TypeError("ERROR: Argumentos invalidos para " + ins)
        elif(ins in Itype2):
            if(ins == "lui"):
                if(len(line) == 3):
                    if(validateRegister(line[1]) and not validateRegister(line[2])):
                        rt = getRegister(line[1])
                        immediate = line[2]
                        if(checkHex(immediate)):
                            immediate = HexToBin(immediate)
                        elif(checkNum(immediate)):
                            immediate = DecimalToBin(immediate)
                        else:
                            raise TypeError("ERROR: Immediate en formato incorrecto")
                        immediate = immediate.zfill(16)
                        if(len(immediate) > 16):
                            raise TypeError("ERROR: Immediate superior a 16 bits")
                    else:
                        raise TypeError("ERROR: Argumentos invalidos para " + ins)
                else:
                    raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)
            elif(validateRegister(line[1]) and not validateRegister(line[2]) and validateRegister(line[3])):
                rt = getRegister(line[1])
                rs = getRegister(line[3])
                immediate = line[2]
                if(checkHex(immediate)):
                    immediate = HexToBin(immediate)
                elif(checkNum(immediate)):
                    immediate = DecimalToBin(immediate)
                else:
                    raise TypeError("ERROR: Immediate en formato incorrecto")
                immediate = immediate.zfill(16)
                if(len(immediate) > 16):
                    raise TypeError("ERROR: Immediate superior a 16 bits")
            else:
                raise TypeError("ERROR: Argumentos invalidos para " + ins)
        else:
            if(validateRegister(line[1]) and validateRegister(line[2]) and not validateRegister(line[3])):
                rt = getRegister(line[1])
                rs = getRegister(line[2])
                immediate = line[3]
                if(checkHex(immediate)):
                    immediate = HexToBin(immediate)
                elif(checkNum(immediate)):
                    immediate = DecimalToBin(immediate)
                else:
                    raise TypeError("ERROR: Immediate en formato incorrecto")
                immediate = immediate.zfill(16)
                if(len(immediate) > 16):
                    raise TypeError("ERROR: Immediate superior a 16 bits")
            else:
                raise TypeError("ERROR: Argumentos invalidos para " + ins)
        translated_line = opcode + rs + rt + immediate
        #print(len(translated_line))
        #print(translated_line)
        return translated_line
    else:
        raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)

def transtaleJ(line):
    ins = line[0]
    opcode = Jformat.getOpcode(ins)
    address = "00000000000000000000000000"
    if(len(line) == 2):
        if(not validateRegister(line[1])):
            address = line[1]
            if(checkHex(address)):
                address = DecimalToBin(str(HexToDecimal(address) // 4))
            elif(checkNum(address)):
                address = DecimalToBin(str(address // 4))
            else:
                raise TypeError("ERROR: Address invalido para " + ins)
            address = address.zfill(26)
            while(len(address) > 26):
                address = address.replace(address[0], '', 1)
        else:
            raise TypeError("ERROR: Argumento invalido para " + ins)
        translated_line = opcode + address
        #print(len(translated_line))
        #print(translated_line)
        return translated_line
    else:
        raise TypeError("ERROR: Cantidad de argumentos invalida para " + ins)

def translation(line, address):
    if(line[1] == "$zero" or line[1] == "$gp"):
        raise ValueError("ERROR: El registro " + line[1] + " no es modificable")
    if(validate(line[0]) == 1):
        return translateR(line)
    elif(validate(line[0]) == 2):
        return translateI(line, address)
    elif(validate(line[0]) == 3):
        return transtaleJ(line)
