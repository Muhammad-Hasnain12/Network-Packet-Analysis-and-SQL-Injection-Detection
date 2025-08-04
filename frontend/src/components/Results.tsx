type ResultsProps = {
  result: any;
};

export default function Results({ result }: ResultsProps) {
  if (!result) return null;
  return (
    <div className="mt-8 p-6 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-4 text-blue-800">Analysis Results</h2>
      {result.error ? (
        <div className="text-red-600">{result.error}</div>
      ) : (
        <div>
          <p className="mb-2">
            <span className="font-semibold">SQL Injection Detected:</span>{" "}
            <span className={result.detected ? "text-red-600 font-bold" : "text-green-600 font-bold"}>
              {result.detected ? "Yes" : "No"}
            </span>
          </p>
          {result.details && (
            <div>
              <h3 className="font-semibold">Details:</h3>
              <ul className="list-disc ml-6">
                {result.details.map((d: string, i: number) => (
                  <li key={i}>{d}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}