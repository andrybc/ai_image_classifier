import React from 'react';

export function FileInput({ id, onChange, className }) {
    return (
        <input
            type="file"
            id={id}
            onChange={onChange}
            className={className}
        />
    );
}
