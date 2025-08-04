export default function About() {
  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold text-blue-900 mb-4">About This Project</h1>
      <p className="mb-4 text-gray-700">
        This project uses Artificial Intelligence (AI) to detect SQL injection attacks in network traffic. It analyzes network packet captures (PCAP files) and uses a machine learning model (Random Forest) to identify suspicious patterns that may indicate SQL injection attempts.
      </p>
      <p className="mb-4 text-gray-700">
        <strong>How it works:</strong> The backend extracts features from network payloads and uses a trained AI model to classify them as benign or malicious.
      </p>
      <p className="mb-4 text-gray-700">
        <strong>Technologies:</strong> React 18, Next.js, Tailwind CSS, Python, scikit-learn.
      </p>
      <p className="mb-4 text-gray-700">
        <strong>Author:</strong> Your Name
      </p>
    </div>
  );
}