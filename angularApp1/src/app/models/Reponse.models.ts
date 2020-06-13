export class Reponse {
    constructor(
        public id: number,
        public FK_Question_id: number,
        public FK_Utilisateur_id : number,
        public reponse: string,
        public FK_Questionnaire_id: number
    ) {
    }
}
