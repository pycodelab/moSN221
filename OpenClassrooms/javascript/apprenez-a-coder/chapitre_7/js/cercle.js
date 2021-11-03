var r = Number(prompt("Entrez le rayon d'un cercle :"));

var cercle = {
    rayon : r,
    perimetre: function () {
        var perim = 2*Math.PI*this.rayon;
        return perim;
    },
    aire: function () {
        var surface = Math.PI*this.rayon**2;
        return surface;
    }
};

console.log("Son périmètre vaut " + cercle.perimetre());
console.log("Son aire vaut "+ cercle.aire());