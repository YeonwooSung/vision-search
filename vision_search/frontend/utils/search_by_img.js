
async function searchByImg(img) {
    const formData = new FormData();
    formData.append("image", img);
    const response = await fetch("http://localhost:8000/search", {
        method: "POST",
        body: formData,
    });
}

async function searchByImgUrl(url) {
    const response = await fetch("http://localhost:8000/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
    });
}

async function searchByText(text) {
    const response = await fetch("http://localhost:8000/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
    });
}

module.exports = {
    searchByImg,
    searchByImgUrl,
    searchByText,
};