import {FormCheck} from "./FormCheck.js";

export class AccountCreateFormCheck extends FormCheck{
    constructor(modalBody, form, submitButton) {
        super(modalBody, form, submitButton);
        this.emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        this.passwordRegex = /^(?=.*?[A-Z])(?=.*?[a-z]).{8,}$/;
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
                else if (this.form['password'].value !== this.form['password_check'].value){
                    this.setErrorLog("Veuillez saisir deux mots de passe identiques");
                    isValid = false;
                }
                else if (!(this.passwordRegex.test(this.form['password'].value))){
                    this.setErrorLog("Mot de passe: au moin une majuscule et > 8 caractères");
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