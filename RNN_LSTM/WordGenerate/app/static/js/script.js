let index = 0;
let sentence = '';
let interval;

function startDisplaying() {
    interval = setInterval(displayChar, 200); // Display each character every 200ms
}

function displayChar() {
    const output = document.getElementById('generatedText');

    // Check if there are characters left to display
    if (index < fullSentence.length) {
        sentence += fullSentence[index]; // Append character to sentence
        output.textContent = sentence; // Update displayed content
        index++;
    } else {
        clearInterval(interval); // Stop the interval when done
    }
}

// Start displaying characters when the page is loaded
document.addEventListener("DOMContentLoaded", startDisplaying);
