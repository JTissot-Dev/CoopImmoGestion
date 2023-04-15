import {FormCheck} from "./FormCheck.js";

export class TenantFormCheck extends FormCheck{
    constructor(modalBody, form, submitButton) {
        super(modalBody, form, submitButton);
        this.emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    }

    // Form submit and data validation
    attachEventListeners(){
        this.submitButton.addEventListener("click", ()=>{
            let isValid = true;
            for (let element=0; element<this.form.elements.length; element++){
                if ((this.form[element].value === '' || this.form[element].value === null)
                    && this.form[element].name !== "additional_address"){
                    this.setErrorLog("Informations incomplètes");
                    isValid = false;
                }
                else if (!(this.emailRegex.test(this.form['email'].value))){
                    this.setErrorLog("Adresse e-mail invalide");
                    isValid = false;
                }
                else if (this.form['phone_number'].value.length !== 10){
                    this.setErrorLog("Numéro de téléphone érroné");
                    isValid = false;
                }
                else if (this.form['zip_code'].value.length !== 5){
                    this.setErrorLog("Code postal érroné");
                    isValid = false;
                }
            }
            if (isValid){
                this.form.submit();
            }
        })
    }
}