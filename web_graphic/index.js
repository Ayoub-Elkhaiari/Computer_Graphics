// Function to create the grid
function createGrid(rows, cols) {
    const gridContainer = document.getElementById("grid-container");
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const cell = document.createElement("div");
            cell.className = "grid-cell";
            cell.addEventListener("click", toggleCell);
            gridContainer.appendChild(cell);
        }
    }
}

// Function to toggle the cell's color
function toggleCell() {
    this.classList.toggle("active");
}

// Create a 20x20 grid on page load
createGrid(20, 20);
