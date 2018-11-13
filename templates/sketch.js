// Definition of global variables
let canvas_input
let clear_
let text_answer
let size_slider

function setup(){
    // Setup Text and Canvas
    text_answer = createElement('h2', 'Answer will be here!');
    text_answer.id('text_display');
    canvas_input = createCanvas(200, 200);
    canvas_input.id('canvas_surface');
    background(200);

    // Create send button
    let button_send = createButton('send');
    button_send.position(130, 270);
    button_send.mousePressed(send_img); // Setting to execute send_img when send button is pressed

    // Create clear button
    button_clear = createButton('clear');
    button_clear.position(40, 270);
    button_clear.mousePressed(clear_canvas); // Setting to execute clear_canvas when clear button is pressed

    // Create size slider
    size_slider = createSlider(0, 40, 20);
    size_slider.position(300, 10);
    size_slider.style('width', '80px');
}

// Draw Black ellipse by pointer position
function draw(){
    if (mouseIsPressed){
        fill(0);                           // Set fill to Black
        var val = size_slider.value();     // Get now ellipse size
        ellipse(mouseX, mouseY, val, val); // Draw Black ellipse using RADIUS mode    
    }
}

// Initialize canvas
function clear_canvas(){
    background(200);
}

// Send img to server with POST method
function send_img(){
    // Get each element by id
    let surface = document.getElementById("canvas_surface");
    let display = document.getElementById("text_display");
    
    // Update text display
    display.innerHTML = ('updating...');

    // Convert surface element into DataURL
    var dataURL = surface.toDataURL("image/jpeg", 1.0);
    console.log(dataURL);

    // Make json type data
    let postData = {imgURI: dataURL};
    let url = '/demotext';

    // Send post data to '/demotext' with json
    httpPost(url, 'json', postData,
	     function(result){
		 tt.innerHTML = ('answer is:' + result);
	     }
	    );
}
