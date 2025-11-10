// Initialize Lucide Icons
document.addEventListener('DOMContentLoaded', function() {
    lucide.createIcons();
});

// Mobile Menu Toggle
const menuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

if (menuButton && mobileMenu) {
    menuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
}

// Countdown Timer Logic
function initCountdown() {
    const countdownElement = document.getElementById('countdown');
    
    if (!countdownElement) return;
    
    const countdown = () => {
        const targetDate = new Date("2026-11-03T00:00:00").getTime();
        const now = new Date().getTime();
        const distance = targetDate - now;

        // Time calculations for days, hours, minutes and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Output the result in elements
        const daysElement = document.getElementById("days");
        const hoursElement = document.getElementById("hours");
        const minutesElement = document.getElementById("minutes");
        const secondsElement = document.getElementById("seconds");
        
        if (daysElement) daysElement.innerText = days;
        if (hoursElement) hoursElement.innerText = hours;
        if (minutesElement) minutesElement.innerText = minutes;
        if (secondsElement) secondsElement.innerText = seconds;

        // If the count down is over, write some text 
        if (distance < 0) {
            clearInterval(interval);
            countdownElement.innerHTML = "<div class='col-span-2 md:col-span-4 text-3xl font-bold text-teal-600'>The Congress is Here!</div>";
        }
    };

    // Update the count down every 1 second
    const interval = setInterval(countdown, 1000);
    // Run on load
    countdown();
}

// Initialize countdown when page loads
if (document.getElementById('countdown')) {
    initCountdown();
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});
