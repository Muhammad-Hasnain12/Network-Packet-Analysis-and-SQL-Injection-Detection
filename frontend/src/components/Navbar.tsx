import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-blue-900 text-white px-6 py-4 flex justify-between items-center shadow-lg">
      <Link href="/" className="text-2xl font-bold hover:text-blue-300">
        SQL Injection Detector
      </Link>
      <div className="space-x-6">
        <Link href="/" className="hover:text-blue-300 transition">Home</Link>
        <Link href="/upload" className="hover:text-blue-300 transition">Upload</Link>
        <Link href="/about" className="hover:text-blue-300 transition">About</Link>
      </div>
    </nav>
  );
}