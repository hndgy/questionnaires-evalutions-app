import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

  constructor(private http: HttpClient) { }

  getAllUtilisateurs(): Observable<any> {
    return this.http.get(this.baseurl + '/utilisateurs/',
    {headers: this.httpHeaders});
  }
  getOneUtilisateur(id): Observable<any> {
    return this.http.get(this.baseurl + '/utilisateurs/' + id + '/',
    {headers: this.httpHeaders});
  }
  updateUtilisateur(utilisateur): Observable<any> {
    const body = {nom: utilisateur.nom , prenom: utilisateur.prenom , num: utilisateur.num ,
    role: utilisateur.role , password: utilisateur.password};
    return this.http.put(this.baseurl + '/utilisateurs/' + utilisateur.id + '/', body,
    {headers: this.httpHeaders});
  }
  createUtilisateur(utilisateur): Observable<any> {
    const body = {nom: utilisateur.nom , prenom: utilisateur.prenom , num: utilisateur.num ,
    role: utilisateur.role , password: utilisateur.password};
    return this.http.post(this.baseurl + '/utilisateurs/', body,
    {headers: this.httpHeaders});
  }
  deleteUtilisateur(id): Observable<any> {
    return this.http.delete(this.baseurl + '/utilisateurs/' + id + '/',
    {headers: this.httpHeaders});
  }
}
