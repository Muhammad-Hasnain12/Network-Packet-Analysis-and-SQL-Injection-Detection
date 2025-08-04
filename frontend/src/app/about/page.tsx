import { Brain, Shield, Zap, Users, Award, Target } from "lucide-react";

export default function About() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-blue-50 via-white to-purple-50 dark:from-gray-900 dark:via-gray-900 dark:to-gray-800 py-20">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="mb-8 flex justify-center">
            <div className="p-4 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl shadow-lg">
              <Shield className="w-16 h-16 text-white" />
            </div>
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-6">
            About SQLGuard AI
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto leading-relaxed">
            Advanced AI-powered cybersecurity solution designed to detect and prevent SQL injection attacks 
            through intelligent network packet analysis and machine learning.
          </p>
        </div>
      </section>

      {/* Mission Section */}
      <section className="py-16 bg-white dark:bg-gray-900">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-6">
                Our Mission
              </h2>
              <p className="text-lg text-gray-600 dark:text-gray-400 mb-6">
                We're dedicated to protecting web applications and databases from SQL injection attacks 
                using cutting-edge artificial intelligence and machine learning technologies.
              </p>
              <p className="text-lg text-gray-600 dark:text-gray-400 mb-8">
                Our solution combines deep packet inspection with advanced pattern recognition to 
                identify malicious SQL injection attempts in real-time, providing organizations with 
                the tools they need to secure their digital assets.
              </p>
              <div className="grid grid-cols-2 gap-6">
                <div className="text-center">
                  <div className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">99.5%</div>
                  <div className="text-gray-600 dark:text-gray-400">Accuracy Rate</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold text-purple-600 dark:text-purple-400 mb-2">1000+</div>
                  <div className="text-gray-600 dark:text-gray-400">Threats Detected</div>
                </div>
              </div>
            </div>
            <div className="bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl p-8 text-white">
              <h3 className="text-2xl font-bold mb-4">Why Choose SQLGuard AI?</h3>
              <ul className="space-y-3">
                <li className="flex items-center">
                  <Brain className="w-5 h-5 mr-3" />
                  Advanced machine learning algorithms
                </li>
                <li className="flex items-center">
                  <Zap className="w-5 h-5 mr-3" />
                  Real-time threat detection
                </li>
                <li className="flex items-center">
                  <Shield className="w-5 h-5 mr-3" />
                  Comprehensive security analysis
                </li>
                <li className="flex items-center">
                  <Target className="w-5 h-5 mr-3" />
                  High precision with low false positives
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Technology Section */}
      <section className="py-16 bg-gray-50 dark:bg-gray-800">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-4">
              Technology Stack
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
              Built with modern technologies and industry best practices
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {/* Frontend */}
            <div className="bg-white dark:bg-gray-900 p-6 rounded-xl shadow-lg">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Frontend</h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>• React 19 with Next.js 15</li>
                <li>• TypeScript for type safety</li>
                <li>• Tailwind CSS for styling</li>
                <li>• Responsive design</li>
              </ul>
            </div>

            {/* Backend */}
            <div className="bg-white dark:bg-gray-900 p-6 rounded-xl shadow-lg">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Backend</h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>• Python for data processing</li>
                <li>• PyShark for packet analysis</li>
                <li>• Scapy for network manipulation</li>
                <li>• RESTful API design</li>
              </ul>
            </div>

            {/* AI/ML */}
            <div className="bg-white dark:bg-gray-900 p-6 rounded-xl shadow-lg">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">AI & Machine Learning</h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>• scikit-learn Random Forest</li>
                <li>• Feature extraction algorithms</li>
                <li>• Pattern recognition</li>
                <li>• Continuous model training</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white dark:bg-gray-900">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-4">
              Key Features
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
              Comprehensive security features designed for modern threats
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="flex items-start space-x-4">
              <div className="w-12 h-12 bg-blue-100 dark:bg-blue-900 rounded-lg flex items-center justify-center flex-shrink-0">
                <Brain className="w-6 h-6 text-blue-600 dark:text-blue-400" />
              </div>
              <div>
                <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                  Intelligent Pattern Recognition
                </h3>
                <p className="text-gray-600 dark:text-gray-400">
                  Advanced algorithms that learn and adapt to new SQL injection techniques and attack vectors.
                </p>
              </div>
            </div>

            <div className="flex items-start space-x-4">
              <div className="w-12 h-12 bg-purple-100 dark:bg-purple-900 rounded-lg flex items-center justify-center flex-shrink-0">
                <Zap className="w-6 h-6 text-purple-600 dark:text-purple-400" />
              </div>
              <div>
                <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                  Real-time Processing
                </h3>
                <p className="text-gray-600 dark:text-gray-400">
                  Lightning-fast analysis with sub-second response times for immediate threat detection.
                </p>
              </div>
            </div>

            <div className="flex items-start space-x-4">
              <div className="w-12 h-12 bg-green-100 dark:bg-green-900 rounded-lg flex items-center justify-center flex-shrink-0">
                <Shield className="w-6 h-6 text-green-600 dark:text-green-400" />
              </div>
              <div>
                <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                  Comprehensive Security
                </h3>
                <p className="text-gray-600 dark:text-gray-400">
                  Multi-layered security approach with deep packet inspection and payload analysis.
                </p>
              </div>
            </div>

            <div className="flex items-start space-x-4">
              <div className="w-12 h-12 bg-orange-100 dark:bg-orange-900 rounded-lg flex items-center justify-center flex-shrink-0">
                <Award className="w-6 h-6 text-orange-600 dark:text-orange-400" />
              </div>
              <div>
                <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                  High Accuracy
                </h3>
                <p className="text-gray-600 dark:text-gray-400">
                  99.5% detection accuracy with minimal false positives for reliable security monitoring.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-16 bg-gradient-to-r from-blue-600 to-purple-600">
        <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-white mb-6">
            Ready to Secure Your Applications?
          </h2>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Join thousands of organizations already protecting their systems with SQLGuard AI.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a
              href="/upload"
              className="inline-flex items-center justify-center bg-white text-blue-600 font-semibold py-3 px-8 rounded-lg hover:bg-gray-100 transition-all duration-300 transform hover:scale-105 shadow-lg"
            >
              Start Free Analysis
            </a>
            <a
              href="mailto:contact@sqlguard.ai"
              className="inline-flex items-center justify-center bg-transparent border-2 border-white text-white font-semibold py-3 px-8 rounded-lg hover:bg-white hover:text-blue-600 transition-all duration-300"
            >
              Contact Us
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}