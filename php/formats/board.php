<?php

class Board
{
	public static $boardPath = './';

	public static function load($boardFile)
	{
		$file = new BinaryIO(self::$boardPath . $boardFile);

		$board = array();
		$board['filename'] = $boardfile;
		$board['header'] = $file->readString();
		$board['version_major'] = $file->readInt();
		$board['version_minor'] = $file->readInt();
		$board['version'] = $board['version_major'] . '.' . $board['version_minor'];
		
		if($board['version_major'] != 2)
		{
			throw new Exception('Cannot handle board file versions other than 2.4.');
		}

		if($board['version_minor'] < 4)
		{
			throw new Exception('Cannot handle board file versions other than 2.4.');
		}

		$board['width'] = $file->readInt();
		$board['height'] = $file->readInt();
		$board['layers'] = $file->readInt();
		$board['coordinateType'] = $file->readInt();
		$board['tilesetCount'] = $file->readInt();
		$board['tilesets'] = array();

		# Load all of the references to tiles within tilesets used by this board:
		for($i = 0; $i < $board['tilesetCount']; $i++)
		{
			$board['tilesets'][] = $file->readString();
		}

		# I have no idea why (yet), but I always have to load an extra 30 bytes
		# from the file in order to find the beginning of the tile data
		for($i = 0; $i < 10; $i++)
		{
			$file->readInt();
		}

		# Load the tile data from the file:
		$board['tileData'] = array();
		$layer = 0;
		$skipTiles = 0;
		$index = 0;
		while($layer < $board['layers'])
		{
			$y = 0;
			$thisLayer = array();

			while($y <= $board['height'])
			{
				$x = 0;
				$thisY = array();

				while($x <= $board['width'])
				{
					# Handle compression:
					if($skipTiles > 0)
					{
						$skipTiles -= 1;
						$thisY[] = $index;
					}
					else
					{
						$index = $file->readInt();

						if($index < 0)
						{
							# If the index is less than zero, the next
							# N tiles are the same. 
							$skipTiles = (-$index) -1;

							# so we read the next index to get the tile
							# and then use that for skipTiles tiles
							$index = $file->readInt();
							$thisY[] = $index;
						}
						else
						{
							$thisY[] = $index;
						}
					}

					$x += 1;
				}

				$y += 1;
				$thisLayer[] = $thisY;
			}

			$layer += 1;
			$board['tileData'][] = $thisLayer;
		}

		# !!! Returning the board here, as the rest of the file format is not
		#		properly supported yet.
		return $board;
	}
}