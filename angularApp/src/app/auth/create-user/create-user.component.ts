import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, AbstractControl } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-create-user',
  templateUrl: './create-user.component.html',
  styleUrls: ['./create-user.component.scss']
})
export class CreateUserComponent implements OnInit {


  createUserForm : FormGroup;
  errorMessage : string;

  role = ['etudiant', 'professeur'];

  constructor( 
    private formbuilder : FormBuilder, 
    private router : Router,
    private apiService : ApiService,
    private authService: AuthService) { }

  ngOnInit(): void {
    this.initForm();
  }

  initForm(){
    this.createUserForm = this.formbuilder.group(
      {
        nom : ['', [Validators.required]],
        prenom : ['', [Validators.required]],
        numero : ['', [Validators.required]],
        role : ['', [Validators.required]],
        password : ['', [Validators.required]],
        password2 : ['', [Validators.required]],
        
    },{validator: this.passwordConfirming}
    );


  }

  passwordConfirming(c : AbstractControl){
    if (c.get('password').value !== c.get('password2').value) {
      return {invalid: true};
  }
  }

  onSubmit(){
    const nomVal = this.createUserForm.get('nom').value;
    const prenomVal = this.createUserForm.get('prenom').value;
    const numVal = this.createUserForm.get('numero').value;
    const roleVal = this.createUserForm.get('role').value;
    const pwdVal = this.createUserForm.get('password').value;

    
    
 
    this.apiService.create_user(nomVal,prenomVal,numVal,roleVal, pwdVal).subscribe(
      (res) => {
        this.apiService.setToken(res['token']);
        this.authService.connected_user = res['id'];
        this.authService.isAuth = true;
        this.authService.emitIsAuth();
        this.router.navigate(['/']); 


      }, (error) => {
        this.errorMessage = error;

      }
    );


  


  }

}
