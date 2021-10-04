var valeurs = [11,3,7,2,9,10];

var max = valeurs[0];
for (i=1;i<valeurs.length;i++) {
    if (valeurs[i]>max) {
       max = valeurs[i];
    }
    else {
        max = max;
    }
};

console.log("Le maximum est égal à "+max);