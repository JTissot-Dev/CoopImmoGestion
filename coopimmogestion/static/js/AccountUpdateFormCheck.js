import {FormCheck} from "./FormCheck.js";

export class AccountUpdateFormCheck extends FormCheck{
    constructor(modalBody, form, submitButton) {
        super(modalBody, form, submitButton);
    }

    // Form submit and data validation
    attachEventListeners(){
        this.submitButton.addEventListener("click", ()=>{
            let isValid = true;
            for (let element=0; element<this.form.elements.length; element++){
                console.log(this.form[element].type)
                if ((this.form[element].value === '' || this.form[element].value === null)
                    && this.form[element].name !== "additional_address"){
                    this.setErrorLog("Informations incomplètes");
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