document.addEventListener('DOMContentLoaded', function() {
    const temaToggle = document.getElementById('tema-toggle');
    if (temaToggle) {
        temaToggle.addEventListener('click', function() {
            document.body.classList.toggle('tema-oscuro');
            if (document.body.classList.contains('tema-oscuro')) {
                localStorage.setItem('tema', 'oscuro');
            } else {
                localStorage.setItem('tema', 'claro');
            }
        });
    }

    const temaGuardado = localStorage.getItem('tema');
    if (temaGuardado === 'oscuro') {
        document.body.classList.add('tema-oscuro');
    }

    const searchForm = document.querySelector('form[role="search"]');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            let searchTerm = this.querySelector('input[type="search"]').value.trim().toLowerCase();

            const datosInternos = [
                { seccion: 'artistas', nombre: 'Artistas', descripcion: 'Lista de artistas' },
                { seccion: 'tecnicas', nombre: 'Técnicas', descripcion: 'Lista de técnicas' },
                { seccion: 'productos', nombre: 'Productos', descripcion: 'Lista de productos' },
            ];

            const resultadosInternos = datosInternos.filter(dato =>
                dato.nombre.toLowerCase().includes(searchTerm) || dato.descripcion.toLowerCase().includes(searchTerm)
            );

            const resultadosDiv = document.getElementById('resultados-busqueda');
            if (resultadosInternos.length > 0) {
                if (resultadosDiv) {
                    resultadosDiv.innerHTML = '';
                    resultadosInternos.forEach(result => {
                        resultadosDiv.innerHTML += `
                            <div>
                                <h3>${result.nombre}</h3>
                                <p>${result.descripcion}</p>
                                <a href="/${result.seccion}/">Ir a ${result.nombre}</a>
                            </div>
                        `;
                    });
                }
            } else {
                window.location.href = `https://www.google.com/search?q=${searchTerm}`;
            }
        });
    }
});
