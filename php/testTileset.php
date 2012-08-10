<?php

require_once('./binaryio.php');
require_once('./formats/tileset.php');
require_once('./renderers/tilesetRenderer.php');

Tileset::$tilePath = '../testFiles/tiles/';
$tileset = Tileset::load('RPGMaker951.tst');

$renderer = new TilesetRenderer($tileset);

#header('Content-Type: text/plain');
header('Content-Type: image/jpeg');
print $renderer->render('jpeg');