import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';
import { Questionnaire } from 'src/app/models/Questionnaire.models';
import { Question } from 'src/app/models/Question.models';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-questionnaire2',
  templateUrl: './questionnaire2.component.html',
  styleUrls: ['./questionnaire2.component.scss']
})
export class Questionnaire2Component implements OnInit {

  id: number;

  questionnaire: any;

  formQuestionnaire: FormGroup;

  message: string;
  sending= false ;

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService,
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router : Router
    ) { }

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];

    this.apiService.getQuestionnaireByID(this.id).subscribe(
      (res : any) => {
        this.questionnaire = res;
        this.initForm();
      }
    );
   
  }

  


  initForm(){

    const form_group = {};

    this.questionnaire.question_value.forEach(q  => {
      
      if (q.list_reponse.length == 0){
        form_group[q.id] = [''];
      }else{
        q.list_reponse.forEach(
          r => {
            if (r.id){
              form_group[q.id +''+ r.id] = [false]
              
            }
          }
        );
      }
        
      
    });
    this.formQuestionnaire = this.formBuilder.group(form_group);


  }

  


  onSubmit(){
    console.log('sending response...');
    this.sending = true ;

    var reps = [];
    
    this.questionnaire.question_value.forEach(q  => {
      
      if (q.list_reponse.length === 0){
        reps.push(
          {
            "FK_Utilisateur": this.authService.connected_user,
            "FK_Questionnaire": this.questionnaire.id,
            "FK_Question": q.id,
            "reponse": this.formQuestionnaire.get(q.id+'').value
            }
        );
        
        
      }else{
        q.list_reponse.forEach(
          r => {
            if (r.id){
              if( this.formQuestionnaire.get(q.id+''+r.id).value){
                reps.push(
                  {
                    "FK_Utilisateur": this.authService.connected_user,
                    "FK_Questionnaire": this.questionnaire.id,
                    "FK_Question": q.id,
                    "reponse": r.reponse
                    }
                );
                
              }
              
            }
          }
        );
      }
        
      
    });


    console.log(reps);

    this.apiService.save_rep(reps).subscribe(
      (res) => {
        this.router.navigate(['/recap',this.id]);
        

      }, (error) => {
        this.message = "Envoie échoué";
        this.sending = false;

      }
      
    );
    
    
   

  }


  

}
