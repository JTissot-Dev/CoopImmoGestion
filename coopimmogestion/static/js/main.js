import { Pagination } from './Pagination.js';
import { AccountCreateFormCheck } from "./AccountCreateFormCheck.js";
import { AccountUpdateFormCheck } from "./AccountUpdateFormCheck.js";
import {ApartmentFormCheck} from "./ApartmentFormCheck.js";


// Table variables
const tbodyRows = document.querySelectorAll('tbody tr');
const pagesNumber = document.querySelectorAll('.page-number');
const nextPage = document.querySelector('.next-page');
const previousPage = document.querySelector('.previous-page');

// Create user account modal variables
const modalBodyCreateAccount = document.querySelector('.modal-body-create-user');
const formCreateAccount = document.querySelector('.form-create-account');
const submitButtonCreateAccount = document.querySelector('.submit-create-user');

// Update user account modal variables
const modalsBodyUpdateAccount = document.querySelectorAll('.modal-body-update-user');
const formsUpdateAccount = document.querySelectorAll('.form-update-account');
const submitsButtonUpdateAccount = document.querySelectorAll('.submit-update-user');

// Create apartment modal variables
const modalsBodyApartment = document.querySelectorAll('.modal-body-apartment');
const formsApartment = document.querySelectorAll('.form-apartment');
const submitsButtonApartment = document.querySelectorAll('.submit-apartment');

// Table display
if (tbodyRows, pagesNumber, nextPage, previousPage){
    const pagination = new Pagination(tbodyRows, pagesNumber, nextPage, previousPage);
    pagination.updatePaging();
    pagination.attachEventListeners();
}

// Create user account form submit
if (modalBodyCreateAccount, formCreateAccount, submitButtonCreateAccount){
    const accountCreateFormCheck = new AccountCreateFormCheck(modalBodyCreateAccount, formCreateAccount, submitButtonCreateAccount);
    accountCreateFormCheck.attachEventListeners();
}

// Update user account form submit
if (modalsBodyUpdateAccount.length, formsUpdateAccount.length, submitsButtonUpdateAccount.length){
    modalsBodyUpdateAccount.forEach((modalBodyUpdateAccount, index)=>{
        const formUpdateAccount = formsUpdateAccount[index];
        const submitButtonUpdateAccount = submitsButtonUpdateAccount[index];
        const accountUpdateFormCheck = new AccountUpdateFormCheck(modalBodyUpdateAccount, formUpdateAccount, submitButtonUpdateAccount);
        accountUpdateFormCheck.attachEventListeners();
    })
}

// Apartment Create/Update form submit
if (modalsBodyApartment, formsApartment, submitsButtonApartment){
if (modalsBodyApartment.length, formsApartment.length, submitsButtonApartment.length){
    modalsBodyApartment.forEach((modalBodyApartment, index)=>{
        const formApartment = formsApartment[index];
        const submitButtonApartment = submitsButtonApartment[index];
        const apartmentFormCheck = new ApartmentFormCheck(modalBodyApartment, formApartment, submitButtonApartment);
        apartmentFormCheck.attachEventListeners();
    })
}
}


