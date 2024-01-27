document.addEventListener("DOMContentLoaded", function () {
    var wordLimit = 20;

    var cards = document.querySelectorAll('.toggleCard');

    cards.forEach(function(card) {
        var element = card.querySelector('.card-text');
        var originalText = element.textContent.trim();

        element.textContent = originalText.split(' ').slice(0, wordLimit).join(' ');

        var btn = card.querySelector('.toggleButton');
        btn.addEventListener('click', function () {
            toggleText(element, originalText, btn, wordLimit);
        });
    });

    function toggleText(element, originalText, btn, wordLimit) {
        if (btn.textContent === "Read More") {
            element.textContent = originalText;
            btn.textContent = "See Less";
        } else {
            element.textContent = originalText.split(' ').slice(0, wordLimit).join(' ');
            btn.textContent = "Read More";
        }
    }
});