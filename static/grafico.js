var myChart;

function redirecionar() {
  var inputSalario = document.querySelector('input[name="salario"]').value;
  var inputGasto = document.querySelector('input[name="gasto"]').value;
  if (inputSalario && inputGasto) {
    atualizarGrafico(parseFloat(inputSalario), parseFloat(inputGasto));
  } else {
    alert("Por favor, preencha os campos antes de entrar.");
  }
}

function atualizarGrafico(salario, gasto) {
  if (myChart) {
    myChart.destroy(); // Destrua o gráfico existente antes de criar um novo
  }

  const ctx = document.getElementById('myChart').getContext('2d');
  const diferenca = salario - gasto;
  const categorias = ['Salário', 'Gastos', 'Diferença'];
  const valores = [salario, gasto, diferenca];
  window.onload = function() {
    const button1 = document.getElementById("openModalDiv1");
    const modal1 = document.getElementById("dialog1");
  
    button1.onclick = function() {
      modal1.showModal();
    };
  };  
  myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: categorias,
      datasets: [{
        label: 'Valores',
        data: valores,
        backgroundColor: ['blue', 'red', 'green'],
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Resumo Financeiro',
        fontColor: 'white' // Cor do título
      },
      scales: {
        xAxes: [{
          ticks: {
            fontColor: 'white' // Cor dos números no eixo X
          },
          gridLines: {
            color: 'white' // Cor das linhas de grade no eixo X
          }
        }],
        yAxes: [{
          ticks: {
            fontColor: 'white' // Cor dos números no eixo Y
          },
          gridLines: {
            color: 'white' // Cor das linhas de grade no eixo Y
          }
        }]
      },
      legend: {
        labels: {
          fontColor: 'white' // Cor das legendas
        }
      }
    }
  });
}

