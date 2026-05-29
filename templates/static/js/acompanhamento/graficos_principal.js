
const cores = [
    '#36A2EB',
    '#FF6384',
    '#FFCE56',
    '#4BC0C0',
    '#9966FF',
    '#FF9F40',
    '#8BC34A',
    '#E91E63',
    '#3F51B5',
    '#009688'
];

// =========================
// TURNOS
// =========================



fetch('/acompanhamento/api/grafico-turno_estuda/')
.then(response => response.json())
.then(data => {

    let total = data.valores.reduce((a, b) => a + b, 0);

    let maiorValor = Math.max(...data.valores);

    let indexMaior = data.valores.indexOf(maiorValor);

    document.getElementById('turnoMais').innerHTML =
        data.labels[indexMaior];

    document.getElementById('totalAlunos').innerHTML = total;

    new Chart(
        document.getElementById('graficoTurnoBarra'),
        {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Quantidade',
                    data: data.valores,
                    backgroundColor: cores
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    );

    new Chart(
        document.getElementById('graficoTurnoPizza'),
        {
            type: 'pie',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.valores,
                    backgroundColor: cores
                }]
            },
            plugins: [ChartDataLabels],
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    datalabels: {
                        color: '#fff',
                        formatter: (value) => {
                            let porcentagem =
                                ((value / total) * 100).toFixed(1);

                            return porcentagem + '%';
                        }
                    }
                }
            }
        }
    );

    let legenda = `<div class="d-flex flex-wrap gap-3">`;

    data.labels.forEach((turno, index) => {

        let porcentagem =
            ((data.valores[index] / total) * 100).toFixed(1);

        legenda += `

            <div class="d-flex align-items-center">

                <div
                    style="
                        width:14px;
                        height:14px;
                        border-radius:50%;
                        background:${cores[index]};
                        margin-right:8px;
                    ">
                </div>

                <small>
                    ${turno} - ${porcentagem}%
                </small>

            </div>

        `;

    });

    legenda += `</div>`;

    document.getElementById('legendaTurnos').innerHTML = legenda;

    

});

// =========================
// BAIRROS
// =========================

fetch('/acompanhamento/api/grafico-bairros/')
.then(response => response.json())
.then(data => {

    // TOTAL DE BAIRROS/CIDADES
    document.getElementById('totalBairros').innerHTML =
        data.labels.length;

    // BAIRRO-CIDADE MAIS FREQUENTE
    let maiorValorBairro = Math.max(...data.valores);

    let indexMaiorBairro =
        data.valores.indexOf(maiorValorBairro);

    document.getElementById('totalBairros').innerHTML =
        data.labels[indexMaiorBairro];

    // GRÁFICO DE BARRAS
    new Chart(
        document.getElementById('graficoBairros'),
        {
            type: 'bar',

            data: {
                labels: data.labels,

                datasets: [{
                    label: 'Quantidade',
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    );

    let total = data.valores.reduce((a, b) => a + b, 0);

    // GRÁFICO PIZZA
    new Chart(
        document.getElementById('graficoBairrosPizza'),
        {
            type: 'pie',

            data: {
                labels: data.labels,

                datasets: [{
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            plugins: [ChartDataLabels],

            options: {

                responsive: true,
                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    },

                    datalabels: {

                        color: '#fff',

                        formatter: (value) => {

                            let porcentagem =
                                ((value / total) * 100).toFixed(1);

                            return porcentagem + '%';

                        }

                    }

                }

            }

        }
    );

    // LEGENDA
    let legenda = `

        <div class="d-flex flex-wrap gap-3">

    `;

    data.labels.forEach((bairro, index) => {

        let porcentagem =
            ((data.valores[index] / total) * 100).toFixed(1);

        legenda += `

            <div class="d-flex align-items-center">

                <div
                    style="
                        width:14px;
                        height:14px;
                        border-radius:50%;
                        background:${cores[index]};
                        margin-right:8px;
                    ">
                </div>

                <small>
                    ${bairro} - ${porcentagem}%
                </small>

            </div>

        `;

    });

    legenda += `</div>`;

    document.getElementById('legendaBairros').innerHTML = legenda;

});


// =========================
// CURSOS
// =========================

fetch('/acompanhamento/api/grafico-cursos/')
.then(response => response.json())
.then(data => {

    document.getElementById('totalCursos').innerHTML =
        data.labels.length;

    // BARRAS
    new Chart(
        document.getElementById('graficoCursos'),
        {
            type: 'bar',

            data: {
                labels: data.labels,

                datasets: [{
                    label: 'Quantidade',
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    );

    let total = data.valores.reduce((a, b) => a + b, 0);

    // PIZZA
    new Chart(
        document.getElementById('graficoCursosPizza'),
        {
            type: 'pie',

            data: {
                labels: data.labels,

                datasets: [{
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            plugins: [ChartDataLabels],

            options: {

                responsive: true,
                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    },

                    datalabels: {

                        color: '#fff',

                        formatter: (value) => {

                            let porcentagem =
                                ((value / total) * 100).toFixed(1);

                            return porcentagem + '%';

                        }

                    }

                }

            }

        }
    );

    // LEGENDA
    let legenda = `

        <div class="d-flex flex-wrap gap-3">

    `;

    data.labels.forEach((curso, index) => {

        let porcentagem =
            ((data.valores[index] / total) * 100).toFixed(1);

        legenda += `

            <div class="d-flex align-items-center">

                <div
                    style="
                        width:14px;
                        height:14px;
                        border-radius:50%;
                        background:${cores[index]};
                        margin-right:8px;
                    ">
                </div>

                <small>
                    ${curso} - ${porcentagem}%
                </small>

            </div>

        `;

    });

    legenda += `</div>`;

    document.getElementById('legendaCursos').innerHTML = legenda;

});


// =========================
// IDADES
// =========================

fetch('/acompanhamento/api/grafico-idades/')
.then(response => response.json())
.then(data => {

    // BARRAS
    new Chart(
        document.getElementById('graficoIdade'),
        {
            type: 'bar',

            data: {
                labels: data.labels,

                datasets: [{
                    label: 'Quantidade',
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    );

    let total = data.valores.reduce((a, b) => a + b, 0);

    // PIZZA
    new Chart(
        document.getElementById('graficoIdadePizza'),
        {
            type: 'pie',

            data: {
                labels: data.labels,

                datasets: [{
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            plugins: [ChartDataLabels],

            options: {

                responsive: true,
                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    },

                    datalabels: {

                        color: '#fff',

                        formatter: (value) => {

                            let porcentagem =
                                ((value / total) * 100).toFixed(1);

                            return porcentagem + '%';

                        }

                    }

                }

            }

        }
    );

    // LEGENDA
    let legenda = `

        <div class="d-flex flex-wrap gap-3">

    `;

    data.labels.forEach((idade, index) => {

        let porcentagem =
            ((data.valores[index] / total) * 100).toFixed(1);

        legenda += `

            <div class="d-flex align-items-center">

                <div
                    style="
                        width:14px;
                        height:14px;
                        border-radius:50%;
                        background:${cores[index]};
                        margin-right:8px;
                    ">
                </div>

                <small>
                    ${idade} anos - ${porcentagem}%
                </small>

            </div>

        `;

    });

    legenda += `</div>`;

    document.getElementById('legendaIdades').innerHTML = legenda;

});


// =============================
// ESCOLARIDADE
// =============================

fetch('/acompanhamento/api/grafico-escolaridade/')
.then(response => response.json())
.then(data => {

    let total = data.valores.reduce((a, b) => a + b, 0);

    // BARRAS
    new Chart(
        document.getElementById('graficoEscolaridadeBarra'),
        {
            type: 'bar',

            data: {
                labels: data.labels,

                datasets: [{
                    label: 'Quantidade',
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    );

    // PIZZA
    new Chart(
        document.getElementById('graficoEscolaridadePizza'),
        {
            type: 'pie',

            data: {
                labels: data.labels,

                datasets: [{
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            plugins: [ChartDataLabels],

            options: {

                responsive: true,
                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    },

                    datalabels: {

                        color: '#fff',

                        formatter: (value) => {

                            let porcentagem =
                                ((value / total) * 100).toFixed(1);

                            return porcentagem + '%';

                        }

                    }

                }

            }

        }
    );

    // LEGENDA
    let legenda = `

        <div class="d-flex flex-wrap gap-3">

    `;

    data.labels.forEach((escolaridade, index) => {

        let porcentagem =
            ((data.valores[index] / total) * 100).toFixed(1);

        legenda += `

            <div class="d-flex align-items-center">

                <div
                    style="
                        width:14px;
                        height:14px;
                        border-radius:50%;
                        background:${cores[index]};
                        margin-right:8px;
                    ">
                </div>

                <small>
                    ${escolaridade} - ${porcentagem}%
                </small>

            </div>

        `;

    });

    legenda += `</div>`;

    document.getElementById('legendaEscolaridade').innerHTML = legenda;

});


// =============================
// Aprendizagem
// =============================



fetch('/acompanhamento/api/grafico-aprendizagem/')
.then(response => response.json())
.then(data => {

    let total = data.valores.reduce((a, b) => a + b, 0);

    // BARRAS
    new Chart(
        document.getElementById('graficoAprendizagemBarra'),
        {
            type: 'bar',

            data: {
                labels: data.labels,

                datasets: [{
                    label: 'Quantidade',
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    );

    // PIZZA
    new Chart(
        document.getElementById('graficoAprendizagemPizza'),
        {
            type: 'pie',

            data: {
                labels: data.labels,

                datasets: [{
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            plugins: [ChartDataLabels],

            options: {

                responsive: true,
                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    },

                    datalabels: {

                        color: '#fff',

                        formatter: (value) => {

                            let porcentagem =
                                ((value / total) * 100).toFixed(1);

                            return porcentagem + '%';

                        }

                    }

                }

            }

        }
    );

    // LEGENDA
    let legenda = `

        <div class="d-flex flex-wrap gap-3">

    `;

    data.labels.forEach((aprendizagem, index) => {

        let porcentagem =
            ((data.valores[index] / total) * 100).toFixed(1);

        legenda += `

            <div class="d-flex align-items-center">

                <div
                    style="
                        width:14px;
                        height:14px;
                        border-radius:50%;
                        background:${cores[index]};
                        margin-right:8px;
                    ">
                </div>

                <small>
                    ${aprendizagem} - ${porcentagem}%
                </small>

            </div>

        `;

    });

    legenda += `</div>`;

    document.getElementById('legendaAprendizagem').innerHTML = legenda;

});



// =============================
// Entidade
// =============================



fetch('/acompanhamento/api/grafico-entidade/')
.then(response => response.json())
.then(data => {

    let total = data.valores.reduce((a, b) => a + b, 0);

    // BARRAS
    new Chart(
        document.getElementById('graficoEntidadeBarra'),
        {
            type: 'bar',

            data: {
                labels: data.labels,

                datasets: [{
                    label: 'Quantidade',
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    );

    // PIZZA
    new Chart(
        document.getElementById('graficoEntidadePizza'),
        {
            type: 'pie',

            data: {
                labels: data.labels,

                datasets: [{
                    data: data.valores,
                    backgroundColor: cores
                }]
            },

            plugins: [ChartDataLabels],

            options: {

                responsive: true,
                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    },

                    datalabels: {

                        color: '#fff',

                        formatter: (value) => {

                            let porcentagem =
                                ((value / total) * 100).toFixed(1);

                            return porcentagem + '%';

                        }

                    }

                }

            }

        }
    );

    // LEGENDA
    let legenda = `

        <div class="d-flex flex-wrap gap-3">

    `;

    data.labels.forEach((entidade, index) => {

        let porcentagem =
            ((data.valores[index] / total) * 100).toFixed(1);

        legenda += `

            <div class="d-flex align-items-center">

                <div
                    style="
                        width:14px;
                        height:14px;
                        border-radius:50%;
                        background:${cores[index]};
                        margin-right:8px;
                    ">
                </div>

                <small>
                    ${entidade} - ${porcentagem}%
                </small>

            </div>

        `;

    });

    legenda += `</div>`;

    document.getElementById('legendaEntidade').innerHTML = legenda;

});


function irPara(id) {
    document.getElementById(id).scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}
