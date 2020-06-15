import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-recapitulatif',
  templateUrl: './recapitulatif.component.html',
  styleUrls: ['./recapitulatif.component.scss']
})
export class RecapitulatifComponent implements OnInit {


  recapitulatif;
  

  constructor(
    private apiService: ApiService,
    private activatedRoute: ActivatedRoute,
    private authService: AuthService


    ) { }

  ngOnInit(): void {

    this.apiService.get_recap(this.authService.connected_user, this.activatedRoute.snapshot.params['id']).subscribe(
      (res) => {
        this.recapitulatif = res['recapitulatif'][0];
      }
    );
  }

  isArray(l){
    return l instanceof Array; 
  }

}
