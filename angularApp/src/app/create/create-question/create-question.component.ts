import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, Validators, FormArray, FormGroup } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-create-question',
  templateUrl: './create-question.component.html',
  styleUrls: ['./create-question.component.scss']
})
export class CreateQuestionComponent implements OnInit {

  id_questionnaire: number;
  questionForm : FormGroup;

  constructor(
    private route: ActivatedRoute,
    private formBuilder: FormBuilder,
    private apiService: ApiService,
    private router: Router
    
    ) { }

  ngOnInit(): void {
    this.id_questionnaire = this.route.snapshot.params['id'];
    this.initForm();
  }

  initForm(){

    this.questionForm = this.formBuilder.group({
      libelle : ['', [Validators.required]],
      reponses : this.formBuilder.array([]),
      bonneReponses : this.formBuilder.array([])

    });

    this.onAddReponse();

  }
  onSubmit(){

    const libelle = this.questionForm.get('libelle').value;
    const reps = this.questionForm.value['reponses'];
    const bonneReps =
     this.questionForm.value['bonneReponses'] ? this.questionForm.value['bonneReponses'] : [];

    
    

    const list_question = [{
      "libelle" : libelle,
      "FK_Questionnaire" : this.id_questionnaire,
      "list_reponse" : reps,
      "bonne_reponse" : bonneReps
    }]; 

    

   this.apiService.create_question(list_question).subscribe(
      (res) => { 
        this.router.navigate(['/create','apercu']);
        console.log(res["success"]);
      },
      (error)=> {console.log(error);
      }
    );
    

  }

  getReponses() : FormArray{
    return this.questionForm.get('reponses') as FormArray;
  }

  onAddReponse(){
    const newRepControl = this.formBuilder.control(null,Validators.required);
    this.getReponses().push(newRepControl);
  }

  getBonneReponses() : FormArray{
    return this.questionForm.get('bonneReponses') as FormArray;
  }

  onAddBonneReponse(){
    const newRepControl = this.formBuilder.control(null,Validators.required);
    this.getBonneReponses().push(newRepControl);
  }
  
  

}
