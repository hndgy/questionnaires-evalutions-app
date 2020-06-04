import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [ApiService]
})
export class AppComponent {
  utilisateurs = [{nom: 'mamady'}];
  selectedUtilisateur;

  constructor(private api: ApiService) {
    this.getUtilisateurs();
    this.selectedUtilisateur = {id: -1, nom: '' , prenom: '' , num: 0 , role: '' , password: '' };
  }
  getUtilisateurs = () => {
    this.api.getAllUtilisateurs().subscribe(
      data => {
        this.utilisateurs = data;
      },
      error => {
        console.log(error);
      }
    );
  }
  UtilisateurClicked = (utilisateur) => {
    this.api.getOneUtilisateur(utilisateur.id).subscribe(
      data => {
        this.selectedUtilisateur = data;
      },
      error => {
        console.log(error);
      }
    );
  }
  updateUtilisateur = () => {
    this.api.updateUtilisateur(this.selectedUtilisateur).subscribe(
      data => {
        this.getUtilisateurs();
      },
      error => {
        console.log(error);
      }
    );
  }
  createUtilisateur = () => {
    this.api.createUtilisateur(this.selectedUtilisateur).subscribe(
      data => {
        this.utilisateurs.push(data);
      },
      error => {
        console.log(error);
      }
    );
  }
  deleteUtilisateur = () => {
    this.api.deleteUtilisateur(this.selectedUtilisateur.id).subscribe(
      data => {
        this.getUtilisateurs();
      },
      error => {
        console.log(error);
      }
    );
  }
}
