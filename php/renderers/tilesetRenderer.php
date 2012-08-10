<?php

class TilesetRenderer
{
	protected $tileset = null;

	public function __construct($tileset)
	{
		$this->tileset = $tileset;
	}

	public function render($format = 'png')
	{
		$t = $this->tileset;

		$imageX		= 288;
		$imageY		= ($t['count'] / 9) * 32;
		$offsetX	= 0;
		$offsetY	= 0;
		
		$im = imagecreatetruecolor($imageX, $imageY);

		for($i = 0; $i < $t['count']; $i++)
		{
			$this->renderTile($im, $i, $offsetX, $offsetY);

			$offsetX += 32;
			if(($offsetX + 32) > $imageX)
			{
				$offsetX	=  0;
				$offsetY	+= 32;
			}
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

	public function renderTile($im, $tileIndex, $offsetX, $offsetY)
	{
		if(!isset($this->tileset['tiles'][$tileIndex]))
		{
			return;
		}
		
		$tile = $this->tileset['tiles'][$tileIndex];

		$x = 0;
		$y = 0;
		foreach($tile as $xData)
		{
			foreach($xData as $yData)
			{
				$color = imagecolorallocate($im, $yData[0], $yData[1], $yData[2]);
				imagesetpixel($im, $offsetX + $x, $offsetY + $y, $color);

				$y++;
			}

			$x++;
			$y = 0;
		}
	}
}