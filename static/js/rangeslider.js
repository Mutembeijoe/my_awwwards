$(document).ready(function () {
    $('#usability_range').change(function (e) {
        $('#usability_value').text(this.value)
    });

    $('#design_range').change(function (e) {
        $('#design_value').text(this.value)

    });

    $('#content_range').change(function (e) {
        $('#content_value').text(this.value)

    });

    $('#rating_form').submit(function (e) {
        e.preventDefault();
        form = $('form')

        $.ajax({
            url: "/site/vote/",
            type: "POST",
            data: form.serialize(),
            dataType: "json",
            success: function (response) {
                alert(response['success'])
                location.reload()
            }
        });
    });
});

