var check_pasted_script = function () {
        source_script = {source: $("#source").val()};
        $.post("/", source_script, function (data, status) {

            $("#target").html(data);
        });
    };

var handleFiles = function (files) {
    var file = files[0];
    if (file) {
        var reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function (evt) {
            $("#source").html(evt.target.result);
            check_pasted_script();
        }
    }
};

$(document).ready(function () {
    $("#check").click(check_pasted_script);
});

