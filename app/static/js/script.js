function addIngredient() {
    fetchIngredients() 
}

function deleteIngredient(element) {
    element.parentElement.remove();
}

document.addEventListener('DOMContentLoaded', function() {
    // Initialize with one ingredient row
    addIngredient();
});

function fetchIngredients() {
    fetch('/ingredients')
        .then(response => response.json())
        .then(data => {
            const ingredientsList = document.getElementById('ingredientsList');
            const row = document.createElement('div');
            row.className = 'ingredient-row';
            let options = data.map(ingredient => `<option value="${ingredient.id}">${ingredient.name}</option>`).join('');
            row.innerHTML = `
                <select name="ingredient[]" required>
                    <option value="">Select Ingredient</option>
                    ${options}
                </select>
                <input type="number" name="quantity[]" placeholder="Quantity" step="0.01" required>
                <button type="button" class="delete-btn" onclick="deleteIngredient(this)">Delete</button>
            `;
            ingredientsList.appendChild(row);
        });
}