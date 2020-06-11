import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';
import { Questionnaire } from '../models/Questionnaire.models';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

   questionnaires : Questionnaire[];

  constructor(private apiService : ApiService, private router: Router) { }

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

}
