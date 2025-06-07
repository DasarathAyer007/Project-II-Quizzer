
//SideBar Start
const sideBar = document.querySelector("#side-bar");
const dropdowns = sideBar.querySelectorAll(".dropdown");

dropdowns.forEach((element) => {
  element.addEventListener("click", () => {
    dropdowns.forEach((otherelement) => {
      if (
        otherelement != element &&
        !otherelement.nextElementSibling.classList.contains("hidden")
      ) {
        toggleSubMenu(otherelement);
      }
    });
    toggleSubMenu(element);
  });
});

const sidebarClose = document.querySelector("#sidebar-close");

sidebarClose.addEventListener("click", () => {
  toogleSideBar();
});

function toogleSideBar() {
  dropdowns.forEach((element) => {
    if (!element.nextElementSibling.classList.contains("hidden")) {
      toggleSubMenu(element);
    }
  });

  sidebarClose.classList.toggle("rotate-180");
  sideBar.classList.toggle("w-60");
  sideBar.classList.toggle("w-11");
  sideBar.classList.toggle("px-3");
}

function toggleSubMenu(button) {
  if (sideBar.classList.contains("w-11")) {
    toogleSideBar();
  }

  button.nextElementSibling.classList.toggle("hidden");
  button.lastElementChild.classList.toggle("rotate-180");
}


//Sidebar End




