$.validator.setDefaults({
    submitHandler:function () {
        document.forms.submit()
    }
});

$(document).ready(function() {

//    $.validator.addMethod("name_field", function (value, element) {
//        return this.optional(element) || /^[a-zA-Z]{2,20}$/i.test(value);
//    }, "This field is 2-20 characters");

    $("#studentForm").validate({

        rules: {

            last_name: {
                name_field: true,
                minlength: 2,
                maxlength: 20,
                required: true
            },

            last_name: {
                name_field: true,
                minlength: 2,
                maxlength: 20,
                required: true
            },

            password: {
                minlength: 6,
                maxlength: 20,
                password_field: true,
                required: true
            },

            e_mail: {
                required: true,
                email: true
            },

            phone: {
                minlength: 5,
                maxlength: 10,
                digits: true,
                required: true
            },

            find_about_us: {
                required: true
            },

            agree: {
                required: true
            }

        }
    });
});