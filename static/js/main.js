// Get the necessary DOM elements
const switchCtn = document.querySelector("#switch-cnt");
const switchC1 = document.querySelector("#switch-c1");
const switchC2 = document.querySelector("#switch-c2");
const switchCircle = document.querySelectorAll(".switch__circle");
const switchBtn = document.querySelectorAll(".switch-btn");
const aContainer = document.querySelector("#a-container");
const bContainer = document.querySelector("#b-container");
const allButtons = document.querySelectorAll(".submit");

// Prevent default form submission
const getButtons = (e) => {
  e.preventDefault();
  // Handle form submission logic here
};

// Switch between forms
const changeForm = (e) => {
  switchCtn.classList.add("is-gx");
  setTimeout(() => {
    switchCtn.classList.remove("is-gx");
  }, 1500);

  switchCtn.classList.toggle("is-txr");
  switchCircle[0].classList.toggle("is-txr");
  switchCircle[1].classList.toggle("is-txr");

  switchC1.classList.toggle("is-hidden");
  switchC2.classList.toggle("is-hidden");
  aContainer.classList.toggle("is-txl");
  bContainer.classList.toggle("is-txl");
  bContainer.classList.toggle("is-z200");
};

// Attach event listeners
const mainF = () => {
  allButtons.forEach((button) => {
    button.addEventListener("click", getButtons);
  });

  switchBtn.forEach((btn) => {
    btn.addEventListener("click", changeForm);
  });
};

window.addEventListener("load", mainF);
