import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';

import { QuestionnaireComponent } from './question/questionnaire/questionnaire.component';
import { HttpClientModule } from '@angular/common/http'
import { ApiService } from './services/api.service';

import { Routes, RouterModule } from '@angular/router';
import { QuestionSingleComponent } from './question/question-single/question-single.component';
import { SigninComponent } from './auth/signin/signin.component';
import { AuthGuardService } from './services/auth-guard.service';
import { AuthService } from './services/auth.service';

import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { CreateComponent } from './create/create.component';
import { Questionnaire2Component } from './question/questionnaire2/questionnaire2.component';
import { CreateUserComponent } from './auth/create-user/create-user.component';
import { UserComponent } from './user/user.component';
import { RecapitulatifComponent } from './recapitulatif/recapitulatif.component';
import { CreateQuestionComponent } from './create/create-question/create-question.component';
import { ApercuComponent } from './create/apercu/apercu.component';



const appRoutes : Routes = [
  {path : '' ,component: HomeComponent},
  {path : 'questionnaire/:id', canActivate: [AuthGuardService] , component: Questionnaire2Component},
  {path : 'recap/:id', canActivate: [AuthGuardService] , component: RecapitulatifComponent},
  {path : 'create',canActivate: [AuthGuardService],  component: CreateComponent},
  {path : 'create/question/:id', canActivate: [AuthGuardService] , component: CreateQuestionComponent},
  {path : 'create/apercu/:id', canActivate: [AuthGuardService] , component: ApercuComponent},

  {path : 'signin', component: SigninComponent},
  {path : 'create-user', component: CreateUserComponent}

]




@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    QuestionnaireComponent,
    QuestionSingleComponent,
    SigninComponent,
    CreateComponent,
    Questionnaire2Component,
    CreateUserComponent,
    UserComponent,
    RecapitulatifComponent,
    CreateQuestionComponent,
    ApercuComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [ApiService, AuthGuardService, AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
