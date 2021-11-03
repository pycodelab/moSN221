let numberOfSeasons = 6;
let numberOfEpisodes = 12;
console.log (numberOfEpisodes);
console.log(numberOfSeasons);

let episodeTime = 45;
let commercialTime = 5;

let totalShowTime = (numberOfEpisodes*numberOfSeasons)*(episodeTime+commercialTime);
console.log(totalShowTime);

/* const hourPerDay = 24;
const minPerHour = 60;
const secondperMinute = 60;

let secondsPerDay = hourPerDay*minPerHour*secondperMinute;
console.log("Une journée comporte " + secondsPerDay + " secondes.") */

/*let episodeTitle = "Damay delu Waalo";
let episodeDuration = 60;
let hasBeenWatched = true;*/

/*console.log ("J'ai déjà regardé "+episodeTitle+". L'épisode dure "+episodeDuration+" mn.");*/

/*let episode = {
    title : "Damay Delu Waalo",
    duration : 60,
    hasBeenWatched : false,
    };

let episodeTitle = episode.title;
let episodeDuration = episode.duration;
let episodeHasBeenWatched = episode.hasBeenWatched;*/

class Episode {
    constructor(title, duration, hasBeenWatched) {
        this.title = title;
        this.duration = duration;
        this.hasBeenWatched = hasBeenWatched;
    }
}

let firstEpisode = new Episode("Saa Nekh",120,true);
let secondEpisode = new Episode("Mbaye Bercy", 220, false);
let thirdEpisode = new Episode("Desperate Housewives", 45, true);
let prologue = new Episode("prologue", 10, true);

console.log(firstEpisode);

/*let series = [firstEpisode,secondEpisode,thirdEpisode];*/
let series = [];

series.push(firstEpisode);
series.push(secondEpisode);
series.push(thirdEpisode);
series.push(thirdEpisode);
series.pop();
nombreEpisodes=series.length;

series.unshift(prologue);
series.pop(thirdEpisode);
console.log(series);


