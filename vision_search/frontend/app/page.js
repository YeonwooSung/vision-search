// import Image from "next/image";
import { RadioGroupItem, RadioGroup } from "@/components/ui/radio-group"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

import MenuIcon from "./icons/MenuIcon"
import PanelTopCloseIcon from "./icons/PanelTopCloseIcon"
import ImageList from "@/components/ImageList"


export default function Home() {
  return (
    <div className="bg-white">
      <header className="flex items-center justify-between p-6 border-b">
      <h1 className="text-4xl font-bold">Image Search Engine</h1>
        <MenuIcon className="text-2xl" />
      </header>
      <main className="flex flex-col lg:flex-row">
        <aside className="w-full lg:w-1/4 bg-gray-100 p-6 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Query by</h2>
            <PanelTopCloseIcon className="cursor-pointer" />
          </div>
          <div className="flex items-center">
            <RadioGroup defaultValue="text">
              <div className="flex items-center space-x-2">
                <RadioGroupItem id="query-text" value="text" />
                <Label htmlFor="query-text">text</Label>
              </div>
              <div className="flex items-center space-x-2">
                <RadioGroupItem id="query-image" value="image" />
                <Label htmlFor="query-image">image</Label>
              </div>
            </RadioGroup>
          </div>
          <div className="flex flex-col space-y-2">
            <Label htmlFor="search-input">Enter text/image URL here:</Label>
            <Input id="search-input" placeholder="two cats" />
          </div>
          <Button>Submit</Button>
        </aside>
      <section className="w-full lg:w-3/4 p-6 space-y-6">
        <h2 className="text-lg font-semibold">Results</h2>
        <ImageList images={[]} />
      </section>
      </main>
    </div>
  );
}
