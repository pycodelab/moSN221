class Student {
    constructor(firstName, lastName)
    {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    getFullName()
    {
        return this.firstName+' '+this.lastName;
    }
}

let john = new Student('John','Doe')
console.log(john.getFullName())
let Mohamed = new Student('Mohamed','Diaw')
console.log(Mohamed.getFullName())