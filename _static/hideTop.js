if (window.innerWidth >= 992) {
    var navbar = document.getElementById('navbar-main');
    navbar.style.display = 'none';
} else {
    var navbar = document.getElementsByClassName('sidebar-header-items sidebar-primary__section') 
    navbar.style.display = 'none';
}