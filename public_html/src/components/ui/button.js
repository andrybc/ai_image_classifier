import React from 'react';

export function Button({ onClick, className, children }) {
    return (
        <button onClick={onClick} className={className}>
            {children}
        </button>
    );
}
