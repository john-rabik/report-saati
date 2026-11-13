import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Landing from "./pages/Landing";
import Dashboard from "./pages/Dashboard";
import Result from "./pages/Result";

function App() {
  return (
    <Router>
      {/* ==== Fixed top navigation ==== */}
      <nav className="bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-5xl mx-auto flex items-center justify-between px-4 py-3">
          <Link to="/" className="text-2xl font-bold text-blue-600">
            ReportSaathi
          </Link>
          <div className="space-x-4">
            <Link
              to="/"
              className="text-gray-700 hover:text-blue-600 transition"
            >
              Home
            </Link>
            <Link
              to="/dashboard"
              className="text-gray-700 hover:text-blue-600 transition"
            >
              Upload
            </Link>
          </div>
        </div>
      </nav>

      {/* ==== Page content ==== */}
      <main className="bg-gray-50 min-h-screen pt-6 pb-12">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/result" element={<Result />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
