import { CheckCircle, AlertTriangle, XCircle, FileText, Clock, Shield } from "lucide-react";

type ResultsProps = {
  result: any;
};

export default function Results({ result }: ResultsProps) {
  if (!result) return null;

  if (result.error) {
    return (
      <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-red-200 dark:border-red-800 p-8">
        <div className="flex items-center mb-4">
          <div className="w-12 h-12 bg-red-100 dark:bg-red-900 rounded-full flex items-center justify-center mr-4">
            <XCircle className="w-6 h-6 text-red-600 dark:text-red-400" />
          </div>
          <h2 className="text-2xl font-bold text-red-800 dark:text-red-400">Analysis Failed</h2>
        </div>
        <p className="text-red-600 dark:text-red-400 text-lg">{result.error}</p>
      </div>
    );
  }

  const isDetected = result.detected;
  const statusColor = isDetected ? 'red' : 'green';
  const StatusIcon = isDetected ? AlertTriangle : CheckCircle;

  return (
    <div className="space-y-6">
      {/* Main Result Card */}
      <div className={`bg-white dark:bg-gray-800 rounded-2xl shadow-xl border-2 ${
        isDetected 
          ? 'border-red-200 dark:border-red-800' 
          : 'border-green-200 dark:border-green-800'
      } p-8`}>
        <div className="flex items-center mb-6">
          <div className={`w-16 h-16 ${
            isDetected 
              ? 'bg-red-100 dark:bg-red-900' 
              : 'bg-green-100 dark:bg-green-900'
          } rounded-full flex items-center justify-center mr-6`}>
            <StatusIcon className={`w-8 h-8 ${
              isDetected 
                ? 'text-red-600 dark:text-red-400' 
                : 'text-green-600 dark:text-green-400'
            }`} />
          </div>
          <div>
            <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
              Analysis Complete
            </h2>
            <p className={`text-xl font-semibold ${
              isDetected 
                ? 'text-red-600 dark:text-red-400' 
                : 'text-green-600 dark:text-green-400'
            }`}>
              {isDetected ? 'SQL Injection Detected!' : 'No Threats Detected'}
            </p>
          </div>
        </div>

        {/* File Info */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
            <div className="flex items-center mb-2">
              <FileText className="w-5 h-5 text-gray-500 dark:text-gray-400 mr-2" />
              <span className="font-medium text-gray-900 dark:text-white">File</span>
            </div>
            <p className="text-gray-600 dark:text-gray-300 text-sm">{result.filename}</p>
          </div>
          
          <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
            <div className="flex items-center mb-2">
              <Shield className="w-5 h-5 text-gray-500 dark:text-gray-400 mr-2" />
              <span className="font-medium text-gray-900 dark:text-white">Size</span>
            </div>
            <p className="text-gray-600 dark:text-gray-300 text-sm">
              {(result.size / 1024).toFixed(2)} KB
            </p>
          </div>
          
          <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
            <div className="flex items-center mb-2">
              <Clock className="w-5 h-5 text-gray-500 dark:text-gray-400 mr-2" />
              <span className="font-medium text-gray-900 dark:text-white">Status</span>
            </div>
            <p className={`text-sm font-medium ${
              isDetected 
                ? 'text-red-600 dark:text-red-400' 
                : 'text-green-600 dark:text-green-400'
            }`}>
              {isDetected ? 'Threat Found' : 'Clean'}
            </p>
          </div>
        </div>

        {/* Details */}
        {result.details && result.details.length > 0 && (
          <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-6">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
              Analysis Details
            </h3>
            <ul className="space-y-2">
              {result.details.map((detail: string, index: number) => (
                <li key={index} className="flex items-start">
                  <CheckCircle className="w-5 h-5 text-blue-500 mr-3 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700 dark:text-gray-300">{detail}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Recommendations */}
        {isDetected && (
          <div className="mt-6 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-6">
            <h3 className="text-lg font-semibold text-red-800 dark:text-red-400 mb-3">
              Security Recommendations
            </h3>
            <ul className="space-y-2 text-red-700 dark:text-red-300">
              <li>• Immediately investigate the source of the malicious traffic</li>
              <li>• Review and update your web application's input validation</li>
              <li>• Consider implementing a Web Application Firewall (WAF)</li>
              <li>• Monitor your database logs for suspicious activity</li>
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}