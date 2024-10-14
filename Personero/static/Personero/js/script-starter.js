$(document).ready(function() {
    // Datos de prueba (esto normalmente vendría del servidor)
    let candidatos = [
        { id: 1, nombre: "Juan Pérez", votos: 120, imagen: "https://voto-vision.s3.amazonaws.com/publico/fotos_perfil/Juan.jpg" },
        { id: 2, nombre: "María López", votos: 150, imagen: "https://voto-vision.s3.amazonaws.com/publico/fotos_perfil/Maria.jpg" },
        { id: 3, nombre: "Carlos Gómez", votos: 100, imagen: "https://voto-vision.s3.amazonaws.com/publico/fotos_perfil/Carlos.jpg" }
    ];
    let totalVotos = 370; // Ejemplo total de votos

    // Cargar lista de candidatos
    function cargarCandidatos() {
        $('#lista-candidatos').empty();
        candidatos.forEach(candidato => {
            $('#lista-candidatos').append(
                `<div class="candidato">
                    <img src="${candidato.imagen}" alt="${candidato.nombre}" class="candidato-img">
                    <h3>${candidato.nombre}</h3>
                    <p>Votos: ${candidato.votos}</p>
                    <button onclick="votar(${candidato.id})">Votar</button>
                </div>`
            );
        });
    }

    // Cargar resultados de la elección
    function cargarResultados() {
        $('#tabla-resultados').empty();
        $('#tabla-resultados').append(`
            <table>
                <tr>
                    <th>Candidato</th>
                    <th>Votos</th>
                    <th>Porcentaje</th>
                </tr>
            `);
        candidatos.forEach(candidato => {
            let porcentaje = ((candidato.votos / totalVotos) * 100).toFixed(2);
            $('#tabla-resultados').append(`
                <tr>
                    <td>${candidato.nombre}</td>
                    <td>${candidato.votos}</td>
                    <td>${porcentaje}%</td>
                </tr>
            `);
        });
        $('#tabla-resultados').append(`</table>`);
    }

    // Simular votación (esto normalmente sería una llamada AJAX al servidor)
    window.votar = function(id) {
        let candidato = candidatos.find(c => c.id === id);
        candidato.votos++;
        totalVotos++;
        cargarCandidatos();
        cargarResultados();
    }

    // Registro de usuario
    $('#registro-form').submit(function(event) {
        event.preventDefault();
        alert('Registro exitoso para ' + $('#nombre').val());
    });

    // Inicializar
    cargarCandidatos();
    cargarResultados();
});
