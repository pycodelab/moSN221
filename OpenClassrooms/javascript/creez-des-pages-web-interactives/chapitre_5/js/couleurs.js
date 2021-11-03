elementParagraph = document.querySelectorAll("div");

/*function coloriage (e) {
    for (i=0; i<elementParagraph.length; i++) {
    switch (String.fromCharCode(e.charCode).toLowerCase) {
            case "r" :
                elementParagraph[i].style.backgroundColor = "red";
                break;
            case "v" :
                elementParagraph[i].style.backgroundColor = "green";
                break;
            case "b" :
                elementParagraph[i].style.backgroundColor = "white";
                break;
            case "j" :
                elementParagraph[i].style.backgroundColor = "jaune";
                break;
            default :
                break;
}
    }
}*/


    
document.addEventListener("keypress", function (e) {
    for (i=0; i<elementParagraph.length; i++) {
    switch ((String.fromCharCode(e.charCode)).toLowerCase()) {
            case "r" :
                elementParagraph[i].style.backgroundColor = "red";
                break;
            case "v" :
                elementParagraph[i].style.backgroundColor = "green";
                break;
            case "b" :
                elementParagraph[i].style.backgroundColor = "white";
                break;
            case "j" :
                elementParagraph[i].style.backgroundColor = "yellow";
                break;
            default :
                break;
}
    }
});

/*document.addEventListener("keypress", function (e) {
    console.log (String.fromCharCode(e.charCode));
})*/