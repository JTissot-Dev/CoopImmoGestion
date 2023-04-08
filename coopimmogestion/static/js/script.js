// Table variables
const tbody = document.querySelector('tbody');
const tbodyRows = document.querySelectorAll('tbody tr');
const pagesNumber = document.querySelectorAll('.page-number');
const nextPage = document.querySelector('.next-page');
const previousPage = document.querySelector('.previous-page');
let currentPage = 1;
let rowsDisplay = [0, 4];
let pages = Math.ceil(tbodyRows.length / 5);


// Table display
// Table paging function
function updatePaging(){
    pagesNumber.forEach((pageNumber)=>{
    pageNumber.innerText = `${currentPage} / ${pages}`;
    })
    tbodyRows.forEach((row, index)=>{
        if (index >= rowsDisplay[0] && index <= rowsDisplay[1]){
            row.className = "";
        }
        else{
            row.className = "d-none";
        }
    })
}

// Manage table display 5 rows
if (tbodyRows){
    updatePaging();

    nextPage.addEventListener('click',()=>{
        if (currentPage < pages){
            rowsDisplay.forEach((row, index)=>{
                rowsDisplay[index] += 5;
            })
            currentPage ++;
            updatePaging();
        }
    })

    previousPage.addEventListener('click',()=>{
        if (currentPage > 1){
            rowsDisplay.forEach((row, index)=>{
                rowsDisplay[index] -= 5;
            })
            currentPage --;
            updatePaging();
        }
    })
}



