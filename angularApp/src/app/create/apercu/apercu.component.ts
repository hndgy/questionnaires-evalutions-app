import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-apercu',
  templateUrl: './apercu.component.html',
  styleUrls: ['./apercu.component.scss']
})
export class ApercuComponent implements OnInit {

  id_questionnaire : number;
  questionnaire;

  constructor(

    private route: ActivatedRoute,
    private router: Router,
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
    this.id_questionnaire = this.route.snapshot.params['id'];
    this.getQuestionnaire();
    
  }

  getQuestionnaire(){
      this.apiService.getQuestionnaireByID(this.id_questionnaire).subscribe(
        (res) => {
          this.questionnaire = res;
        }
      );
  }

  onAjouter(){
    this.router.navigate(['/create', 'question']);
  }



}
