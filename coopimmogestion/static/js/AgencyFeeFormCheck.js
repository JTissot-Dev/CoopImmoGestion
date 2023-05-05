import {FormCheck} from "./FormCheck.js";

export class AgencyFeeFormCheck extends FormCheck{
    constructor(modalBody, form, submitButton) {
        super(modalBody, form, submitButton);
    }

    // Form submit and data validation
    attachEventListeners(){
        this.submitButton.addEventListener("click", ()=>{
            let isValid = true;
            if (this.form['rate'].value === '' || this.form['rate'].value === null){
                this.setErrorLog("Informations incomplètes");
                isValid = false;
            }
            else if (this.form['rate'].value < 0.05 || this.form['rate'].value > 0.15){
                this.setErrorLog("Le taux doit être compris entre 0.05 et 0.15");
                isValid = false;
            }
            if (isValid){
                this.form.submit();
            }
        })
    }
}