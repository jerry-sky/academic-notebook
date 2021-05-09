const imagesQuantity = 12;
let imagesLoadedQuantity = 0;

const imagesListElement = document.querySelector('.images');

// first, immediately load the low resolution image
for (let i = 1; i <= 12; i++) {
    imagesListElement.innerHTML += "<img src=\"img/low/img" + i + ".jpg\"/>"
}
/**
 * @type HTMLImageElement[]
 */
const images = document.querySelectorAll('.images > img');

// then for each image make a query for target resolution version
images.forEach((imageElement) => {
    const targetResImageURL = imageElement.src.replace('low/', '');

    const p = new Promise((resolve) => {
        const image = new Image();

        image.addEventListener('load', () => {
            resolve(image);
        });
        image.src = targetResImageURL;
    })

    p.then(() => {
        imageElement.src = targetResImageURL;
        imagesLoadedQuantity++;

        if(imagesLoadedQuantity === imagesQuantity) {
            document.querySelector('.loaded-message').removeAttribute('hidden');
            document.querySelector('.loading-message').setAttribute('hidden', '');
        }
    })

});
