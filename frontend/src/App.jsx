import React from 'react';

const CATEGORIES = [
  { id: 'water_supply', name: 'Water Supply', icon: '💧' },
  { id: 'road_damage', name: 'Road Damage', icon: '🚧' },
  { id: 'garbage', name: 'Garbage Disposal', icon: '🗑️' },
  { id: 'drainage', name: 'Drainage & Sewage', icon: '🌊' },
  { id: 'streetlight', name: 'Streetlight', icon: '💡' },
  { id: 'other', name: 'Other Grievance', icon: '📋' },
];

export default function App() {
  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Top Header */}
      <header
        style={{
          borderBottom: '1px solid var(--border-color)',
          padding: '1.25rem 2rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          backdropFilter: 'blur(12px)',
          position: 'sticky',
          top: 0,
          zIndex: 10,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <div
            style={{
              width: 38,
              height: 38,
              borderRadius: 'var(--radius-md)',
              background: 'var(--accent-gradient)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontWeight: 800,
              fontSize: '1.2rem',
            }}
          >
            CP
          </div>
          <div>
            <h1 style={{ fontSize: '1.1rem', fontWeight: 700, letterSpacing: '-0.02em' }}>
              CivicPulse
            </h1>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              Multilingual & Code-Mixed Grievance Redressal
            </p>
          </div>
        </div>
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
          <span
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.4rem',
              padding: '0.35rem 0.75rem',
              borderRadius: 'var(--radius-full)',
              background: 'rgba(16, 185, 129, 0.1)',
              color: 'var(--status-success)',
              fontSize: '0.75rem',
              fontWeight: 600,
              border: '1px solid rgba(16, 185, 129, 0.2)',
            }}
          >
            ● Setup Ready
          </span>
        </div>
      </header>

      {/* Main Container */}
      <main style={{ maxWidth: 960, margin: '3rem auto', padding: '0 1.5rem', flex: 1 }}>
        <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
          <span
            style={{
              display: 'inline-block',
              padding: '0.4rem 0.9rem',
              borderRadius: 'var(--radius-full)',
              background: 'rgba(99, 102, 241, 0.1)',
              color: 'var(--accent-primary)',
              fontSize: '0.8rem',
              fontWeight: 600,
              marginBottom: '1rem',
              border: '1px solid rgba(99, 102, 241, 0.25)',
            }}
          >
            College Capstone Project
          </span>
          <h2
            style={{
              fontSize: '2.25rem',
              fontWeight: 800,
              lineHeight: 1.2,
              marginBottom: '1rem',
              letterSpacing: '-0.03em',
            }}
          >
            Intelligent Public-Service Complaints Redressal
          </h2>
          <p
            style={{
              color: 'var(--text-muted)',
              maxWidth: 650,
              margin: '0 auto',
              fontSize: '1rem',
            }}
          >
            Empowering citizens to report municipal grievances in their natural language—whether
            English, regional vernacular, or Romanized code-mixed text.
          </p>
        </div>

        {/* Categories Grid */}
        <section style={{ marginBottom: '3rem' }}>
          <h3
            style={{
              fontSize: '1rem',
              textTransform: 'uppercase',
              letterSpacing: '0.08em',
              color: 'var(--text-subtle)',
              marginBottom: '1rem',
            }}
          >
            Supported Complaint Categories
          </h3>
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))',
              gap: '1rem',
            }}
          >
            {CATEGORIES.map((cat) => (
              <div
                key={cat.id}
                style={{
                  background: 'var(--bg-secondary)',
                  border: '1px solid var(--border-color)',
                  borderRadius: 'var(--radius-md)',
                  padding: '1.25rem 1rem',
                  textAlign: 'center',
                }}
              >
                <div style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>{cat.icon}</div>
                <div style={{ fontSize: '0.9rem', fontWeight: 600 }}>{cat.name}</div>
                <div
                  style={{
                    fontSize: '0.7rem',
                    color: 'var(--text-subtle)',
                    marginTop: '0.25rem',
                    fontFamily: 'monospace',
                  }}
                >
                  {cat.id}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Roles Allocation Card */}
        <section
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
            gap: '1.5rem',
          }}
        >
          <div
            style={{
              background: 'var(--bg-secondary)',
              border: '1px solid var(--border-color)',
              borderRadius: 'var(--radius-lg)',
              padding: '1.5rem',
            }}
          >
            <h4
              style={{
                color: 'var(--accent-secondary)',
                fontSize: '1.1rem',
                marginBottom: '0.5rem',
              }}
            >
              Member 1: NLP Engine
            </h4>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', lineHeight: 1.6 }}>
              Code-mixed preprocessing, Indic language identification, zero-shot/fine-tuned classification,
              extractive summarization, and semantic duplicate detection.
            </p>
          </div>

          <div
            style={{
              background: 'var(--bg-secondary)',
              border: '1px solid var(--border-color)',
              borderRadius: 'var(--radius-lg)',
              padding: '1.5rem',
            }}
          >
            <h4
              style={{
                color: 'var(--accent-primary)',
                fontSize: '1.1rem',
                marginBottom: '0.5rem',
              }}
            >
              Member 2: Application & Platform
            </h4>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', lineHeight: 1.6 }}>
              FastAPI backend integration, SQLite database modeling, municipal routing engine,
              citizen grievance filing portal, and administrative triage dashboard.
            </p>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer
        style={{
          borderTop: '1px solid var(--border-color)',
          padding: '1.5rem 2rem',
          textAlign: 'center',
          color: 'var(--text-subtle)',
          fontSize: '0.8rem',
        }}
      >
        A Multilingual and Code-Mixed NLP Framework for Public-Service Complaints • Initial Setup Complete
      </footer>
    </div>
  );
}
