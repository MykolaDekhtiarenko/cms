/**
 * Created by mykola.dekhtiarenko on 31.03.17.
 */

function prossesClientData() {
    client = {};
    client["edrpou"]=$('#edrpou').val();
    client["contactPersone"]=$('#first_name').val()+" "+$('#last_name').val();
    client["phone"]=$('#phone').val();
    client["address"]=$('#address').val();
    client["activity"]=$('#activity').val();

    user = {};
    user["username"]=$('#username').val();
    user["password"]=$('#password').val();
    user["email"]=$('#email').val();
    user["first_name"]=$('#first_name').val();
    user["last_name"]=$('#last_name').val();

    client["user"]=user;
    return JSON.stringify(client);
}

function registerOnClick() {
    var client = prossesClientData();
    registerClient(client);

}

function registerClient(client) {
     $.ajax({
            beforeSend: function(xhr, settings) {
                            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", $("input[name=csrfmiddlewaretoken]").val());
                            }
                        },
            url: "/api/client/",
            type: "POST",
            data: client,
            contentType: "application/json",
            dataType: "json",
            success: function(data) {
               alert("Success!");
               window.location.href="/login";

            },
            error: function (request, status, error) {
                console.log(request.responseText);
            }


        });

}



function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}