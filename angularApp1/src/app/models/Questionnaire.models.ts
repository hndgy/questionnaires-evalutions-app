import { Question } from './Question.models';

export class Questionnaire{
    constructor(

        public id : number,
        public libelle: string,
        public prof: number,
        public listRepondant: any[],
        public question: any[]
    ){

    }
}