/**
 * Created by mykola.dekhtiarenko on 08.04.17.
 */
/**
 * Created by mykola.dekhtiarenko on 24.03.17.
 */
$(document).ready(function () {
    $('#new-report-btn').on('click', function () {

        $.ajax({
            beforeSend: function(xhr, settings) {
                            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", $("#csrfmiddlewaretoken").text());
                            }
                        },
            url: "/api/report/",
            type: "POST",
            data: prossesData(),
            contentType: "application/json",
            dataType: "json",
            success: function(data) {
                alert();
                window.location.href="/api/analyst/campaign/"+forcampaign;
            },
            error: function (request, status, error) {
                console.log(request.responseText);
            }


        });
    });
});


function prossesData() {
    report = {};
    report["report"]=$('#report').val();
    report["campaign"]= forcampaign;
    report["employee"]= employee;
    report["date"]=$('#dated').val();
    alert(JSON.stringify(report));
    return JSON.stringify(report);
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}