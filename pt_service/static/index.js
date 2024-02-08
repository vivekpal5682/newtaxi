
function show() {
 var blur = document.getElementById('mainForm');
 blur.style.display="block";
}
function cancel() {
 var blur = document.getElementById('mainForm');
 blur.style.display="none";
}

var right=document.getElementById("navLinks")
function showmenu(){
    navLinks.style.display= "block"
}
function hidemenu(){
    navLinks.style.display= "none"
}
function mousefolow() {
    window.addEventListener("mousemove", function (dets) {
        document.querySelector("#circle").style.transform = `translate(${dets.clientX}px , ${dets.clientY}px)`
    })
}
//mousefolow()

$(window).scroll(function() { // when the page is scrolled run this
    if($(this).scrollTop() > 200) { // if you're NOT at the top
        $('#arrow').fadeIn("fast"); // fade in
    } else { // else
        $('#arrow').fadeOut("fast"); // fade out
    }
});

$('#arrow').click(function() { // when the button is clicked
    $('body,html').animate({scrollTop:0},500); // return to the top with a nice animation
});


document.getElementById("myForm").addEventListener("submit", function (event) {
    // Prevent the form from submitting normally
    // event.preventDefault();

    // Show the popup
    document.getElementById("pop").style.visibility = "visible";
});

function closePopup() {
    // Close the popup
    document.getElementById("pop").style.visibility = "hidden";
}