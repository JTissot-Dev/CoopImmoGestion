import {FormCheck} from "./FormCheck.js";

export class PaymentFormCheck extends FormCheck{
    constructor(modalBody, form, submitButton) {
        super(modalBody, form, submitButton);
    }

    // Form submit and data validation
    attachEventListeners(){
        this.submitButton.addEventListener("click", ()=>{
            let isValid = true;
            if (this.form['type_payment'].value === "Dépôt de garantie"){
                for (let element=0; element<this.form.elements.length; element++){
                    if ((this.form[element].value === '' || this.form[element].value === null)
                        && this.form[element].name !== "origin"){
                        this.setErrorLog("Informations incomplètes");
                        isValid = false;
                    }
                }
            }
            else{
                for (let element=0; element<this.form.elements.length; element++){
                    if (this.form[element].value === '' || this.form[element].value === null){
                        this.setErrorLog("Informations incomplètes");
                        isValid = false;
                    }
                }
            }
            if (isValid){
                this.form.submit();
            }
        })
    }
}