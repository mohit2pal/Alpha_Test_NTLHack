
const button = document.getElementById('btn') 

var uploaded_image

var body

function marks_update() {

    console.log("run")

    var chr = new XMLHttpRequest()
    chr.open('GET', './static/json/marks.json', true)

    chr.onload = function() {
        var mark = JSON.parse(this.responseText)

        console.log(mark['marks'])

        document.getElementById('score').innerHTML = mark['marks']
    }

    chr.send()
}

const image_input = document.querySelector("#image_input");
image_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
    uploaded_image = reader.result;
    document.querySelector("#display_image").style.backgroundImage = `url(${uploaded_image})`;
});
    reader.readAsDataURL(this.files[0]);
});

function api_call(){

    var body2 = JSON.stringify(body)

    var vhr = new XMLHttpRequest();
    vhr.open('POST', '/test', true);

    vhr.setRequestHeader('Content-Type', 'application/json')

    vhr.send(body2)

    const myTimeout = setTimeout(marks_update, 10000)

  }

function toDataUrl(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var reader = new FileReader();
        reader.onloadend = function() {
            callback(reader.result);
        }
        reader.readAsDataURL(xhr.response);
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    xhr.send();
}

function base() {
    var base64 = "base"
        toDataUrl(uploaded_image , function(myBase64) {
        console.log(myBase64); // myBase64 is the base64 string
        base64 = myBase64
    
        console.log('base64=' + base64);
        console.log(typeof base64)
    
        const base64_split = base64.split(",")[1]
        console.log(base64_split)
    
        body = {
            "png": base64_split
        }
    
        console.log(body)
    
        // const myTimeout = setTimeout(api_call, 600)
        api_call()
    
    })}

button.addEventListener('click', upload)

function upload() {

    base()

}
