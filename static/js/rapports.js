document.addEventListener('DOMContentLoaded', function() {
    const coutsLabels = JSON.parse(document.getElementById('coutsLabelsData').textContent);
    const coutsValues = JSON.parse(document.getElementById('coutsValuesData').textContent);
    const revenusLabels = JSON.parse(document.getElementById('revenusLabelsData').textContent);
    const revenusValues = JSON.parse(document.getElementById('revenusValuesData').textContent);

    new Chart(document.getElementById('coutsChart'), {
        type: 'bar',
        data: {
            labels: coutsLabels,
            datasets: [{
                label: 'Coût (fcfa)',
                data: coutsValues,
                backgroundColor: '#e8f2ec',
                borderColor: '#51946b',
                borderWidth: 2
            }]
        },
        options: { responsive: true }
    });

    new Chart(document.getElementById('revenusChart'), {
        type: 'bar',
        data: {
            labels: revenusLabels,
            datasets: [{
                label: 'Revenu (fcfa)',
                data: revenusValues,
                backgroundColor: '#e8f2ec',
                borderColor: '#39e079',
                borderWidth: 2
            }]
        },
        options: { responsive: true }
    });
});