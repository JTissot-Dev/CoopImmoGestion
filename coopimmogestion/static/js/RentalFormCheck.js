import {FormCheck} from "./FormCheck.js";

export class RentalFormCheck extends FormCheck{
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
                else if (this.form['start_date'].value >= this.form['end_date'].value){
                    this.setErrorLog("La fin du bail doit être ultérieure au début du bail");
                    isValid = false;
                }
            }
            if (isValid){
                this.form.submit();
            }
        })
    }
}