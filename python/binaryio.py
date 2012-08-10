# coding=UTF-8
import struct

# Read string data from a binary file, stopping at the first null byte:
def readString(f):
	rtn = ''
	byte = f.read(1)
	while byte:
		unpacked = struct.unpack('B', byte)[0]

		if unpacked is 0:
			return rtn

		rtn = rtn + byte
		byte = f.read(1)

# Read a one byte int from the file:
def readByte(f):
	return struct.unpack('b', f.read(1))[0]

# Read a one byte unsigned int from the file:
def readUnsignedByte(f):
	return struct.unpack('B', f.read(1))[0]

# Read a two byte (short) int from the file:
def readInt(f):
	return struct.unpack('<h', f.read(2))[0]

# Read a four byte int from the file:
def readLong(f):
	return struct.unpack('<i', f.read(4))[0]