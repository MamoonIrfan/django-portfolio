// =============================
// Portfolio Website
// Muhammad Mamoon Irfan
// =============================

// Welcome Message

window.onload = function () {

    console.log("Welcome to Muhammad Mamoon Irfan's Portfolio Website.");

};


// Contact Form

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function (event) {

        event.preventDefault();

        alert("Thank you! Your message has been submitted successfully.");

        form.reset();

    });

}