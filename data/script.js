function toggleAccount() {
    const dropdown = document.getElementById("account-dropdown");
    dropdown.classList.toggle("open");
}

document.addEventListener("click", function(e) {
    const wrap = document.querySelector(".account-wrap");
    if (wrap && !wrap.contains(e.target)) {
        document.getElementById("account-dropdown").classList.remove("open");
    }
});

function openMenu() {
    document.getElementById("side-menu").classList.add("open");
    document.getElementById("menu-overlay").classList.add("open");
    document.getElementById("menu-open").style.display = "none";
}

function closeMenu() {
    document.getElementById("side-menu").classList.remove("open");
    document.getElementById("menu-overlay").classList.remove("open");
    document.getElementById("menu-open").style.display = "inline-flex";
}

function updateKyivClock() {
    const clock = document.getElementById("kyiv-clock");
    const date = document.getElementById("kyiv-date");

    if (!clock || !date) {
        return;
    }

    const now = new Date();

    const timeOptions = {
        timeZone: "Europe/Kyiv",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false
    };

    const dateOptions = {
        timeZone: "Europe/Kyiv",
        day: "2-digit",
        month: "2-digit",
        year: "numeric"
    };

    clock.textContent = new Intl.DateTimeFormat("uk-UA", timeOptions).format(now);
    date.textContent = new Intl.DateTimeFormat("uk-UA", dateOptions).format(now);
}

updateKyivClock();
setInterval(updateKyivClock, 1000);