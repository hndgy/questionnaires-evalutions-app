import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';
import { Questionnaire } from '../models/Questionnaire.models';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

   questionnaires : Questionnaire[];

  constructor(private apiService : ApiService, private router: Router, private authService: AuthService) { }

  ngOnInit(): void {
    this.getQuestionnaires();
  }


  getQuestionnaires(){
    this.apiService.getListQuestionnaire().subscribe(
      (res: any ) => {
        this.questionnaires = res['results'] ;
        console.log(res);
        
 
      }
    );

  }


  afficherQuestionnaire(id: number){
      this.router.navigate(['/questionnaire',id])
  }


  dejaParticipe(list_repondant: number[]){
    return list_repondant.includes(this.authService.connected_user);
    
      
  }

}
