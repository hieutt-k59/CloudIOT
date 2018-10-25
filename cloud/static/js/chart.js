window.chart = null;
$(document).on('change', '.graph-year-earning', function () {
    var year = $(this).val();
    $.get($('.graph-ajaxload-context').data('href'), { 'year': year, 'number': Math.floor(Math.random() * (1000000 - 10 + 1) + 10) }, function (response) {
        window.chart.data.labels = response.labels;
        window.chart.data.datasets[0].soldProductLabel = response.product_sold_label;
        window.chart.data.datasets[0].totalCommissionLabel = response.monthly_commission_label;
        window.chart.data.datasets[0].dataLabel = response.your_share_label;

        if (response.total_commission == 0) {
            window.chart.options.scales.yAxes[0].ticks.suggestedMin = 0;
            window.chart.options.scales.yAxes[0].ticks.suggestedMax = 140000;
        } else {
            window.chart.options.scales.yAxes[0].ticks.suggestedMin = '';
            window.chart.options.scales.yAxes[0].ticks.suggestedMax = '';
        }

        $.each(response.data, function (index, value) {
            window.chart.data.datasets[0].soldProduct[index] = value[2];
            window.chart.data.datasets[0].data[index] = Math.round(value[0]);
        });
        window.chart.update();
        $(".txt-total-commission-by-year").html(response.total_commission)
        $('.graph-ajaxload-context .inline-loader').hide();
    });
});
if ($('.graph-ajaxload-context').length > 0) {
    showLoader()
    $('.graph-year-earning').trigger('change');
    var ctx = $('#userEarningGraph');
    window.chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                soldProductLabel: '',
                soldProduct: [],
                dataLabel: '',
                data: [],
                backgroundColor: '#ADAEB1',
                hoverBackgroundColor: '#48C6B9'
            }]
        },
        options: {
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        maxTicksLimit: 8,
                        userCallback: function (value, index, values) {
                            value = value.toString();
                            value = value.split(/(?=(?:...)*$)/);
                            value = value.join(',');
                            var currency_code = ' ₩'
                            if ($('.graph-ajaxload-context').data('currency-code') && $('.graph-ajaxload-context').data('currency-code') != 'None') {
                                currency_code = $('.graph-ajaxload-context').data('currency-code')
                            }
                            return value + ' ' + currency_code;
                        }
                    },
                }]
            },
            tooltips: {
                mode: 'label',
                callbacks: {
                    label: function (tooltipItem, data) {
                        var soldProduct = data.datasets[tooltipItem.datasetIndex].soldProduct[tooltipItem.index];
                        var soldProductLabel = data.datasets[tooltipItem.datasetIndex].soldProductLabel;
                        var dataPro = data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
                        var dataLabel = data.datasets[tooltipItem.datasetIndex].dataLabel;
                        return [soldProductLabel + ':' + soldProduct, dataLabel + ':' + dataPro + ' ₩',];
                    }
                }
            }
        }
    });
}

$(document).on('click', '.showgraph', function (e) {
    $('.graph-year-earning').trigger('change');
});
/** Graph End Here */