export class Question{


    constructor(
        public id : number ,
        public libelle : string,
        public FK_Questionnaire: number,
        public list_reponse: any[]
    ){}

    
} 