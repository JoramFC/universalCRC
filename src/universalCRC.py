def _hex_2_bit_array(hex_string):
    bit_array = ""
    for i in range(0,len(hex_string)//2):
        stbyte = bin(int(hex_string[(i*2):2+(i*2)],16))[2:].zfill(8)
        bit_array = bit_array + stbyte
    return bit_array

def _xor_bin(bin1,bin2):
    result = ""
    if len(bin1) != len(bin2):
        print("ERROR XOR not same length")
        return ""
    for x,y in zip(bin1,bin2):
        if x != y:
            result = result + '1'
        else:
            result = result + '0'
    return result
    
def _check_HEX_input(hex_input):
    # Check if input is ASCII format
    if not hex_input.isascii():
        raise _CRCInputError(hex_input,"Input isn't in ASCII format")
    # Check if input is hexadecimal format
    try:
        int(hex_input,16)
    except:
        raise _CRCInputError(hex_input,"Input isn't in hexadecimal format") from None
    # Check if input length is even number
    if (len(hex_input.strip())%2) != 0:
        raise _CRCInputError(hex_input,"Input length isn't an even number")

def compute_CRC(hexadecimal_input,poly=0,init=0,type=8):
    """
    This function computes the CRC of a given hexadecimal string
    :hexadecimal_input: An hexadecimal string representing the data with which the CRC will be computed (length must be an even number)
    :poly: The polynom used for CRC computation (must be a positive integer)
    :init: The init value used for CRC computation (must be a positive integer)
    :type: CRC type (must be either 8, 16, 32 or 64)
    :return: integer
    """
    if not isinstance(type, int):
        raise _CRCTypeError(str(type),"Type isn't an integer")
    if type not in [8,16,32,64]:
        raise _CRCTypeError(str(type),"Type isn't managed")
        
    # Convert input into bit array
    _check_HEX_input(hexadecimal_input)
    bit_array = _hex_2_bit_array(hexadecimal_input.strip())

    # Compare parameter size with type
    if (len(hex(init)[2:])*4) > type:
        raise _CRCParameterError(str(init),"Init size is not compliant with CRC type")
    if (len(hex(poly)[2:])*4) > type:
        raise _CRCParameterError(str(poly),"Polynom size is not compliant with CRC type")

    # Convert init to bits
    try:
        init_bits = _hex_2_bit_array(hex(init)[2:].zfill(2))
    except:
        raise _CRCParameterError(str(init),"Init isn't a valid number (must be a positive integer)") from None
    # Convert polynom to bits
    try:
        poly_bits = _hex_2_bit_array(hex(poly)[2:].zfill(2))
    except:
        raise _CRCParameterError(str(poly),"Polynom isn't a valid number (must be a positive integer)") from None

    # Convert hex input to bits and pad 0s at the end
    bit_array =  bit_array + '0'*type
    bit_array = _xor_bin(init_bits,bit_array[:len(init_bits)]) + bit_array[len(init_bits):]

    # Compute CRC
    for i in range(0,len(bit_array)-type):
        if(bit_array[0]=='1'):
            bit_array = bit_array[1:]+'0'
            bit_array = _xor_bin(poly_bits,bit_array[:len(poly_bits)]) + bit_array[len(poly_bits):]
        else:
            bit_array = bit_array[1:]+'0'
    return int(bit_array[:type],2)
    
# ERROR classes
class _CRCError(Exception):
    pass

class _CRCInputError(_CRCError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class _CRCParameterError(_CRCError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class _CRCTypeError(_CRCError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message