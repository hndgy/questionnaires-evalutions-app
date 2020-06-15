import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from '../models/User.models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  readonly host = "http://localhost:8000/";
  readonly api_host = this.host + "api/";

  token;

  headers: HttpHeaders;

  constructor(private httpClient: HttpClient) { 

 
  }



  setToken(token: string){
    this.headers = new HttpHeaders().set("Authorization","Token " + token)
  }

  getListQuestionnaire(){
  
    
    return this.httpClient.get(this.api_host + "Questionnaire/", );
  }

  getListQuestion(){
    return this.httpClient.get(this.api_host + "Question/",{ 'headers' : this.headers} );
  }

  getQuestionnaireByID(id: number){
    return this.httpClient.get(this.api_host + "show_questionnaire/"+ id, { 'headers' : this.headers});
  }


  getQuestionByID(id: number){
    return this.httpClient.get(this.api_host + "show_question/"+ id, { 'headers' : this.headers});
  }

  createResponse(id_question: number, id_user: number, listRep: [], id_questionnaire: number){
    return this.httpClient.post(this.api_host + "create_reponse/",  {'FK_Question': [id_question.toString()], 'FK_Utilisateur': [id_user.toString()], 'listReponse': listRep, 'FK_Questionnaire': [id_questionnaire.toString()]});
  }




  getUser(login: string, pwd: string) {
      return this.httpClient.get(this.api_host + "get_utilisateur/" + login + "/" + pwd);
  }


  getReponse(id : number){
    return this.httpClient.get(this.api_host + "reponse/" + id.toString(), { 'headers' : this.headers});
  }

  login(username : string , password : string){
  
    
    return this.httpClient.post(this.host + "login/",{"username" : username, "password" : password});
  }

  create_user(nom,prenom, num, role, password){
    return this.httpClient.post(this.host + "register",
     {
       "nom" : nom, 
       "prenom" : prenom,
       "num" : num,
       "role" : role,
       "password" : password, 
       "password2" : password

    });

  }

  save_rep( reponses: any[]){
    return this.httpClient.post(this.api_host + "save_reponseUser/", reponses, { 'headers' : this.headers});
  }


  get_recap(id_user,id_questionnaire){
    return this.httpClient.get(this.api_host + "show_recap_user/"+id_user+"/"+id_questionnaire, { 'headers' : this.headers} );
  }


  create_questionnaire(libelle: string, id_prof: number){
    return this.httpClient.post(this.api_host + "create_questionnaire/", {"libelle" : libelle, "prof" : id_prof.toString()}, { 'headers' : this.headers});
  }

  create_question(liste_question){

    return this.httpClient.post(this.api_host + "create_question", 
    {
      liste_question
    } ,{ 'headers' : this.headers});


  }

}








