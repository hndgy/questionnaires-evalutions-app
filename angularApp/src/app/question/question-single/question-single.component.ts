import { Component, OnInit, Input } from '@angular/core';
import { Question } from 'src/app/models/Question.models';

@Component({
  selector: 'app-question-single',
  templateUrl: './question-single.component.html',
  styleUrls: ['./question-single.component.scss']
})
export class QuestionSingleComponent implements OnInit {


  @Input() question : Question;
  @Input() index : number;
  
  constructor() { }

  ngOnInit(): void {
  }

}
