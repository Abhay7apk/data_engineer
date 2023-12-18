import React, { useState, useEffect } from 'react';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/items")
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  return (
    <div>
      {items.map(item => (
        <div key={item.id}>
          {item.name} - {item.quantity}
        </div>
      ))}
    </div>
  );
}

export default App;
