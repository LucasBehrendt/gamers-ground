// Handle sort selector inputs & reload page
document.getElementById('sort-selector').onchange = function() {
    let selector = this.value;
    let currentUrl = new URL(window.location);

    let selectedValue = selector;
    if (selectedValue != 'reset') {
        let sort = selectedValue.split('_')[0];
        let direction = selectedValue.split('_')[1];

        currentUrl.searchParams.set('sort', sort);
        currentUrl.searchParams.set('direction', direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');

        window.location.replace(currentUrl);
    }
};