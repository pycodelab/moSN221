/* 
Activité : gestion des contacts
*/

// TODO : complétez le programme

var contact = {
    prenom:"",
    nom:""
}
var contacts = [];
var choice;

while(choice != 0){
    console.log("1 : Lister les contacts" );
    console.log("2 : Ajouter un contact");
    console.log("0 : Quitter");
    choice = prompt("Choisissez un option:");

    if(choice == 1){
        for(var i=0;i<contacts.length;i++){
            if(contacts.length != 0)console.log("Nom : "+contacts[i].nom+",prénom : "+contacts[i].prenom);
            else console.log("Hello buddy, y as rien a afficher");
        }
        console.log("");
    }
    if(choice==2){
        var newContact = {
            prenom:"",
            nom:""
        };
        newContact.prenom = prompt("Prénom ?");
        newContact.nom = prompt("Nom ?");
        contacts.push(newContact);
        console.log("");
    }
}