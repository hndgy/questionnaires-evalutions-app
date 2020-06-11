import { Injectable } from '@angular/core';
import { User } from '../models/User.models';
import { ApiService } from './api.service';
import { Subject } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  connected_user : number;
  isAuthSubject = new Subject<boolean>();

  isAuth : boolean;

  emitIsAuth(){
    this.isAuthSubject.next(this.isAuth);
  }

  constructor(private apiService: ApiService, private router: Router) { }

  ngOnInit(): void {
    
  }


  signIn(login: string, pwd : string){
      return this.apiService.login(login,pwd);
    
  }

  setToken(token: string){
    this.apiService.setToken(token);
    console.log(token);
    
  }

  signOut(){
    this.connected_user = undefined;
    this.isAuth = false ;
    this.emitIsAuth();
  }

  isConnected(){
    return this.isAuth;
  }

}
