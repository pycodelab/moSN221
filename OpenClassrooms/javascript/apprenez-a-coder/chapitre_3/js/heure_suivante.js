var heure = Number(prompt("entrez l'heure qu'il fait"));
var minute = Number(prompt("entrez le nombre de minutes"));
var seconde = Number(prompt("entrez le nombre de secondes"));
if (seconde<0 || minute<0 || heure<0 || seconde>59 || minute>59 || heure>23) {
    console.log("erreur de saisie");
}
else{
    if (seconde<58 && minute<58 && heure<22) {
    heure;
    minute;
    seconde++;
    console.log("il est "+heure+" h "+minute+" mn "+ seconde+" s ");
    }
    if (seconde===59 || minute===59 || heure===23) {
        if (seconde===59 && minute===59 && heure===23) {
        seconde=0;
        minute=0;
        heure=0;
        console.log("il est "+heure+" h "+minute+" mn "+ seconde+" s ");
    }
        if (seconde===59 && minute===59) {
            minute=0;
            seconde=0;
            heure++;
            console.log("il est "+heure+" h "+minute+" mn "+ seconde+" s ");
        }
        if (seconde===59 && heure===23) {
            seconde=0;
            heure=0;
            minute++;
            console.log("il est "+heure+" h "+minute+" mn "+ seconde+" s ");
        }
        if (seconde===59) {
            seconde=0;
            minute++;
            console.log("il est "+heure+" h "+minute+" mn "+ seconde+" s ");
        }
        if (minute===59 || heure===23 || (minute===59 && heure===23)) {
            seconde++;
            console.log("il est "+heure+" h "+minute+" mn "+ seconde+" s ");
        }
        }
    }
