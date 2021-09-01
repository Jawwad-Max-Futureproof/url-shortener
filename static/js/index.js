const copyButton = document.querySelector('svg');
const link = document.querySelector('a').href;
const toolTip = document.querySelector('div span');

function copyToClipboard() {
	navigator.clipboard.writeText(link);
}

function handleClick() {
	copyToClipboard();
	toolTip.classList.add('visible');
	setTimeout(() => toolTip.classList.remove('visible'), 2000);
}

copyButton.addEventListener('click', handleClick);
