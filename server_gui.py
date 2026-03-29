<!DOCTYPE html>
<html>
<head>
    <title>AidanOS Downloads Timeline</title>
    <style>
        body {
            background: #0d1117;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        .card {
            background: #161b22;
            margin: 20px auto;
            padding: 20px;
            width: 300px;
            border-radius: 10px;
        }

        button {
            background: #2ea043;
            border: none;
            padding: 10px 20px;
            color: white;
            cursor: pointer;
            border-radius: 5px;
        }

        #chartContainer {
            width: 90%;
            max-width: 900px;
            margin: 40px auto;
        }
    </style>
</head>
<body>

<h1>AidanOS Downloads & Timeline</h1>

<div id="versions"></div>

<div id="chartContainer">
    <canvas id="timelineChart"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const versions = [
    {name:"26.0", date:"2026-01-01", end:"2026-03-01", file:"aidanos26_0.py"},
    {name:"26.1", date:"2026-01-21", end:"2026-03-21", file:"aidanos26_1.py"},
    {name:"26.2", date:"2026-02-01", end:"2026-04-01", file:"aidanos26_2.py"},
    {name:"26.3", date:"2026-03-01", end:"2026-05-01", file:"aidanos26_3.py"},
    {name:"26.4", date:"2026-04-01", end:"2026-06-01", file:"aidanos26_4.py"}
];

// --- Build download cards ---
const container = document.getElementById("versions");
versions.forEach(v => {
    const div = document.createElement("div");
    div.className = "card";
    div.innerHTML = `
        <h2>AidanOS ${v.name}</h2>
        <p>Release: ${v.date} → End: ${v.end}</p>
        <button onclick="downloadFile('${v.file}')">Download</button>
    `;
    container.appendChild(div);
});

function downloadFile(filename) {
    const link = document.createElement("a");
    link.href = `http://localhost:8000/${filename}`;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// --- Build timeline chart ---
const ctx = document.getElementById('timelineChart').getContext('2d');

const chartData = {
    labels: versions.map(v => v.name),
    datasets: versions.map((v, i) => {
        const start = new Date(v.date);
        const end = new Date(v.end);
        return {
            label: v.name,
            data: [[start.getTime(), end.getTime()]], // floating bar
            backgroundColor: `rgba(${50 + i*50}, ${160 - i*30}, 67, 0.7)`,
            borderColor: `rgba(${50 + i*50}, ${160 - i*30}, 67, 1)`,
            borderWidth: 1
        };
    })
};

new Chart(ctx, {
    type: 'bar',
    data: chartData,
    options: {
        indexAxis: 'y',
        scales: {
            x: {
                type: 'time',
                time: { unit: 'month', tooltipFormat: 'MMM dd' },
                title: { display: true, text: 'Month' }
            },
            y: {
                type: 'category',
                labels: versions.map(v => v.name),
                title: { display: true, text: 'Version' }
            }
        },
        plugins: {
            tooltip: {
                callbacks: {
                    label: function(context) {
                        const start = new Date(context.raw[0]);
                        const end = new Date(context.raw[1]);
                        return `${context.dataset.label}: ${start.toISOString().slice(0,10)} → ${end.toISOString().slice(0,10)}`;
                    }
                }
            },
            legend: { display: false }
        }
    }
});
</script>

</body>
</html>