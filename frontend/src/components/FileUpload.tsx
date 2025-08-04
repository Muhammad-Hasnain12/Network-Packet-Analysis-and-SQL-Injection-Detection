'use client';

import { useState } from "react";

type FileUploadProps = {
  onResult: (result: any) => void;
};

export default function FileUpload({ onResult }: FileUploadProps) {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(e.target.files?.[0] || null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      // Replace with your backend API endpoint
      const res = await fetch("/api/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setLoading(false);
      onResult(data);
    } catch (error) {
      setLoading(false);
      onResult({ error: "Failed to analyze file" });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        type="file"
        accept=".pcap"
        onChange={handleFileChange}
        className="block w-full text-sm text-gray-500
          file:mr-4 file:py-2 file:px-4
          file:rounded-full file:border-0
          file:text-sm file:font-semibold
          file:bg-blue-50 file:text-blue-700
          hover:file:bg-blue-100"
      />
      <button
        type="submit"
        className="bg-blue-700 text-white px-6 py-2 rounded hover:bg-blue-800 transition disabled:opacity-50"
        disabled={loading || !file}
      >
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </button>
    </form>
  );
}