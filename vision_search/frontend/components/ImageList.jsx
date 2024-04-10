import generateUniqueKey from "../utils/unique_key";

export default function ImageList({ images }) {
    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {images.map((image) => {
                const unique_key = generateUniqueKey();
                const img_alt = `Image description for ${image["_source"]["url"]}`;

                return (
                    <img
                        key={unique_key}
                        alt={img_alt}
                        className="w-full h-auto"
                        height="300"
                        src={image["_source"]["url"]}
                        style={{
                            aspectRatio: "450/300",
                            objectFit: "cover",
                        }}
                        width="450"
                    />
                );
            })}
        </div>
    );
}
