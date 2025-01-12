import type { Metadata } from "next";
import { GeistSans } from "geist/font/sans";
import "./globals.css";
import { cn } from "@/lib/utils";
import { TransitionProvider } from "@/lib/hooks/use-shared-transition";

export const metadata: Metadata = {
  title: "Semantic Image Search",
  description: "Semantic Image Search.",
  metadataBase: process.env.SVC_HOST_URL
    ? new URL(`https://${process.env.SVC_HOST_URL}`)
    : undefined,
};


export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={cn("font-sans antialiased", GeistSans.variable)}>
        <TransitionProvider>{children}</TransitionProvider>
      </body>
    </html>
  );
}
