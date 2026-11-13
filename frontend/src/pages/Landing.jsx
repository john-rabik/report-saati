import React from "react";
import { Link } from "react-router-dom";

function Landing() {
  return (
    <div className="bg-gray-100 min-h-screen flex flex-col">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-6xl mx-auto flex items-center justify-between py-4 px-6">
          <h1 className="text-2xl font-bold text-indigo-700">ReportSaathi</h1>
          <nav className="space-x-4">
            <Link to="/" className="text-gray-600 hover:text-indigo-600 transition">Home</Link>
            <Link to="/dashboard" className="text-gray-600 hover:text-indigo-600 transition">Upload</Link>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="flex-1 bg-white py-12">
        <div className="max-w-6xl mx-auto px-6 flex flex-col md:flex-row items-center">
          {/* Text side */}
          <div className="md:w-1/2">
            <h2 className="text-4xl md:text-5xl font-extrabold text-gray-800 mb-4">
              Explain lab reports in simple language
            </h2>
            <p className="text-lg text-gray-600 mb-6">
              Upload a PDF, JPG or PNG and receive an easy‑to‑understand summary with AI‑powered explanations.
            </p>
            <Link
              to="/dashboard"
              className="inline-block bg-teal-600 hover:bg-teal-700 text-white font-semibold px-6 py-3 rounded-md transition"
            >
              Get Started
            </Link>
          </div>
          {/* Image side (placeholder) */}
          <div className="md:w-1/2 mt-8 md:mt-0 flex justify-center">
            <img
              src="/src/assets/hero-placeholder.png"
              alt="Report illustration"
              className="w-80 h-auto rounded-lg shadow-md"
            />
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="bg-gray-50 py-12">
        <div className="max-w-6xl mx-auto grid gap-8 md:grid-cols-3 px-6">
          <div className="bg-white rounded-xl shadow p-6 text-center">
            <h3 className="text-xl font-semibold mb-2 text-indigo-600">Fast OCR</h3>
            <p className="text-gray-600 text-sm">Extract text from PDFs and images instantly.</p>
          </div>
          <div className="bg-white rounded-xl shadow p-6 text-center">
            <h3 className="text-xl font-semibold mb-2 text-indigo-600">AI Explanations</h3>
            <p className="text-gray-600 text-sm">Gemini turns medical values into plain‑language explanations.</p>
          </div>
          <div className="bg-white rounded-xl shadow p-6 text-center">
            <h3 className="text-xl font-semibold mb-2 text-indigo-600">Educational Use Only</h3>
            <p className="text-gray-600 text-sm">Clear disclaimer – not medical advice.</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 py-4">
        <div className="max-w-6xl mx-auto text-center text-gray-500 text-sm">
          © {new Date().getFullYear()} ReportSaathi – Educational use only.
        </div>
      </footer>
    </div>
  );
}

export default Landing;
