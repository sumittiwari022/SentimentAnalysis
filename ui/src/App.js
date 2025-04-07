import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('/api/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    const data = await response.json();
    setSentiment(data.sentiment);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Sentiment Analysis</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text here..."
          rows="5"
          cols="50"
        />
        <br />
        <button type="submit">Predict Sentiment</button>
      </form>
      {sentiment && <h3>Sentiment: {sentiment}</h3>}
    </div>
  );
}

export default App;
