
//SideBar Start


//Sidebar End




//sidenav for mobile

const openSidenav=document.querySelector('#open-sidenav')
const closeSidenav=document.querySelector('#close-sidenav')
const sideNav=document.querySelector('#side-nav')

openSidenav.addEventListener('click',()=>{
  sideNav.classList.toggle('hidden')
})


closeSidenav.addEventListener('click',()=>{
  sideNav.classList.toggle('hidden')
})


function toogelSidenavDropdown(element){
  element.nextElementSibling.classList.toggle("hidden")
}







//profile Dropdown
const profilePic = document.querySelector('#profile-pic');
const profileDropdown = document.querySelector('#profile-dropdown');

profilePic.addEventListener('click', (event) => {
  profileDropdown.classList.toggle('hidden');
  event.stopPropagation();
});

document.addEventListener('click', (event) => {
  if (!profileDropdown.contains(event.target) && event.target !== profilePic) {
    profileDropdown.classList.add('hidden');
  }
});





