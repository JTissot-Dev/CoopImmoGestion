import { Pagination } from './Pagination.js';
import { AccountCreateFormCheck } from "./AccountCreateFormCheck.js";
import { AccountUpdateFormCheck } from "./AccountUpdateFormCheck.js";
import {ApartmentFormCheck} from "./ApartmentFormCheck.js";
import {TenantFormCheck} from "./TenantFormCheck.js";
import {RentalFormCheck} from "./RentalFormCheck.js";
import {InventoryFormCheck} from "./InventoryFormCheck.js";
import {PaymentFormCheck} from "./PaymentFormCheck.js";
import {RentReceiptFormCheck} from "./RentReceiptFormCheck.js";


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

// Apartment modal variables
const modalsBodyApartment = document.querySelectorAll('.modal-body-apartment');
const formsApartment = document.querySelectorAll('.form-apartment');
const submitsButtonApartment = document.querySelectorAll('.submit-apartment');

// Tenant modal variables
const modalsBodyTenant = document.querySelectorAll('.modal-body-tenant');
const formsTenant = document.querySelectorAll('.form-tenant');
const submitsButtonTenant = document.querySelectorAll('.submit-tenant');

// Rental modal variables
const modalsBodyRental = document.querySelectorAll('.modal-body-rental');
const formsRental = document.querySelectorAll('.form-rental');
const submitsButtonRental = document.querySelectorAll('.submit-rental');

// Inventory modal variables
const modalsBodyInventory = document.querySelectorAll('.modal-body-inventory');
const formsInventory = document.querySelectorAll('.form-inventory');
const submitsButtonInventory = document.querySelectorAll('.submit-inventory');

// Payment modal variables
const modalsBodyPayment = document.querySelectorAll('.modal-body-payment');
const formsPayment = document.querySelectorAll('.form-payment');
const submitsButtonPayment = document.querySelectorAll('.submit-payment');

const modalBodyRentReceipt = document.querySelector('.modal-body-rent-receipt');
const formRentReceipt = document.querySelector('.form-rent-receipt');
const submitButtonRentReceipt = document.querySelector('.submit-rent-receipt');

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

// Tenant Create/Update form submit
if (modalsBodyTenant, formsTenant, submitsButtonTenant){
    if (modalsBodyTenant.length, formsTenant.length, submitsButtonTenant.length){
        modalsBodyTenant.forEach((modalBodyTenant, index)=>{
            const formTenant = formsTenant[index];
            const submitButtonTenant = submitsButtonTenant[index];
            const tenantFormCheck = new TenantFormCheck(modalBodyTenant, formTenant, submitButtonTenant);
            tenantFormCheck.attachEventListeners();
        })
    }
}

// Rental Create/Update form submit
if (modalsBodyRental, formsRental, submitsButtonRental){
    if (modalsBodyRental.length, formsRental.length, submitsButtonRental.length){
        modalsBodyRental.forEach((modalBodyRental, index)=>{
            const formRental = formsRental[index];
            const submitButtonRental = submitsButtonRental[index];
            const rentalFormCheck = new RentalFormCheck(modalBodyRental, formRental, submitButtonRental);
            rentalFormCheck.attachEventListeners();
        })
    }
}

// Inventory Create/Update form submit
if (modalsBodyInventory, formsInventory, submitsButtonInventory){
    if (modalsBodyInventory.length, formsInventory.length, submitsButtonInventory.length){
        modalsBodyInventory.forEach((modalBodyInventory, index)=>{
            const formInventory = formsInventory[index];
            const submitButtonInventory = submitsButtonInventory[index];
            const inventoryFormCheck = new InventoryFormCheck(modalBodyInventory, formInventory, submitButtonInventory);
            inventoryFormCheck.attachEventListeners();
        })
    }
}

// Payment Create/Update form submit
if (modalsBodyPayment, formsPayment, submitsButtonPayment){
    if (modalsBodyPayment.length, formsPayment.length, submitsButtonPayment.length){
        modalsBodyPayment.forEach((modalBodyPayment, index)=>{
            const formPayment = formsPayment[index];
            const submitButtonPayment = submitsButtonPayment[index];
            const paymentFormCheck = new PaymentFormCheck(modalBodyPayment, formPayment, submitButtonPayment);
            paymentFormCheck.attachEventListeners();
        })
    }
}

if (modalBodyRentReceipt, formRentReceipt, submitButtonRentReceipt){
    const rentReceiptFormCheck = new RentReceiptFormCheck(modalBodyRentReceipt, formRentReceipt, submitButtonRentReceipt);
    rentReceiptFormCheck.attachEventListeners();
}