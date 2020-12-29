preset_list = {
    'CRC8' : {'poly': 0x07,'init': 0x00,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'CDMA2000' : {'poly': 0x9B,'init': 0xFF,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'DARC' : {'poly': 0x39,'init': 0x00,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'EBU' : {'poly': 0x1D,'init': 0xFF,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'ARC' : {'poly': 0x8005,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
}

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

def inverse_bits_byte(bit_array):
    reverse_bits_array = ""
    for i in range(0,len(bit_array),8):
        tmp = bit_array[i:i+8]
        reverse_bits_array += tmp[::-1]
    return reverse_bits_array

def presets_list():
    list = []
    for preset in preset_list:
        list.append(preset)
    return list

def compute_CRC(hexadecimal_input,*args,**kwargs):
    """
    This function computes the CRC of a given hexadecimal string
    :hexadecimal_input: An hexadecimal string representing the data with which the CRC will be computed (length must be an even number)
    :poly: The polynom used for CRC computation (must be a positive integer)
    :init: The init value used for CRC computation (must be a positive integer)
    :final XOR: The value XORed at the end of CRC computation (must be a positive integer)
    :width: CRC width (must be either 8, 16, 32 or 64)
    :refin: If True, bits are inverted in bytes (LSB first). If False bits are left as they are (MSB first)
    :refout: If True, final CRC bits are reversed before final XOR
    :preset: Allows to use predifined parameters for CRC computation (will overwrite poly, init, final XOR and width if written)
    :return: integer
    """

    preset = kwargs.get("preset",None)
    if preset != None:
        if len(args) > 0:
            print("WARNING : Custom parameters will not be used if preset is defined")
        if preset in preset_list:
            poly=preset_list[preset]['poly']
            init=preset_list[preset]['init']
            final_xor=preset_list[preset]['xor']
            width=preset_list[preset]['width']
            refin=preset_list[preset]['refin']
            refout=preset_list[preset]['refout']
        else:
            raise _CRCParameterError(preset,"Preset doesn't exist")
    else:
        if len(args) != 6:
            raise _CRCParameterError(args,"Parameter is missing (polynom, init, final XOR, width)")
        else:
            poly=args[0]
            init=args[1]
            final_xor=args[2]
            width=args[3]
            refin=args[4]
            refout=args[5]
        
    if not isinstance(width, int):
        raise _CRCwidthError(str(width),"width isn't an integer")
    if width not in [8,16,32,64]:
        raise _CRCwidthError(str(width),"width isn't managed")
        
    # Convert input into bit array
    _check_HEX_input(hexadecimal_input)
    bit_array = _hex_2_bit_array(hexadecimal_input.strip())
    if refin == True:
        bit_array = inverse_bits_byte(bit_array)

    # Compare parameter size with width
    if (len(hex(init)[2:])*4) > width:
        raise _CRCParameterError(str(init),"Init size is not compliant with CRC width")
    if (len(hex(poly)[2:])*4) > width:
        raise _CRCParameterError(str(poly),"Polynom size is not compliant with CRC width")
    if (len(hex(final_xor)[2:])*4) > width:
        raise _CRCParameterError(str(final_xor),"Final XOR size is not compliant with CRC width")

    # Convert init to bits
    try:
        init_bits = _hex_2_bit_array(hex(init)[2:].zfill(width//4))
    except:
        raise _CRCParameterError(str(init),"Init isn't a valid number (must be a positive integer)") from None
    # Convert polynom to bits
    try:
        poly_bits = _hex_2_bit_array(hex(poly)[2:].zfill(width//4))
    except:
        raise _CRCParameterError(str(poly),"Polynom isn't a valid number (must be a positive integer)") from None
    # Convert XOR to bits
    try:
        final_xor_bits = _hex_2_bit_array(hex(final_xor)[2:].zfill(width//4))
    except:
        raise _CRCParameterError(str(final_xor),"Final XOR isn't a valid number (must be a positive integer)") from None

    # Convert hex input to bits and pad 0s at the end
    bit_array =  bit_array + '0'*width
    bit_array = _xor_bin(init_bits,bit_array[:len(init_bits)]) + bit_array[len(init_bits):]

    # Compute CRC
    for i in range(0,len(bit_array)-width):
        if(bit_array[0]=='1'):
            bit_array = bit_array[1:]+'0'
            bit_array = _xor_bin(poly_bits,bit_array[:len(poly_bits)]) + bit_array[len(poly_bits):]
        else:
            bit_array = bit_array[1:]+'0'
    bit_array = bit_array[:width]
    if refout == True:
        bit_array = bit_array[::-1]
    final_CRC = _xor_bin(bit_array,final_xor_bits)
    return int(final_CRC,2)
    
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
        
class _CRCwidthError(_CRCError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message