document.addEventListener('DOMContentLoaded', () => {
    const resultados = document.querySelector('#resultados');
    const button = document.querySelector('#buscar');
    const palabra = document.querySelector('#escribir');
    const tipoBusqueda = document.querySelector('#tipo-busqueda');

    let showResultados = false;
    resultados.classList.add('hidden');

    const realizarBusqueda = () => {
        const searchTerm = palabra.value.trim();
        const searchType = tipoBusqueda.value;

        if (searchTerm === '') {
            alert("Por favor, escribe una palabra.");
            return;
        }

        let url = '';

        if (searchType === 'definicion') {
            url = `http://127.0.0.1:5000/definicion/${searchTerm}`;
        } else if (searchType === 'sinonimos') {
            url = `http://127.0.0.1:5000/sinonimos/${searchTerm}`;
        } else if (searchType === 'antonimos') {
            url = `http://127.0.0.1:5000/antonimos/${searchTerm}`;
        }

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('No se encontraron resultados.');
                }
                return response.json();
            })
            .then(data => {
                if (searchType === 'definicion') {
                    if (data.error) {
                        resultados.innerHTML = '<p>No se encontraron resultados.</p>';
                    } else {
                        const { definition, _id } = data;
                        resultados.innerHTML = `
                            <p><strong>Definición:</strong> ${definition}</p>
                            <p><strong>ID:</strong> ${_id}</p>
                        `;
                    }
                } else if (searchType === 'sinonimos') {
                    if (data.error) {
                        resultados.innerHTML = '<p>No se encontraron resultados.</p>';
                    } else {
                        const { sinonimos, _id } = data;
                        resultados.innerHTML = `
                            <p><strong>Sinónimos:</strong> ${sinonimos}</p>
                            <p><strong>ID:</strong> ${_id}</p>
                        `;
                    }
                } else if (searchType === 'antonimos') {
                    if (data.error) {
                        resultados.innerHTML = '<p>No se encontraron resultados.</p>';
                    } else {
                        const { antonimos, _id } = data;
                        resultados.innerHTML = `
                            <p><strong>Antónimos:</strong> ${antonimos}</p>
                            <p><strong>ID:</strong> ${_id}</p>
                        `;
                    }
                }
            })
            .catch(error => {
                resultados.innerHTML = `<p>Error al realizar la búsqueda: ${error.message}</p>`;
            })
            .finally(() => {
                resultados.classList.remove('hidden');
            });
    };

    button.addEventListener('click', realizarBusqueda);

    palabra.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            realizarBusqueda();
        }
    });
});
