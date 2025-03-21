document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("cubeCanvas");
    if (canvas.getContext) {
        const ctx = canvas.getContext("2d");
        const size = 50; // Size of each square
        // Draw a 3x3 grid with random colors to simulate a Rubik's cube face
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                // Generate a random color in hex format
                const color = '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
                ctx.fillStyle = color;
                ctx.fillRect(j * size, i * size, size, size);
                ctx.strokeStyle = "#000";
                ctx.strokeRect(j * size, i * size, size, size);
            }
        }
        ctx.font = "20px Arial";
        ctx.fillStyle = "black";
        ctx.fillText("Rubik's Cube Placeholder", 10, 200);
    }
});
