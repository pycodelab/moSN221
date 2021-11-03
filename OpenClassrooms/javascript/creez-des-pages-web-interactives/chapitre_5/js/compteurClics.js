function clic () {
     document.getElementById("compteurClics").textContent ++;
}

document.getElementById("clic").addEventListener("click", clic);

document.getElementById("desactiver").addEventListener("click", function () {
   // document.getElementById("clic").removeEventListener("click", clic);
    document.getElementById("compteurClics").textContent = 0;
    })