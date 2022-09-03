// Sets country field on profile page to correct colour values
let countrySelected = document.getElementById('default_country');
if (!countrySelected.value) {
    countrySelected.style.color = 'grey';
}
countrySelected.onchange = function() {
    countrySelected = this.value;
    if (!countrySelected) {
        this.style.color = 'grey';
    } else {
        this.style.color = '#212529';
    }
}