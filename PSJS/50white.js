var doc = app.activeDocument;
var w = doc.width;
var h = doc.height;

doc.selection.selectAll();
doc.selection.copy(true);
doc.selection.deselect();

// var tempDoc = app.documents.add(w, h, 300);
// tempDoc.paste();
// var bg = tempDoc.layers[1];
// bg.remove();
// var visible = tempDoc.layers[0];

doc.paste();

var numWhite = 0;
var totalPx = w*h;

for (y=0; y<h; y+=1) {
    for (x=0; x<w; x+=1) {
        var spot = doc.colorSamplers.add([x,y]);
        var red = spot.color.rgb.red;
        var green = spot.color.rgb.green;
        var blue = spot.color.rgb.blue;
        if (red==255 && green==255 && blue==255) {
            numWhite+=1;
        }
        spot.remove();
    }
}

doc.layers[0].remove();

var percent = numWhite/totalPx;
percent*=100;

alert("How much whitespace? \n \n" + percent + "%");