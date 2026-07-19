import React from 'react';
import ReactDOM from 'react-dom/client';

const startLocalPython = () => {
  if (window.__PYODIDE_INSTANCE__) return Promise.resolve(window.__PYODIDE_INSTANCE__);
  if (window.__PYODIDE_BOOT_PROMISE__) return window.__PYODIDE_BOOT_PROMISE__;

  window.__PYODIDE_INIT_LOCK__ = true;
  window.__PYODIDE_BOOT_PROMISE__ = (async () => {
    let retries = 0;
    while (typeof window.loadPyodide === 'undefined' && retries < 120) {
      await new Promise(resolve => window.setTimeout(resolve, 250));
      retries += 1;
    }
    if (typeof window.loadPyodide === 'undefined') {
      throw new Error('Local Python runtime is unavailable. Please refresh.');
    }

    const pyodide = await window.loadPyodide({
      indexURL: new URL('./pyodide/', window.location.href).href,
    });
    await pyodide.loadPackage([]);
    window.__PYODIDE_INSTANCE__ = pyodide;
    return pyodide;
  })();

  return window.__PYODIDE_BOOT_PROMISE__;
};

// Python and the large editor/curriculum bundle load concurrently on mobile.
startLocalPython().catch(() => undefined);

class AppErrorBoundary extends React.Component<{ children: React.ReactNode }, { error: Error | null }> {
  constructor(props: { children: React.ReactNode }) {
    super(props);
    this.state = { error: null };
  }

  static getDerivedStateFromError(error: Error) {
    return { error };
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    console.error('App render failed:', error, info);
  }

  clearCacheAndReload = async () => {
    try {
      if ('caches' in window) {
        const keys = await caches.keys();
        await Promise.all(keys.map(key => caches.delete(key)));
      }
      if ('serviceWorker' in navigator) {
        const registrations = await navigator.serviceWorker.getRegistrations();
        await Promise.all(registrations.map(registration => registration.unregister()));
      }
    } catch (error) {
      console.error('Crash recovery cache clear failed:', error);
    }

    const nextUrl = new URL(window.location.href);
    nextUrl.searchParams.set('reset-cache', Date.now().toString());
    window.location.replace(nextUrl.toString());
  };

  render() {
    if (!this.state.error) return this.props.children;

    return (
      <div style={{
        minHeight: '100vh',
        background: '#050c18',
        color: '#ffffff',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 24,
        textAlign: 'center',
        fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif'
      }}>
        <div style={{ maxWidth: 420, width: '100%' }}>
          <h1 style={{ fontSize: 18, letterSpacing: 1, textTransform: 'uppercase' }}>App Recovery</h1>
          <p style={{ color: '#cbd5e1', lineHeight: 1.6 }}>
            The app hit a startup error. Clear the cached app files and reload.
          </p>
          <button
            onClick={this.clearCacheAndReload}
            style={{
              marginTop: 16,
              width: '100%',
              border: '1px solid rgba(255,255,255,0.12)',
              borderRadius: 16,
              background: '#2563eb',
              color: '#ffffff',
              padding: '14px 18px',
              fontWeight: 900,
              letterSpacing: 1,
              textTransform: 'uppercase'
            }}
          >
            Clear Cache & Reload
          </button>
          <pre style={{
            marginTop: 16,
            padding: 12,
            borderRadius: 12,
            background: 'rgba(15,23,42,0.82)',
            color: '#fca5a5',
            textAlign: 'left',
            whiteSpace: 'pre-wrap',
            overflowX: 'auto',
            fontSize: 11
          }}>{this.state.error.message}</pre>
        </div>
      </div>
    );
  }
}

const rootElement = document.getElementById('root');
if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  import('./App')
    .then(({ default: App }) => {
      root.render(
        <AppErrorBoundary>
          <App />
        </AppErrorBoundary>
      );
    })
    .catch(error => {
      root.render(
        <AppErrorBoundary>
          <StartupFailure error={error instanceof Error ? error : new Error(String(error))} />
        </AppErrorBoundary>
      );
    });
}

function StartupFailure({ error }: { error: Error }) {
  throw error;
}
