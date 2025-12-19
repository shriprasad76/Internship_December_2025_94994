function changetext() {
    document.getElementById("msg").innerText = "This text change";
}

function changecolor() {
    document.getElementById("msg").style.color = "green";
}

function showtext() {
    const name = document.getElementById("name").value;
    document.getElementById("title").innerText = "Hello " + name + " welcome to dom demo";
}
