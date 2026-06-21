import { Component, OnDestroy, OnInit } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import { CalculadoraService } from '../../core/service/calculadora.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

Chart.register(...registerables);

@Component({
  selector: 'app-calculadora',
  imports: [CommonModule, FormsModule],
  templateUrl: './calculadora.component.html',
  styleUrl: './calculadora.component.css'
})
export class CalculadoraComponent implements OnInit, OnDestroy{

  dadosForm = {
    capital_inicial: 1000,
    aporte_mensal: 200,
    taxa_juros: 1,
    tipo_taxa: 'mensal',
    periodo: 12,
    tipo_periodo: 'meses'
  };

  resultados: any = null

  chart:any = null

  constructor(private calculadoraService: CalculadoraService) {}

  ngOnInit(): void {
    // this.enviarCalculo();
  }

  ngOnDestroy(): void {
    if (this.chart) {
      this.chart.destroy()
    }
  }

  calculado = false;

  enviarCalculo() {
    this.calculadoraService.calcular(this.dadosForm).subscribe({
      next: (res) => {
        this.resultados = res;
        this.calculado = true;

        setTimeout(() => {
          this.renderizarGrafico(res.tipo_periodo, res.timeline)
        }, 50);
      },
      error: (err) => console.error('Erro ao conectar com o back-end:', err)
    });
  }

  renderizarGrafico(tipo_periodo: any, timeline: any[]) {
    if (!timeline || timeline.length === 0) {
      console.warn("Nenhum dado de histórico recebido do back-end para desenhar o gráfico.");
      return;
    }

    if (this.chart) {
      this.chart.destroy();
    }

    let labels: string[] = [];
    if (timeline && timeline.length > 0 && 'ano' in timeline[0]) {
      labels = timeline.map((item: any) => `${item.ano}º Ano`);
    } else {
      labels = timeline.map((item: any) => `${item.mes}º Mês`);
    }
    
    const dadosInvestido = timeline.map(item => item.invested);
    const dadosTotal = timeline.map(item => item.total);

    const ctx = document.getElementById('graficoEvolucao') as HTMLCanvasElement;

    if (!ctx) return;

    this.chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Total Investido (Aportes)',
            data: dadosInvestido,
            borderColor: '#9a3b8',
            fill: true,
            tension: 0.2
          },
          {
            label: 'Total Acumulado (Com Juros)',
            data: dadosTotal,
            borderColor: '#10b981',
            fill: true,
            tension: 0.2
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'top' }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: (value: any) => 'R$ ' + Number(value).toLocaleString('pt-BR')
            }
          }
        }
      }
    });
  }
}
