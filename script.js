// Example inventory list (simulating a database)
let inventory = [];

// Function to display inventory in the table
function displayInventory() {
    const inventoryList = document.getElementById("inventory-list");
    inventoryList.innerHTML = '';  // Clear existing list
    inventory.forEach((item, index) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.quantity}</td>
            <td>${item.price}</td>
            <td><button onclick="removeItem(${index})">Remove</button></td>
        `;
        inventoryList.appendChild(row);
    });
}

// Add item to inventory when the form is submitted
document.getElementById("add-item-form").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent form from submitting the default way
    const name = document.getElementById("product-name").value;
    const quantity = parseInt(document.getElementById("product-quantity").value);
    const price = parseFloat(document.getElementById("product-price").value);

    // Add new product to inventory
    inventory.push({ name, quantity, price });
    displayInventory();
    
    // Clear input fields
    document.getElementById("product-name").value = '';
    document.getElementById("product-quantity").value = '';
    document.getElementById("product-price").value = '';
});

// Remove item from inventory
function removeItem(index) {
    inventory.splice(index, 1);  // Remove item at the specified index
    displayInventory();  // Re-render the inventory list
}

// Initially display the inventory
displayInventory();
