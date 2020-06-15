import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';
import {  Subscription } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {




  isAuth : boolean;
  constructor(
    private authService : AuthService,
    private router : Router
  ) { }

  ngOnInit(): void {
     this.authService.isAuthSubject.subscribe(
      (res) => {
        this.isAuth = res;
      }
    );
  }

  onSignOut(){
    this.authService.signOut();
    this.router.navigate(['/']);
  }

  isProf(){
    return true;

  }
}
