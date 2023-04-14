import { Pagination } from './Pagination.js';
import { AccountCreateFormCheck } from "./AccountCreateFormCheck.js";
import { AccountUpdateFormCheck } from "./AccountUpdateFormCheck.js";
import {ApartmentCreateFormCheck} from "./ApartmentCreateFormCheck.js";


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
const modalBodyCreateApartment = document.querySelector('.modal-body-create-apartment');
const formCreateApartment = document.querySelector('.form-create-apartment');
const submitButtonCreateApartment = document.querySelector('.submit-create-apartment');

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

// Create user account form submit
if (modalBodyCreateApartment, formCreateApartment, submitButtonCreateApartment){
    const apartmentCreateFormCheck = new ApartmentCreateFormCheck(modalBodyCreateApartment, formCreateApartment, submitButtonCreateApartment);
    apartmentCreateFormCheck.attachEventListeners();
}


