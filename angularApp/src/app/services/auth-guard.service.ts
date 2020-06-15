import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { AuthService } from './auth.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate{

  constructor(private router : Router, private authService: AuthService) { }

  canActivate(): Observable<boolean> | Promise<boolean> | boolean {

    if (! this.authService.isConnected()){
        this.router.navigate(['/signin']);
        
    }
    return true;
    
  }
}

