const priceSlider = document.getElementById('price-range-slider');
const inputNumberStart = document.querySelector('.price-min');
const inputNumberEnd = document.querySelector('.price-max');
const catalogFilter = document.querySelector('.catalog-filter');
const categoryList = document.querySelector('.category-list');
const allInputReset = document.querySelector('.brands-checkbox-clean');

let amountLinks = categoryList.children.length - 8;


// Category list crop function
document.querySelector('.category-show-next')
    .style.display = amountLinks < 0 ? 'none' : 'block';

catalogFilter.addEventListener('click', (event) => {
    const target = event.target;
    
    if (!target.matches('.category-show-next')) return;
    
    if (target.textContent !== 'Свернуть') {
        categoryList.classList.remove('crop-height');
    } else {
        categoryList.classList.add('crop-height');
    }

    target.textContent = target.textContent !== 'Свернуть' 
        ? 'Свернуть' 
        : `Ещё ${amountLinks} категорий...`;
});

// no UI Slider config
noUiSlider.create(priceSlider, {
    start: [1000, 900000],
    connect: [false, true, false],
    step: 1,
    range: {
        'min': [1000],
        'max': [1000000]            }
});

priceSlider.noUiSlider.on("update", function (values, handle) {
    let value = values[handle];

    if (handle) {
        inputNumberEnd.value = Math.round(value);
    } else {
        inputNumberStart.value = Math.round(value);
    }
});

inputNumberStart.addEventListener("change", function () {
    priceSlider.noUiSlider.set([this.value, null]);
});

inputNumberEnd.addEventListener("change", function () {
    priceSlider.noUiSlider.set([null, this.value]);
});

// Reset inputs and checkbox
allInputReset.addEventListener('click', () => {
    inputNumberStart.value = '';
    inputNumberEnd.value = '';
    document.querySelectorAll('.brands-checkbox')
        .forEach(item => item.checked = false)
});
