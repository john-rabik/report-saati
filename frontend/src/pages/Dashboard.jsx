import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { SAMPLE_RESULT } from '../sampleData';

function Dashboard() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const validateFile = (f) => {
    const allowed = ['application/pdf', 'image/jpeg', 'image/png'];
    if (!allowed.includes(f.type)) return 'Unsupported file type.';
    const maxSize = 5 * 1024 * 1024; // 5 MB
    if (f.size > maxSize) return 'File exceeds 5 MB size limit.';
    return '';
  };

  const handleChange = (e) => {
    const selected = e.target.files[0];
    if (!selected) return;
    const msg = validateFile(selected);
    if (msg) {
      setError(msg);
      setFile(null);
    } else {
      setError('');
      setFile(selected);
    }
  };

  const handleSubmit = async () => {
    if (!file) return;
    setLoading(true);
    // Simulate async processing (OCR + AI) using a short timeout
    setTimeout(() => {
      // Store simulated result in sessionStorage for the Result page
      sessionStorage.setItem('reportResult', JSON.stringify(SAMPLE_RESULT));
      setLoading(false);
      navigate('/result');
    }, 1500);
  };

  return (
    <section className="max-w-2xl mx-auto p-6">
      <h2 className="text-2xl font-semibold mb-4 text-gray-800">Upload Report</h2>
      <input
        type="file"
        accept=".pdf,.jpg,.jpeg,.png"
        onChange={handleChange}
        className="border rounded p-2 w-full mb-2"
      />
      {error && <p className="text-red-600 mb-2">{error}</p>}
      <button
        onClick={handleSubmit}
        disabled={!file || loading}
        className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
      >
        {loading ? 'Processing…' : 'Analyze Report'}
      </button>
    </section>
  );
}

export default Dashboard;
