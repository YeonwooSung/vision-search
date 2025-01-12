"use client";

import { Input } from "@/components/ui/input";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
import { SearchIcon } from "lucide-react";
import { useRef, useState } from "react";
import { Button } from "./ui/button";
import { X } from "lucide-react";
import { useDebouncedCallback } from "use-debounce";
import { useSharedTransition } from "@/lib/hooks/use-shared-transition";


export function SearchBox({
  query,
  disabled,
}: {
  query?: string | null;
  disabled?: boolean;
}) {
  const { startTransition } = useSharedTransition();
  const inputRef = useRef<HTMLInputElement>(null);
  const [isValid, setIsValid] = useState(true);

  const searchParams = useSearchParams();
  const q = searchParams.get("q")?.toString() ?? "";
  const pathname = usePathname();

  const router = useRouter();

  const handleSearch = useDebouncedCallback((term: string) => {
    const params = new URLSearchParams(searchParams);

    if (term) {
      params.set("q", term);
    } else {
      params.delete("q");
    }
    startTransition &&
      startTransition(() => {
        router.push(`${pathname}?${params.toString()}`);
      });
  }, 300);

  const resetQuery = () => {
    startTransition &&
      startTransition(() => {
        router.push("/");
        if (inputRef.current) {
          inputRef.current.value = "";
          inputRef.current?.focus();
        }
      });
  };

  return (
    <div className="flex flex-col">
      <div className="w-full mx-auto mb-4">
        <div className="relative flex items-center space-x-2">
          <div className="relative w-full flex items-center">
            <SearchIcon className="absolute left-4 w-5 h-5 text-gray-500" />
            <Input
              disabled={disabled}
              ref={inputRef}
              defaultValue={query ?? ""}
              minLength={3}
              onChange={(e) => {
                const newValue = e.target.value;
                if (newValue.length > 2) {
                  setIsValid(true);
                  handleSearch(newValue);
                } else if (newValue.length === 0) {
                  handleSearch(newValue);
                  setIsValid(false);
                } else {
                  setIsValid(false);
                }
              }}
              className={
                "text-base w-full pl-12 pr-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:focus:ring-blue-500"
              }
              placeholder="Search..."
            />
            {q.length > 0 ? (
              <Button
                className="absolute right-2 text-gray-400 rounded-full h-8 w-8"
                variant="ghost"
                type="reset"
                size={"icon"}
                onClick={resetQuery}
              >
                <X height="20" width="20" />
              </Button>
            ) : null}
          </div>
        </div>
        {!isValid ? (
          <div className="text-xs pt-2 text-destructive">
            Query must be 3 characters or longer
          </div>
        ) : (
          <div className="h-6" />
        )}
      </div>
    </div>
  );
}
