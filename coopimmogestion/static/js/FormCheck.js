export class FormCheck{
    constructor(modalBody, form, submitButton) {
        this.modalBody = modalBody;
        this.form = form;
        this.submitButton = submitButton;
        this.errorLog = document.createElement("span");
        this.loading_spinner = document.createElement('div');
    }

    // Message error generator
    setErrorLog(message){
        this.errorLog.innerText = message;
        this.errorLog.className = "position-absolute bottom-0 ms-1 form-submit-error text-danger"
        this.modalBody.append(this.errorLog);
    }

    // Create loading element
    setLoadingSpinner(){
        const span_spinner = document.createElement('span');
        // Define bootstrap style
        this.loading_spinner.className = "position-absolute start-50 bottom-50 top-50 spinner-border text-custom";
        this.loading_spinner.ariaRoleDescription = "status";
        span_spinner.className = "visually-hidden";

        this.loading_spinner.append(span_spinner)
        this.modalBody.append(this.loading_spinner);
    }
}