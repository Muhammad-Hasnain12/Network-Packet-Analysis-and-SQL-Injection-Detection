import Link from "next/link";

export default function Home() {
  return (
    <div className="text-center flex-1 flex flex-col justify-center">
      <h1 className="text-4xl font-bold text-blue-900 mb-4">Network Packet SQL Injection Detection</h1>
      <p className="text-lg text-gray-700 mb-8 max-w-2xl mx-auto">
        Upload your network packet capture (PCAP) files and detect potential SQL injection attacks using AI-powered analysis.
      </p>
      <Link
        href="/upload"
        className="inline-block bg-blue-700 text-white px-8 py-3 rounded-lg text-lg font-semibold hover:bg-blue-800 transition"
      >
        Get Started
      </Link>
    </div>
  );
}