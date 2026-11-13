import React from 'react';
import { useNavigate } from 'react-router-dom';

function Result() {
  const navigate = useNavigate();
  const stored = sessionStorage.getItem('reportResult');
  const result = stored ? JSON.parse(stored) : null;

  if (!result) {
    return (
      <section className="max-w-2xl mx-auto p-6">
        <p className="text-gray-600">No report data found. Please upload a report first.</p>
        <button
          onClick={() => navigate('/dashboard')}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded"
        >
          Go to Upload
        </button>
      </section>
    );
  }

  const { extractedValues, explanation, disclaimer } = result;

  return (
    <section className="max-w-2xl mx-auto p-6">
      <h2 className="text-2xl font-semibold mb-4 text-gray-800">Report Results</h2>
      <div className="mb-4">
        <h3 className="text-xl font-medium mb-2">Extracted Values</h3>
        <ul className="list-disc list-inside">
          {Object.entries(extractedValues).map(([k, v]) => (
            <li key={k}>
              <strong>{k}:</strong> {v}
            </li>
          ))}
        </ul>
      </div>
      <div className="mb-4">
        <h3 className="text-xl font-medium mb-2">Explanation</h3>
        <p>{explanation}</p>
      </div>
      <div className="text-sm text-gray-500 border-t pt-2">
        <p>{disclaimer}</p>
      </div>
    </section>
  );
}

export default Result;
