# Universal CRC

The goal of this project is to provide a simple and universal CRC computation tool, allowing the user to freely choose any of the parameters.

## Installation

Install universalCRC

    $ pip install universal-crc

## Usage

To use custom parameters :

	from universalCRC import crc
	CRC = crc.compute_CRC("111213141516171819",0x07,0x00,0x00,8,False,False)

To use predefined parameters :

	from universalCRC import crc
	CRC = crc.compute_CRC("111213141516171819",preset = "DARC")