function board(filename){
	this.file = new binaryIO(filename);
	
	this.header = this.file.readString();
	
	this.version = {
		major: this.file.readInt16(),
		minor:  this.file.readInt16()
	};
	
	this.width = this.file.readInt16();
	this.height = this.file.readInt16();
	this.layers = this.file.readInt16();
	
	this.coordinateType = this.file.readInt16();
	
	// adding 1 fixed things - seems the last tile source gets missed (empty string starts source list?)
	this.tilesUsed = this.file.readInt16() + 1;
	
	this.tileSources = [];
	
	// get tile sources
	for(var i=0; i<this.tilesUsed; i++) this.tileSources.push(this.file.readString());
	
	this.tiles = [];
	
	var skipTiles = 0, tileIndex = 0;
	
	// loop through layers
	for(var layer=0; layer < this.layers; layer++){
		currentLayer = [];
		
		// y axis
		for(var y=0; y<this.height; y++){
			currentColumn = [];
			
			// x axis
			for(var x=0; x<this.width; x++){
				
				// if still repeating for X tiles
				if(skipTiles > 0){
					skipTiles -= 1;
					currentColumn.push(tileIndex);	
				}
				else{
					// get tile
					tileIndex = this.file.readInt16();
					
					// if tile is less than -X, means we're repeating the next tile for (-X) -1
					if(tileIndex < 0){
						skipTiles = (-tileIndex) - 1;
						
						// get tile to be repeated
						tileIndex = this.file.readInt16();
					}
					currentColumn.push(tileIndex);
				}
				
			}
			
			currentLayer.push(currentColumn);
		}
		
		this.tiles.push(currentLayer);
	}
}