import { Component, OnInit } from '@angular/core';
import { Questionnaire } from 'src/app/models/Questionnaire.models';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';
import { Question } from 'src/app/models/Question.models';

@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  styleUrls: ['./questionnaire.component.scss']
})
export class QuestionnaireComponent implements OnInit {


  questionnaire : Questionnaire;
  id : number;


  reponses : any[];

  idx_question: number;
  current_id_question : number;
  current_question : Question;
  

  current_text_aera_rep: string;


  constructor(private route: ActivatedRoute,private apiService: ApiService) { }

  ngOnInit(): void {

    this.id = this.route.snapshot.params['id'];

    this.apiService.getQuestionnaireByID(this.id).subscribe(
      (res : any) => {
        this.questionnaire = res;
        this.initReponses();
      }
    );
  
  
  
  }

initReponses(){
  
}

get_rep(id_rep){
  this.apiService.getReponse(id_rep).subscribe(
    (rep) => {
      return rep['reponse'];
    }
  );
}





get_current_question(){
   this.apiService.getQuestionByID(this.current_id_question).subscribe(
    (res : any) => {
      this.current_question = res;
    }
  ); 


}
  
  

  // passe à la question suivante
  next(){
    this.idx_question++;
    this.current_id_question = this.questionnaire.question[this.idx_question];  

    if (this.idx_question < this.questionnaire.question.length){ // questionnaire en cours
        this.get_current_question();
    }else{
      this.current_id_question = null;
    }
  
  }

  // revient à la question précédente
  previous(){
    this.idx_question--;
    this.current_id_question = this.questionnaire.question[this.idx_question]; 
    this.get_current_question();

  }
  onCommencer(){
    this.idx_question = 0;
    this.current_id_question = this.questionnaire.question[this.idx_question];    
    this.get_current_question();
  }

  onChangeTextAera(val){
    this.reponses[this.idx_question].rep[0] = [val];

  }

  getValueTxtAera(){
    
    return this.reponses[this.idx_question].rep[0] == undefined ? '' : this.reponses[this.idx_question].rep[0];
  }

  onChangeCheck(index_of_cbox, val){ 

    if (this.reponses[this.idx_question].rep[index_of_cbox] === false ){ // si c'etait pas coché
        //on met la valeur à la place de false 
        this.reponses[this.idx_question].rep[index_of_cbox] = val;
    }else {
      this.reponses[this.idx_question].rep[index_of_cbox] = false ; // sinon on décoche 
    }
      

  }

  isChecked(index_of_cbox){
    return this.reponses[this.idx_question].rep[index_of_cbox] !== false ;
    // si c'est pas coché c'est false sinon c'est la val de la reponse et on renvoit true.
    
  }



}
