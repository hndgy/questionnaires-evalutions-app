import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ApiService } from '../services/api.service';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {



  questionnaireForm: FormGroup;

  listeQuestion: [];

  constructor(
    private formBuilder: FormBuilder,
    private apiService: ApiService,
    private authService: AuthService,
    private router: Router
    ) { }

  ngOnInit(): void {

    this.initForm();    
  }

  initForm(){

   
    this.questionnaireForm = this.formBuilder.group(
      {
         libelle : ['', [Validators.required]]
    }
      );
   
  }

  onSubmit(){

    console.log("submiting new questionnaire...");
    
    const lib = this.questionnaireForm.get('libelle').value ;

   this.apiService.create_questionnaire(lib,this.authService.connected_user).subscribe(

      
      (res) => {
        console.log("ok.");
        
        
        
        this.router.navigate(['/']);
        
      }
    );
  }

}
