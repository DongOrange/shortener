export function shortUrlApp() {
    return {
        copyToClipboard() {
            const shortUrl = document.getElementById('shortUrl');
            shortUrl.select();
            document.execCommand('copy');
            alert('短網址已複製！');
        }
    };
}

document.addEventListener('alpine:init', () => {
    Alpine.data('shortUrlApp', shortUrlApp);
});