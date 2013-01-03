$.validator.setDefaults({
    submitHandler:function () {
        document.forms.submit()
    }
});

$(document).ready(function() {

//    $.validator.addMethod("name_field", function (value, element) {
//        return this.optional(element) || /^[a-zA-Z]{2,20}$/i.test(value);
//    }, "This field is 2-20 characters");

//    $.validator.addMethod("password_field", function (value, element) {
//        return this.optional(element) || /^[a-zA-Z0-9]{6,20}$/i.test(value);
//    }, "Password is 6-20 characters");
//
//    $.validator.addMethod("phone", function (value, element) {
//        return this.optional(element) || /^[0-9]{5,10}$/i.test(value);
//    }, "Phone is 5-10 numbers");

    $("#studentForm").validate({

        rules: {
            first_name: {
//                minlength: 2,
//                maxlenght: 7,
                name_field: true,
                required: true
            },

            last_name: {
//                name_field: true,
                required: true
            },

            password: {
                password_field: true,
                required: true
            },

            e_mail: {
                required: true,
                email: true
            },

            phone: {
                digits: true,
                required: true
            },

            find_about_us: {
                required: true
            },
            agree: "required"
        },
        messages: {

//            password: {
//                required: "Please provide a password"
//            },
//
//            email: "Please enter a valid email address",
//
//            find_about_us: "Please select",
//
//            agree: "Please accept"
        }
    });
});