export class Pagination {
  constructor(tbodyRows, pagesNumber, nextPage, previousPage) {
    this.tbodyRows = tbodyRows;
    this.pagesNumber = pagesNumber;
    this.nextPage = nextPage;
    this.previousPage = previousPage;
    this.currentPage = 1;
    this.rowsDisplay = [0, 4];
    this.pages = Math.ceil(tbodyRows.length / 5);
  }

  // Pagination display
  updatePaging() {
    this.pagesNumber.forEach((pageNumber) => {
      if (this.pages === 0){
        pageNumber.innerText = '1 / 1';
      }
      else{
        pageNumber.innerText = `${this.currentPage} / ${this.pages}`;
      }
    });
    this.tbodyRows.forEach((row, index) => {
      if (index >= this.rowsDisplay[0] && index <= this.rowsDisplay[1]) {
        row.className = "";
      } else {
        row.className = "d-none";
      }
    });
  }

  // Table navigation 5x5 rows
  attachEventListeners() {
    this.nextPage.addEventListener("click", () => {
      if (this.currentPage < this.pages) {
        this.rowsDisplay.forEach((row, index) => {
          this.rowsDisplay[index] += 5;
        });
        this.currentPage++;
        this.updatePaging();
      }
    });

    this.previousPage.addEventListener("click", () => {
      if (this.currentPage > 1) {
        this.rowsDisplay.forEach((row, index) => {
          this.rowsDisplay[index] -= 5;
        });
        this.currentPage--;
        this.updatePaging();
      }
    });
  }
}

