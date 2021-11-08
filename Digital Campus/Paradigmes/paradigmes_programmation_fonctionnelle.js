// Factorielle d'un nombre en programmation impérative
function factorielle_imperative(nombre)
{
    let produit = 1
    for (let i= 1;i<=nombre;i++){
        produit *=i;
    }
    return produit
}
// Factorielle d'un nombre en programmation fonctionnelle
function factorielle_fonctionnelle(nombre)
{
    if (nombre == 0) {
        return 1;
    }

    return nombre * factorielle_fonctionnelle(nombre -1)
}

console.log(factorielle_imperative(5))
console.log(factorielle_fonctionnelle(5))