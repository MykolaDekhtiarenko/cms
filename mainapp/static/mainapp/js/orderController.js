/**
 * Created by mykola.dekhtiarenko on 24.03.17.
 */
$(document).ready(function () {

    $('#order-btn').on('click', function () {

        $.ajax({
            beforeSend: function(xhr, settings) {
                            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", $("#csrfmiddlewaretoken").text());
                            }
                        },
            url: "/api/campaign/",
            type: "POST",
            data: prossesData(),
            contentType: "application/json",
            dataType: "json",
            success: function(data) {
                alert();
                window.location.href="/redirect";
            },
            error: function (request, status, error) {
                console.log(request.responseText);
            }


        });
    });
});


function prossesData() {
    campaign = {};
    campaign["subject"]=$('#subject').val();
    campaign["plannedBudget"]=$('#budget').val();
    campaign["description"]=$('#description').val();
    campaign["startDate"]=$('#startdate').val();
    campaign["endDate"]=$('#enddate').val();
    campaign["lastUpdateDate"]=$('#startdate').val();
    campaign["client"]=$('#client').val();
    campaign['moneySpent']=0;
    campaign["state"]="Замовлена";
    campaign["paymentDetails"]="Узгоджуються з менеджером після прийняття замовлення і підписання договору";
    var serviceOptions = [];
        $.each($("#service option:selected"), function(){
            serviceOptions.push($(this).val());
        });
    campaign["service"] = serviceOptions;
    return JSON.stringify(campaign);
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}