var nombre=Number(prompt("entrez un nombre"))
if (nombre>=0) {
for (i=1;i<=nombre;i++) {
    if (i%2===0) {
        console.log(i+ " est pair.")
    }
    else {
        console.log(i+ " est impair")
    }
}
}
else {
    for (i=nombre;(i>=nombre && i<=0);i++)
       if (i%2===0) {
        console.log(i+ " est pair.")
    }
    else {
        console.log(i+ " est impair")
    }  
}