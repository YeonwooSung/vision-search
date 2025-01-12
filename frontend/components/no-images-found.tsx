/** Add fonts into your Next.js project:

import { Inter } from 'next/font/google'

inter({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
export function NoImagesFound({ query }: { query: string }) {
  return (
    <div className="flex flex-col items-center justify-start p-16 h-[50vh]">
      <div className="text-center space-y-2">
        <h3 className="text-lg font-medium text-gray-700 dark:text-gray-300">
          No images found
        </h3>
        <p className="text-sm text-gray-500 dark:text-gray-400">
          There were no results (semantic or direct) found for the query &apos;
          {query}&apos;.
        </p>
      </div>
    </div>
  );
}
