<?php

class BinaryIO
{
	protected $file = null;
	protected $fileName = null;

	public function __construct($fileName)
	{
		$this->fileName = $fileName;
		$this->file		= fopen($fileName, 'rb');
	}

	public function readString()
	{
		$rtn  = '';
		$byte = fread($this->file, 1);

		while($byte && !feof($this->file))
		{
			$byte = unpack('a', $byte);
			$byte = array_shift($byte);

			if(empty($byte))
			{
				return $rtn;
			}

			$rtn .= $byte;
			$byte = fread($this->file, 1);
		}

		return $rtn;
	}

	public function readByte()
	{
		return array_shift(unpack('c', fread($this->file, 1)));
	}

	public function readUnsignedByte()
	{
		return array_shift(unpack('C', fread($this->file, 1)));
	}

	public function readInt()
	{
		return array_shift(unpack('s', fread($this->file, 2)));
	}

	public function readLong()
	{
		return array_shift(unpack('i*', fread($this->file, 4)));
	}
}