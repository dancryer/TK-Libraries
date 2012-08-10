<?php

class Tileset
{
	public static $tilePath = './';

	public static function load($tilesetFile)
	{
		$file = new BinaryIO(self::$tilePath . $tilesetFile);

		$thisTileset = array();
		$thisTileset['filename'] = $tilesetFile;
		$thisTileset['version'] = $file->readInt();
		$thisTileset['count'] = $file->readInt();
		$thisTileset['detail'] = $file->readInt();

		if($thisTileset['detail'] != 1)
		{
			throw new Exception('Cannot read tilesets with a detail level other than 1.');
		}

		$thisTileset['tiles'] = array();

		for($i = 0; $i < $thisTileset['count']; $i++)
		{
			$thisTile = array();

			for($x = 0; $x < 32; $x++)
			{
				$thisX = array();

				for($y = 0; $y < 32; $y++)
				{
					$r = $file->readUnsignedByte();
					$g = $file->readUnsignedByte();
					$b = $file->readUnsignedByte();

					$thisX[] = array($r, $g, $b);
					unset($r, $g, $b);
				}

				$thisTile[] = $thisX;
				unset($thisX);
			}

			$thisTileset['tiles'][] = $thisTile;
			unset($thisTile);
		}

		return $thisTileset;
	}
}