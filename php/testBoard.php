<?php

require_once('./binaryio.php');
require_once('./formats/tileset.php');
require_once('./renderers/tilesetRenderer.php');
require_once('./formats/board.php');
require_once('./renderers/boardRenderer.php');

Board::$boardPath  = '../testFiles/boards/';
Tileset::$tilePath = '../testFiles/tiles/';

$board = Board::load('modorodar.brd');
$renderer = new BoardRenderer($board);

#header('Content-Type: text/plain');
header('Content-Type: image/jpeg');
print $renderer->render('jpeg');