
function generateUniqueKey() {
    const unique_id = "id" + Math.random().toString(16).slice(2);
    return unique_id;
}

export default generateUniqueKey;
