var myChart;

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
function save_salary(salary) {
  let nomeUsuario = window.location.pathname.split('/')[2];
  fetch(`/usuario/${nomeUsuario}/salva_salario`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({"table" : salary})
  });
}

function redirecionar() {
  var inputSalario = document.querySelector('input[name="salario"]').value;
  //var inputGasto = document.querySelector('input[name="gasto"]').value;
  save_salary(inputSalario);
  if (inputSalario) {
    show_tables();
  } else {
    alert("Por favor, preencha os campos antes de entrar.");
  }
}

function show_tables() {
  let nomeUsuario = window.location.pathname.split('/')[2];
  fetch(`/usuario/${nomeUsuario}/mostrar_tabelas`, {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json',
      },
  })
  .then(response => response.json())
  .then(results => {
      let soma_gasto = 0;
      results.forEach(result => {
        console.log(result);
          salario = result[0];
          soma_gasto += result[1];
      });
      console.log(`Soma dos gastos: ${soma_gasto}`);
      atualizarGrafico(salario, soma_gasto);
  })
  .catch(error => {
      console.error('Erro ao buscar tabelas:', error);
  });
}
