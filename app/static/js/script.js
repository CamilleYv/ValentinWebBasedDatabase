function addIngredient() {
    const ingredientsList = document.getElementById('ingredientsList');
    const row = document.createElement('div');
    row.className = 'ingredient-row';
    row.innerHTML = `
        <select name="ingredient[]" required>
            <option value="">Select Ingredient</option>
            <option value="flour">Flour</option>
            <option value="water">Water</option>
            <option value="sugar">Sugar</option>
            <!-- Additional ingredients -->
        </select>
        <input type="number" name="quantity[]" placeholder="Quantity" step="0.01" required>
        <button type="button" class="delete-btn" onclick="deleteIngredient(this)">Delete</button>
    `;
    ingredientsList.appendChild(row);
}

function deleteIngredient(element) {
    element.parentElement.remove();
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('recipeForm').addEventListener('submit', function(event) {
        event.preventDefault();
        // Implement form data collection and submission to server here
        alert('Recipe submitted! (Implement submission logic)');
    });

    // Initialize with one ingredient row
    addIngredient();
});
