import {FormCheck} from "./FormCheck.js";

export class RentReceiptFormCheck extends FormCheck{
    constructor(modalBody, form, submitButton) {
        super(modalBody, form, submitButton);
    }

    // Form submit and data validation
    attachEventListeners(){
        this.submitButton.addEventListener("click", ()=>{
            let isValid = true;
            for (let element=0; element<this.form.elements.length; element++){
                if (this.form[element].value === '' || this.form[element].value === null){
                    this.setErrorLog("Informations incomplètes");
                    isValid = false;
                }
            }
            if (isValid){
                this.form.submit();
            }
        })
    }
}