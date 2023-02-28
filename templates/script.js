function dlgOK(){
    var whitebg = document.getElementById("white-background");
    var dlg = document.getElementById("dlgbox");
    whitebg.style.display = "none";
    dlg.style.display = "none";
}

function showDialog(){
    var whitebg = document.getElementById("white-background");
    var dlg = document.getElementById("dlgbox");
    whitebg.style.display = "block";
    dlg.style.display = "block";
    
    var winWidth = window.innerWidth;
    var winHeight = window.innerHeight;
    
    dlg.style.left = (winWidth/2) - 480/2 + "px";
    dlg.style.top = "150px";
}