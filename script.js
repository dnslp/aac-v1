import { items } from './items.js'; // Import items.js
console.log(items)
const emojiContainer = document.getElementById('emojiContainer');
const decreaseSizeButton = document.getElementById('decreaseSize');
const increaseSizeButton = document.getElementById('increaseSize');
const sortAscendingButton = document.getElementById('sortAscending');
const sortDescendingButton = document.getElementById('sortDescending');
const filterSystemSelect = document.getElementById('filterSystem');
const filterTagSelect = document.getElementById('filterTag');

let currentSize = 100;
const minSize = 50;
const maxSize = 200;

function populateFilterOptions() {
    const systems = [...new Set(items.map(item => item.system))];
    systems.forEach(system => {
        const option = document.createElement('option');
        option.value = system;
        option.textContent = system;
        filterSystemSelect.appendChild(option);
    });
}

function populateTagOptions() {
    const allTags = new Set(items.flatMap(item => item.tags || []));
    allTags.forEach(tag => {
        const option = document.createElement('option');
        option.value = tag;
        option.textContent = tag;
        filterTagSelect.appendChild(option);
    });
}

function renderItems(filterSystem = "all", filterTag = "all") {
    emojiContainer.innerHTML = '';
    const filteredItems = items.filter(item => {
        const systemMatch = filterSystem === "all" || item.system === filterSystem;
        const tagMatch = filterTag === "all" || (item.tags && item.tags.includes(filterTag));
        return systemMatch && tagMatch;
    });
    filteredItems.forEach(item => {
        const emojiItem = document.createElement('div');
        emojiItem.classList.add('emoji-item');
        emojiItem.setAttribute('data-label', item.label);

        if (item.type === 'emoji') {
            const emoji = document.createElement('div');
            emoji.classList.add('emoji');
            emoji.textContent = item.symbol;
            emojiItem.appendChild(emoji);
        } else if (item.type === 'image') {
            const img = document.createElement('img');
            img.src = item.symbol;
            img.alt = item.label;
            img.style.width = '80%';
            img.style.height = '80%';
            emojiItem.appendChild(img);
        }

        const label = document.createElement('div');
        label.classList.add('label');
        label.textContent = item.label;
        emojiItem.appendChild(label);

        emojiItem.addEventListener('click', () => {
            speakText(item.label);
        });

        emojiContainer.appendChild(emojiItem);
    });
}

function adjustSize(amount) {
    currentSize = Math.max(minSize, Math.min(maxSize, currentSize + amount));
    document.documentElement.style.setProperty('--emoji-size', `${currentSize}px`);
}

function sortEmojis(order) {
    items.sort((a, b) => {
        const labelA = a.label.toLowerCase();
        const labelB = b.label.toLowerCase();
        return order === 'asc' ? labelA.localeCompare(labelB) : labelB.localeCompare(labelA);
    });
    renderItems(filterSystemSelect.value, filterTagSelect.value);
}

decreaseSizeButton.addEventListener('click', () => adjustSize(-10));
increaseSizeButton.addEventListener('click', () => adjustSize(10));
sortAscendingButton.addEventListener('click', () => sortEmojis('asc'));
sortDescendingButton.addEventListener('click', () => sortEmojis('desc'));
filterSystemSelect.addEventListener('change', () => renderItems(filterSystemSelect.value, filterTagSelect.value));
filterTagSelect.addEventListener('change', () => renderItems(filterSystemSelect.value, filterTagSelect.value));

let voices = [];

function populateVoices() {
    voices = window.speechSynthesis.getVoices().filter(voice =>
        voice.lang.startsWith('en') &&
        (voice.lang.includes('US') || voice.lang.includes('GB') || voice.lang.includes('AU'))
    );
    const voiceSelect = document.getElementById('voiceSelect');
    voiceSelect.innerHTML = '';
    voices.forEach((voice, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = `${voice.name} (${voice.lang})`;
        voiceSelect.appendChild(option);
    });
}

function speakText(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    const selectedVoiceIndex = document.getElementById('voiceSelect').value;
    if (voices[selectedVoiceIndex]) {
        utterance.voice = voices[selectedVoiceIndex];
    }
    window.speechSynthesis.speak(utterance);
}

window.speechSynthesis.onvoiceschanged = populateVoices;

document.addEventListener('DOMContentLoaded', () => {
    populateFilterOptions();
    populateTagOptions();
    renderItems();
    populateVoices();
});
