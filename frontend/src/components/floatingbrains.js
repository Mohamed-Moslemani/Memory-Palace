import React from 'react';
import brain from '../assets/images/brain.svg';

const FloatingBrains = () => {
  const numBrains = 15; 
  const brains = Array.from({ length: numBrains });

  return (
    <div className="absolute inset-0 overflow-hidden z-0 pointer-events-none">
      {brains.map((_, index) => {
        const size = 30 + Math.random() * 50; // Random size between 30 and 80px
        const left = Math.random() * 100; // Random left position (0% to 100%)
        const delay = Math.random() * -20; // Random animation delay (-20s to 0s)
        const duration = 20 + Math.random() * 20; // Random duration between 20s and 40s

        return (
          <img
            key={index}
            src={brain}
            alt="Floating Brain"
            className="pointer-events-none" 
            style={{
              position: 'absolute',
              width: `${size}px`,
              height: 'auto',
              left: `${left}%`,
              animation: `floatUp ${duration}s linear infinite`,
              animationDelay: `${delay}s`,
              bottom: '-100px', 
            }}
          />
        );
      })}
    </div>
  );
};

export default FloatingBrains;
