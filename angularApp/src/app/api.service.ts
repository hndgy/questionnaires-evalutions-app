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

  getAllEtudiant(): Observable<any> {
    return this.http.get(this.baseurl + '/etudiants/',
    {headers: this.httpHeaders});
  }
  getOneEtudiant(id): Observable<any> {
    return this.http.get(this.baseurl + '/etudiants/' + id + '/',
    {headers: this.httpHeaders});
  }
  updateEtudiant(etudiant): Observable<any> {
    const body = {pseudo: etudiant.pseudo , password: etudiant.password };
    return this.http.put(this.baseurl + '/etudiants/' + etudiant.id + '/', body,
    {headers: this.httpHeaders});
  }
  createEtudiant(etudiant): Observable<any> {
    const body = {pseudo: etudiant.pseudo , password: etudiant.password };
    return this.http.post(this.baseurl + '/etudiants/', body,
    {headers: this.httpHeaders});
  }
  deleteEtudiant(id): Observable<any> {
    return this.http.delete(this.baseurl + '/etudiants/' + id + '/',
    {headers: this.httpHeaders});
  }
}
