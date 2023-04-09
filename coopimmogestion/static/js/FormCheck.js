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
        this.errorLog.className = "position-absolute bottom-0 form-submit-error m-1 text-danger"
        this.modalBody.append(this.errorLog);
    }
}