import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [ApiService]
})
export class AppComponent {
  etudiants = [{pseudo: 'mamady'}];
  selectedEtudiant;

  constructor(private api: ApiService) {
    this.getEtudiant();
    this.selectedEtudiant = {id: -1, pseudo: '' , password: '' };
  }
  getEtudiant = () => {
    this.api.getAllEtudiant().subscribe(
      data => {
        this.etudiants = data;
      },
      error => {
        console.log(error);
      }
    );
  }
  EtudiantClicked = (etudiant) => {
    this.api.getOneEtudiant(etudiant.id).subscribe(
      data => {
        this.selectedEtudiant = data;
      },
      error => {
        console.log(error);
      }
    );
  }
  updateEtudiant = () => {
    this.api.updateEtudiant(this.selectedEtudiant).subscribe(
      data => {
        this.getEtudiant();
      },
      error => {
        console.log(error);
      }
    );
  }
  createEtudiant = () => {
    this.api.createEtudiant(this.selectedEtudiant).subscribe(
      data => {
        this.etudiants.push(data);
      },
      error => {
        console.log(error);
      }
    );
  }
  deleteEtudiant = () => {
    this.api.deleteEtudiant(this.selectedEtudiant.id).subscribe(
      data => {
        this.getEtudiant();
      },
      error => {
        console.log(error);
      }
    );
  }
}
