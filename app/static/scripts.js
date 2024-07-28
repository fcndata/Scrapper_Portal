document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll('.gusto-button');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const itemId = this.dataset.id;
            const gusto = this.dataset.gusto;

            fetch('/label', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `item_id=${itemId}&gusto=${gusto}`
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Actualizar la interfaz según sea necesario
                        alert("¡Etiqueta actualizada con éxito!");
                    } else {
                        alert("Error al actualizar la etiqueta.");
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        });
    });
});
