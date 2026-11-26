import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { HomePage } from './pages/HomePage';
import { AnalysisPage } from './pages/AnalysisPage';
import { ResultsPage } from './pages/ResultsPage';
import { ResearchDashboard } from './pages/ResearchDashboard';
import { MethodologyPage } from './pages/MethodologyPage';
import { AboutPage } from './pages/AboutPage';
import { api } from './services/api';
import { AnalysisResponse, HealthStatus } from './types';

export const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<string>('home');
  const [activeResult, setActiveResult] = useState<AnalysisResponse | null>(null);
  const [health, setHealth] = useState<HealthStatus | null>(null);

  // Check backend health on mount
  useEffect(() => {
    const fetchHealth = async () => {
      try {
        const h = await api.checkHealth();
        setHealth(h);
      } catch (err) {
        console.warn('Backend currently offline or unreachable:', err);
        setHealth(null);
      }
    };
    fetchHealth();
    const interval = setInterval(fetchHealth, 15000); // periodic status check
    return () => clearInterval(interval);
  }, []);

  const handleAnalysisComplete = (result: AnalysisResponse) => {
    setActiveResult(result);
    setActiveTab('results');
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#0a0f1d] text-slate-100 selection:bg-teal-500 selection:text-white">
      {/* Navigation */}
      <Navbar 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
        health={health}
        hasResult={activeResult !== null}
      />

      {/* Main Content Area */}
      <main className="flex-1">
        {activeTab === 'home' && (
          <HomePage 
            onStartAnalysis={() => setActiveTab('analysis')} 
            onExploreResearch={() => setActiveTab('methodology')} 
          />
        )}

        {activeTab === 'analysis' && (
          <AnalysisPage 
            health={health} 
            onAnalysisComplete={handleAnalysisComplete}
          />
        )}

        {activeTab === 'results' && (
          <ResultsPage 
            result={activeResult} 
            onAnalyseAnother={() => setActiveTab('analysis')}
            onViewResearch={() => setActiveTab('dashboard')}
          />
        )}

        {activeTab === 'dashboard' && (
          <ResearchDashboard health={health} />
        )}

        {activeTab === 'methodology' && (
          <MethodologyPage />
        )}

        {activeTab === 'about' && (
          <AboutPage />
        )}
      </main>

      {/* Footer */}
      <Footer />
    </div>
  );
};

export default App;
