export default function Navbar() {
  return (
    <nav className="bg-blue-900 text-white px-6 py-4 flex justify-between items-center shadow-lg">
      <div className="text-2xl font-bold">SQL Injection Detector</div>
      <div className="space-x-6">
        <a href="/" className="hover:text-blue-300">Home</a>
        <a href="/upload" className="hover:text-blue-300">Upload</a>
        <a href="/about" className="hover:text-blue-300">About</a>
      </div>
    </nav>
  );
}