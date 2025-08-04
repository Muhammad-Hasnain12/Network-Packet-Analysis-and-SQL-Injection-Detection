'use client';

import { useState } from "react";
import FileUpload from "../../components/FileUpload";
import Results from "../../components/Results";

export default function Upload() {
  const [result, setResult] = useState<any>(null);

  return (
    <div>
      <h1 className="text-2xl font-bold text-blue-900 mb-6">Upload PCAP File</h1>
      <FileUpload onResult={setResult} />
      <Results result={result} />
    </div>
  );
}