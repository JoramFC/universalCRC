_preset_list = {
    'CDMA2000' : {'poly': 0x9B,'init': 0xFF,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'DARC' : {'poly': 0x39,'init': 0x00,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'EBU' : {'poly': 0x1D,'init': 0xFF,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'AUTOSAR' : {'poly': 0x2f,'init': 0xff,'xor': 0xff,'width': 8,'refin': False,'refout': False},
    'BLUETOOTH' : {'poly': 0xa7,'init': 0x00,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'CDMA2000' : {'poly': 0x9b,'init': 0xff,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'DVB-S2' : {'poly': 0xd5,'init': 0x00,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'GSM-A' : {'poly': 0x1d,'init': 0x00,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'GSM-B' : {'poly': 0x49,'init': 0x00,'xor': 0xff,'width': 8,'refin': False,'refout': False},
    'I-432-1' : {'poly': 0x07,'init': 0x00,'xor': 0x55,'width': 8,'refin': False,'refout': False},
    'I-CODE' : {'poly': 0x1d,'init': 0xfd,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'LTE' : {'poly': 0x9b,'init': 0x00,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'MAXIM-DOW' : {'poly': 0x31,'init': 0x00,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'MIFARE-MAD' : {'poly': 0x1d,'init': 0xc7,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'CRC8-NRSC-5' : {'poly': 0x31,'init': 0xff,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'OPENSAFETY' : {'poly': 0x2f,'init': 0x00,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'ROHC' : {'poly': 0x07,'init': 0xff,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'SAE-J1850' : {'poly': 0x1d,'init': 0xff,'xor': 0xff,'width': 8,'refin': False,'refout': False},
    'SMBUS' : {'poly': 0x07,'init': 0x00,'xor': 0x00,'width': 8,'refin': False,'refout': False},
    'TECH-3250' : {'poly': 0x1d,'init': 0xff,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'WCDMA' : {'poly': 0x9b,'init': 0x00,'xor': 0x00,'width': 8,'refin': True,'refout': True},
    'ARC' : {'poly': 0x8005,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'CDMA2000' : {'poly': 0xc867,'init': 0xffff,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'CMS' : {'poly': 0x8005,'init': 0xffff,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'DDS-110' : {'poly': 0x8005,'init': 0x800d,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'DECT-R' : {'poly': 0x0589,'init': 0x0000,'xor': 0x0001,'width': 16,'refin': False,'refout': False},
    'DECT-X' : {'poly': 0x0589,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'DNP' : {'poly': 0x3d65,'init': 0x0000,'xor': 0xffff,'width': 16,'refin': True,'refout': True},
    'EN-13757' : {'poly': 0x3d65,'init': 0x0000,'xor': 0xffff,'width': 16,'refin': False,'refout': False},
    'GENIBUS' : {'poly': 0x1021,'init': 0xffff,'xor': 0xffff,'width': 16,'refin': False,'refout': False},
    'GSM' : {'poly': 0x1021,'init': 0x0000,'xor': 0xffff,'width': 16,'refin': False,'refout': False},
    'IBM-3740' : {'poly': 0x1021,'init': 0xffff,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'IBM-SDLC' : {'poly': 0x1021,'init': 0xffff,'xor': 0xffff,'width': 16,'refin': True,'refout': True},
    'ISO-IEC-14443-3-A' : {'poly': 0x1021,'init': 0xc6c6,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'KERMIT' : {'poly': 0x1021,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'LJ1200' : {'poly': 0x6f63,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'MAXIM-DOW' : {'poly': 0x8005,'init': 0x0000,'xor': 0xffff,'width': 16,'refin': True,'refout': True},
    'MCRF4XX' : {'poly': 0x1021,'init': 0xffff,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'MODBUS' : {'poly': 0x8005,'init': 0xffff,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'CRC16-NRSC-5' : {'poly': 0x080b,'init': 0xffff,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'OPENSAFETY-A' : {'poly': 0x5935,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'OPENSAFETY-B' : {'poly': 0x755b,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'PROFIBUS' : {'poly': 0x1dcf,'init': 0xffff,'xor': 0xffff,'width': 16,'refin': False,'refout': False},
    'RIELLO' : {'poly': 0x1021,'init': 0xb2aa,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'SPI-FUJITSU' : {'poly': 0x1021,'init': 0x1d0f,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'T10-DIF' : {'poly': 0x8bb7,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'TELEDISK' : {'poly': 0xa097,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'TMS37157' : {'poly': 0x1021,'init': 0x89ec,'xor': 0x0000,'width': 16,'refin': True,'refout': True},
    'UMTS' : {'poly': 0x8005,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'USB' : {'poly': 0x8005,'init': 0xffff,'xor': 0xffff,'width': 16,'refin': True,'refout': True},
    'XMODEM' : {'poly': 0x1021,'init': 0x0000,'xor': 0x0000,'width': 16,'refin': False,'refout': False},
    'AIXM' : {'poly': 0x814141ab,'init': 0x00000000,'xor': 0x00000000,'width': 32,'refin': False,'refout': False},
    'AUTOSAR' : {'poly': 0xf4acfb13,'init': 0xffffffff,'xor': 0xffffffff,'width': 32,'refin': True,'refout': True},
    'BASE91-D' : {'poly': 0xa833982b,'init': 0xffffffff,'xor': 0xffffffff,'width': 32,'refin': True,'refout': True},
    'BZIP2' : {'poly': 0x04c11db7,'init': 0xffffffff,'xor': 0xffffffff,'width': 32,'refin': False,'refout': False},
    'CD-ROM-EDC' : {'poly': 0x8001801b,'init': 0x00000000,'xor': 0x00000000,'width': 32,'refin': True,'refout': True},
    'CKSUM' : {'poly': 0x04c11db7,'init': 0x00000000,'xor': 0xffffffff,'width': 32,'refin': False,'refout': False},
    'ISCSI' : {'poly': 0x1edc6f41,'init': 0xffffffff,'xor': 0xffffffff,'width': 32,'refin': True,'refout': True},
    'ISO-HDLC' : {'poly': 0x04c11db7,'init': 0xffffffff,'xor': 0xffffffff,'width': 32,'refin': True,'refout': True},
    'JAMCRC' : {'poly': 0x04c11db7,'init': 0xffffffff,'xor': 0x00000000,'width': 32,'refin': True,'refout': True},
    'MPEG-2' : {'poly': 0x04c11db7,'init': 0xffffffff,'xor': 0x00000000,'width': 32,'refin': False,'refout': False},
    'XFER' : {'poly': 0x000000af,'init': 0x00000000,'xor': 0x00000000,'width': 32,'refin': False,'refout': False},
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

def _inverse_bits_byte(bit_array):
    reverse_bits_array = ""
    for i in range(0,len(bit_array),8):
        tmp = bit_array[i:i+8]
        reverse_bits_array += tmp[::-1]
    return reverse_bits_array

def presets_list():
    """
    This function returns the list of all the presets available for CRC computation
    :return: List of string containing the names of the presets
    """
    list = []
    for preset in _preset_list:
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
        if preset in _preset_list:
            poly=_preset_list[preset]['poly']
            init=_preset_list[preset]['init']
            final_xor=_preset_list[preset]['xor']
            width=_preset_list[preset]['width']
            refin=_preset_list[preset]['refin']
            refout=_preset_list[preset]['refout']
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
        bit_array = _inverse_bits_byte(bit_array)

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