
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







//profile Dropdown
const profilePic=document.querySelector('#profile-pic')
const profileDropdown=document.querySelector('#profile-dropdown')

profilePic.addEventListener('click',()=>{
  profileDropdown.classList.toggle('hidden')
})