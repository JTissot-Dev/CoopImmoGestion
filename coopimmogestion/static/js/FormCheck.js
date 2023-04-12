export class FormCheck{
    constructor(modalBody, form, submitButton) {
        this.modalBody = modalBody;
        this.form = form;
        this.submitButton = submitButton;
        this.errorLog = document.createElement("span");
    }

    // Message error generator
    setErrorLog(message){
        this.errorLog.innerText = message;
        this.errorLog.className = "position-absolute bottom-0 ms-1 form-submit-error text-danger"
        this.modalBody.append(this.errorLog);
    }
}