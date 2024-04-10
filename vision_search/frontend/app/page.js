// import Image from "next/image";

import MenuIcon from "./icons/MenuIcon"
import ImageList from "@/components/ImageList"
import SearchAside from "@/components/SearchAside"


export default function Home() {
  return (
    <div className="bg-white">
      <header className="flex items-center justify-between p-6 border-b">
      <h1 className="text-4xl font-bold">Image Search Engine</h1>
        <MenuIcon className="text-2xl" />
      </header>
      <main className="flex flex-col lg:flex-row">
        <SearchAside />
      <section className="w-full lg:w-3/4 p-6 space-y-6">
        <h2 className="text-lg font-semibold">Results</h2>
        <ImageList images={[]} />
      </section>
      </main>
    </div>
  );
}
