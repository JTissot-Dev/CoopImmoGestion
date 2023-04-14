import {FormCheck} from "./FormCheck.js";

export class ApartmentCreateFormCheck extends FormCheck{
    constructor(modalBody, form, submitButton) {
        super(modalBody, form, submitButton);
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
                else if (this.form['zip_code'].value.length !== 5){
                    this.setErrorLog("Code postal érroné");
                    isValid = false;
                }
            }
            if (isValid){
                this.form.submit();
            }
        })
        for (let element=0; element<this.form.elements.length; element++){
            if (this.form[element].name === 'outdoor'){
                this.form[element].addEventListener("change",()=>{
                    if (this.form[element].checked){
                        this.form[element].value = true;
                        console.log(this.form[element].value)
                    }
                    else{
                        this.form[element].value = false;
                        console.log(this.form[element].value)
                    }
                })
            }
        }
    }
}