import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CalculadoraService {

  private apiUrl = 'http://localhost:8000/api/calcular';

  constructor(private http:  HttpClient) { }

  calcular(dados: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, dados)
  }

}
