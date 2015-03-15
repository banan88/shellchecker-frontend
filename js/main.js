
$(document).ready(function() {

    $("#check").click(function () {
        source_script={source: $("#source").val()};
        $.post("/", source_script,function (data, status) {

            $("#target").html(data);
        });
    });
});