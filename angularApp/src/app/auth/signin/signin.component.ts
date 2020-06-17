import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
import { User } from 'src/app/models/User.models';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.scss']
})
export class SigninComponent implements OnInit {

  signinForm: FormGroup;
  errorMessage: string;


  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private apiService: ApiService,
    private router: Router) { }

  ngOnInit(): void {
    this.initForm();
  }

  initForm() {
    this.signinForm = this.formBuilder.group({
      login : ['o2177545', [Validators.required]],
      pwd : ['test', [Validators.required]]
    });
  }

  onSubmit() {
    const login = this.signinForm.get('login').value;
    const pwd = this.signinForm.get('pwd').value;

    console.log('login...');

    this.apiService.login(login, pwd).subscribe(
      (res) => {

        console.log(res);

        console.log('login ok..');

        this.authService.setToken(res.token);
        this.authService.isAuth = true;
        this.authService.emitIsAuth();
        this.authService.connected_user = res.user_id;
        this.router.navigate(['/']);

      }, (error) => {
        this.errorMessage = error.error;
      }
    );




  }

}
