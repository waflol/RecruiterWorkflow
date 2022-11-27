async function postRegister(url) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let form_data = new FormData();
    form_data.append('first_name', $('#id_first_name').val());
    form_data.append('last_name', $('#id_last_name').val())
    form_data.append('email', $('#id_email').val())
    form_data.append('password', $('#id_password').val())
    const response = await fetch(url,{
        method: 'POST',
        mode: 'same-origin',
        body: form_data,
        headers:{
            'X-CSRFToken': csrftoken
        }
    });
    if(response.status===409){
        Swal.fire({
            text: "Register Failed! Account is already registered!",
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: "Ok, got it!",
            customClass: {
                confirmButton: "btn btn-primary"
            }
        });
    }
    else if (response.status===201){
        console.log(response)
        Swal.fire({
            text: "Register Successful! Please activate on your email!!",
            icon: "success",
            buttonsStyling: false,
            confirmButtonText: "Ok, got it!",
            customClass: {
                confirmButton: "btn btn-primary"
            }
        }).then((result) => {
            window.location.replace("/login/");
        });
    }
    else{
        Swal.fire({
            text: "Some problem!",
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: "Ok, got it!",
            customClass: {
                confirmButton: "btn btn-primary"
            }
        });
    }
}
const form =document.querySelector("#kt_sign_up_form");
const submitButton = document.querySelector("#kt_sign_up_submit");
const passwordMeterElement = form.querySelector('[data-kt-password-meter="true"]')
let validator = FormValidation.formValidation(form,{
    fields:{
        "first_name":{
            validators:{
                notEmpty:{
                    message:"First Name is required"
                }
            }
        },
        "last_name":{
            validators:{
                notEmpty:{
                    message:"Last Name is required"
                }
            }
        },
        "username":{
            validators:{
                notEmpty:{
                    message:"Username is required"
                }
            }
        },
        "email":{
            validators:{
                regexp:{
                    regexp:/^[^\s@]+@[^\s@]+\.[^\s@]+$/,message:"The value is not a valid email address"
                },
                notEmpty:{
                    message:"Email address is required"
                }
            }
        },
        'password':{
            validators:{
                notEmpty:{
                    message:"The password is required"
                },
                callback:{
                    message:"Please enter valid password",
                    callback:
                        function(e){
                            let passwordMeter = KTPasswordMeter.getInstance(passwordMeterElement);
                            if(e.value.length>0) return 100===passwordMeter.getScore();
                        }
                }
            }
        },
        "confirm_password":{
            validators:{
                notEmpty:{
                    message:"The password confirmation is required"
                },
                identical:{
                    compare:function(){
                        return form.querySelector('[name="password"]').value
                    },
                    message:"The password and its confirm are not the same"
                }
            }},
        toc:{
            validators:{
                notEmpty:{
                    message:"You must accept the terms and conditions"
                }
            }
        }},
    plugins:{
        trigger:new FormValidation.plugins.Trigger({
            event:{
                password:!1
            }}),
        bootstrap:new FormValidation.plugins.Bootstrap5({
            rowSelector:".fv-row",
            eleValidClass:""
        })
    }
});

submitButton.addEventListener('click', function (e) {
    // Prevent default button action
    e.preventDefault();
    // Validate form before submit

    validator.revalidateField("password");
    validator.validate().then((status)=>{
        if (status === 'Valid') {

            // Show loading indication
            submitButton.setAttribute('data-kt-indicator', 'on');

            // Disable button to avoid multiple click
            submitButton.disabled = true;

            // Simulate form submission. For more info check the plugin's official documentation: https://sweetalert2.github.io/
            setTimeout((function(){
                submitButton.removeAttribute("data-kt-indicator");
                submitButton.disabled=false;
                postRegister('')
                    .then((function(result){
                        if(result.isConfirmed){
                            form.reset();
                            KTPasswordMeter.getInstance(passwordMeterElement).reset();
                        }
                    }))
            }),1500);
        }
        else{
            Swal.fire({
                text: "Sorry, looks like there are some errors detected, please try again.",
                icon:"error",
                buttonsStyling:!1,
                confirmButtonText: "Ok, got it!",
                customClass:{confirmButton:"btn btn-primary"}
            })
        }
    })
});
form.querySelector('input[name="password"]').addEventListener("input",(function(){
    this.value.length>0&&validator.updateFieldStatus("password","Valid")
}))