class Episode {
    constructor(title, duration, minutesWatched) {
        this.title = title;
        this.duration = duration;
        
        if (minutesWatched==this.duration) {
            this.hasBeenWatched = true;
        }
        else if (minutesWatched<=this.duration){
            this.hasBeenWatched = false;
        }
        
    }
}

let firstEpisode = new Episode ("Saa nekh", 85, 85);
let secondEpisode = new Episode ("Mbaye Bercy", 185, 85);
let thirdEpisode = new Episode ("Lamb dji", 85, 0);
let fourthEpisode = new Episode ("Askanou Laobé", 85, 2);
/*if (firstEpisode.hasBeenWatched) {
    console.log("Film déjà regardé");
}
else {
    console.log("Film pas encore regardé");
} */

/*class Episode {
    constructor(title,duration,minutesWatched) {
        this.title = title;
        this.duration = duration;
        this.continueWatching = false;
        if (minutesWatched < duration && minutesWatched>0) {
            this.watchedText = "En train de regarder";
            this.continueWatching = true;
        }
        if (minutesWatched == duration) {
            this.watchedText = "déjà regardé";
        }
        if (minutesWatched == 0) {
            this.watchedText = "Pas encore regardé";
        }
       else if (duration <=0 || minutesWatched<0) {
            this.watchedText = "erreur de saisie";
        }
        

}

}
episode1 = new Episode ("Saa Nekh",-85,-85);
console.log(episode1);
console.log(episode1.watchedText);
console.log(episode1.continueWatching);*/

let saga = [firstEpisode,secondEpisode,thirdEpisode,fourthEpisode];
/*for (i = 0; i<saga.length; i++) {
    saga[i].hasBeenWatched = false;
    console.log(saga[i].hasBeenWatched);
}*/

for (let i in saga) {
    saga[i].hasBeenWatched = false;
    console.log (saga[i].hasBeenWatched);
}

for (let i of saga) {
    i.hasBeenWatched = true;
    console.log(i.hasBeenWatched);
}


