function daysDiff(d1, d2) {
    const oneDay = 24 * 60 * 60 * 1000;
    return Math.round((d2 - d1) / oneDay);
  }
  
  function addElementToTable() {
    let conta = prompt("Digite o nome da conta:");
    if (conta === null) return;
  
    let valor = prompt("Digite o valor da conta:");
    if (valor === null) return;
  
    let data = prompt("Digite a data de vencimento (dd/mm/aaaa):");
    if (data === null) return;
  
    let tableBody = document.getElementById('table-body');
    let newRow = tableBody.insertRow();
    newRow.insertCell(0).innerHTML = conta;
    newRow.insertCell(1).innerHTML = valor;
    newRow.insertCell(2).innerHTML = data;
  
    let statusCheckbox = document.createElement('input');
    statusCheckbox.type = 'checkbox';
    statusCheckbox.onchange = function() {
        if (statusCheckbox.checked) {
            newRow.className = 'pago';
        } else {
            updateRowStatusBasedOnDate(newRow, data);
        }
    };
  
    let statusCell = newRow.insertCell(3);
    statusCell.appendChild(statusCheckbox);
  
    // Adicionando a palavra "Pago" ao lado da caixa de seleção
    let statusLabel = document.createElement('span');
    statusLabel.textContent = " Pago";
    statusCell.appendChild(statusLabel);
  
    // Define o status inicial baseado na data de vencimento
    updateRowStatusBasedOnDate(newRow, data);
  
    let actionCell = newRow.insertCell(4);
    let deleteButton = document.createElement('button');
    deleteButton.innerHTML = 'Apagar';
    deleteButton.onclick = function() { deleteRow(newRow); };
    actionCell.appendChild(deleteButton);
  }
  
  function updateRowStatusBasedOnDate(row, dueDateString) {
    let currentDate = new Date();
    let [day, month, year] = dueDateString.split("/");
    let dueDate = new Date(year, month - 1, day);
  
    let daysDifference = daysDiff(currentDate, dueDate);
    if (daysDifference < 0) {
        row.className = 'atrasado';
    } else if (daysDifference <= 3) {
        row.className = 'alerta';
    } else {
        row.className = 'neutro';
    }
  }
  
  function deleteRow(row) {
    row.parentElement.removeChild(row);
  }
  
  // Adiciona o evento de click ao botão "Adicionar Elemento"
  document.addEventListener('DOMContentLoaded', function() {
    let addButton = document.querySelector(".addElementButton");
    if (addButton) {
        addButton.addEventListener('click', addElementToTable);
    }
  });
  
  // Usando JavaScript puro
  window.addEventListener("load", function() {
    document.body.classList.add("loaded");
  });


  