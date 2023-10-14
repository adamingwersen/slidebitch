import "./globals.css";

import { Inter } from "next/font/google";

import { Toaster } from "@/components/ui/toaster";
import { cn } from "@/lib/utils";

import type { Metadata } from "next";
const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Slidebitch",
  description:
    "Support your arguments with citations from the top consulting firms",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={cn(inter.className)}>
        <link rel="icon" href="/favicon.ico" sizes="any" />
        {children}
        <Toaster />
      </body>
    </html>
  );
}
