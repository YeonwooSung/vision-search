import { RadioGroupItem, RadioGroup } from "@/components/ui/radio-group"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

import PanelTopCloseIcon from "./icons/PanelTopCloseIcon"


export default function SearchAside() {
    return (
        <aside className="w-full lg:w-1/4 bg-gray-100 p-6 space-y-4">
            <div className="flex items-center justify-between">
                <h2 className="text-lg font-semibold">Query by</h2>
                <PanelTopCloseIcon className="cursor-pointer" />
            </div>

            {/* radio button group to select search query type */}
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
                    <div className="flex items-center space-x-2">
                        <RadioGroupItem id="query-image" value="image-url" />
                        <Label htmlFor="query-image">image</Label>
                    </div>
                </RadioGroup>
            </div>

            {/* input field to enter search query */}
            <div className="flex flex-col space-y-2">
                <Label htmlFor="search-input">Enter text here:</Label>
                <Input id="search-input" placeholder="two cats" />
            </div>

            {/* TODO need to add input field for image query (display=none/flex based on radiobutton) */}
            <div className="flex flex-col space-y-2 hidden">
                <Label htmlFor="search-image">Enter image URL here:</Label>
                <Input id="search-image" placeholder="https://example.com/image.jpg" />
            </div>

            {/* TODO need to add input field for image url input (display=none/flex based on radiobutton) */}
            <div className="flex flex-col space-y-2 hidden">
                <Label htmlFor="search-image-url">Enter image URL here:</Label>
                <Input id="search-image-url" placeholder="https://example.com/image.jpg" />
            </div>

            <Button>Submit</Button>
        </aside>
    );
}
