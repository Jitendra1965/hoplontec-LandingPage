const companyMenu = document.querySelector('.company-menu');
if (companyMenu) {
  document.addEventListener('click', (event) => {
    if (!companyMenu.contains(event.target)) companyMenu.open = false;
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && companyMenu.open) {
      companyMenu.open = false;
      companyMenu.querySelector('summary').focus();
    }
  });
}
