// scripts.js

let expenses = [];

document.getElementById('add-expense').addEventListener('submit', function(e) {
    e.preventDefault();

    const expenseName = document.getElementById('expense-name').value;
    const expenseAmount = parseFloat(document.getElementById('expense-amount').value);

    const expense = {
        id: expenses.length + 1,
        name: expenseName,
        amount: expenseAmount
    };

    expenses.push(expense);
    updateExpenseList();
    document.getElementById('add-expense').reset();
});

function updateExpenseList() {
    const expenseTableBody = document.getElementById('expense-table-body');
    expenseTableBody.innerHTML = '';

    expenses.forEach(expense => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${expense.name}</td>
            <td>$${expense.amount.toFixed(2)}</td>
            <td>
                <button onclick="deleteExpense(${expense.id})">Delete</button>
            </td>
        `;
        expenseTableBody.appendChild(row);
    });
}

function deleteExpense(id) {
    expenses = expenses.filter(expense => expense.id !== id);
    updateExpenseList();
}