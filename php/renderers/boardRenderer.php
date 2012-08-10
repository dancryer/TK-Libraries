<?php

class BoardRenderer
{
	protected $board = null;

	public function __construct($board)
	{
		$this->board = $board;
	}

	public function render($format = 'png')
	{
		$b = $this->board;
		$imageX = $b['width'] * 32;
		$imageY = $b['height'] * 32;

		$im = imagecreatetruecolor($imageX, $imageY);
		imagefill($im, 0, 0, imagecolorallocate($im, 0, 0, 0));

		$tilesets = array();

		$x = 0;
		$y = 0;

		foreach($b['tileData'] as $layer)
		{
			foreach($layer as $yData)
			{
				foreach($yData as $tile)
				{
					if($tile > 0 && $tile < count($b['tilesets']) && $b['tilesets'][$tile] != '')
					{
						$data = $this->getTileData($b['tilesets'][$tile]);

						if($data)
						{
							if(!isset($tilesets[$data['file']]))
							{
								$tilesets[$data['file']] = Tileset::load($data['file']);

								
							}

							$renderer = new TilesetRenderer($tilesets[$data['file']]);

							$renderer->renderTile($im, $data['tile'] - 1, $x * 32, $y * 32);
						}
					}

					$x++;
				}

				$y++;
				$x = 0;
			}

			$y = 0;
			$x = 0;
		}

		ob_start();
		switch($format)
		{
			case 'jpg':
			case 'jpeg':
				imagejpeg($im);
			break;

			case 'gif':
				imagegif($im);
			break;

			case 'png':
			default:
				imagepng($im);
			break;
		}

		$image = ob_get_contents();
		ob_end_clean();

		return $image;
	}

	public function getTileData($tile)
	{
		$idx = strpos($tile, '.tst');

		if($idx === false)
		{
			return false;
		}

		$idx += 4;

		return array('file' => substr($tile, 0, $idx), 'tile' => substr($tile, $idx));
	}
}