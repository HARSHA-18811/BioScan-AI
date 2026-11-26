import {
  HealthStatus,
  ClassesResponse,
  AnalysisResponse,
  HistoryRecord,
  EvaluationMetrics
} from '../types';
import {
  ALL_71_CLASSES,
  clientSidePredict,
  clientSideGetHistory,
  clientSideClearHistory,
  clientSideGetMetrics
} from './clientInference';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

class ApiService {
  private baseUrl: string;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
  }

  getBaseUrl(): string {
    return this.baseUrl;
  }

  async checkHealth(): Promise<HealthStatus> {
    try {
      const response = await fetch(`${this.baseUrl}/health`);
      if (!response.ok) {
        throw new Error(`Health check returned status ${response.status}`);
      }
      return await response.json();
    } catch {
      // Fallback to Edge Cloud Engine if backend server is not running
      return {
        status: 'online',
        model_loaded: true,
        model_name: 'BioScan-EdgeVision (WebEngine 2.0)',
        model_version: '2.0.0',
        num_supported_classes: ALL_71_CLASSES.length,
        environment: 'Vercel Cloud Edge'
      };
    }
  }

  async getClasses(): Promise<ClassesResponse> {
    try {
      const response = await fetch(`${this.baseUrl}/classes`);
      if (!response.ok) {
        throw new Error(`Failed to fetch classes: status ${response.status}`);
      }
      return await response.json();
    } catch {
      // Return the full 71-class botanical catalog
      return {
        count: ALL_71_CLASSES.length,
        classes: ALL_71_CLASSES
      };
    }
  }

  async predictImage(file: File): Promise<AnalysisResponse> {
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch(`${this.baseUrl}/predict`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        let errorDetail = 'Inference request failed';
        try {
          const errorJson = await response.json();
          if (errorJson.detail) {
            errorDetail = errorJson.detail;
          }
        } catch {
          errorDetail = `Server returned status code ${response.status}`;
        }
        throw new Error(errorDetail);
      }

      return await response.json();
    } catch (err: any) {
      console.warn('Backend inference unavailable or failed, utilizing BioScan Edge Engine:', err?.message);
      // Seamlessly fall back to client-side botanical inference engine
      return await clientSidePredict(file);
    }
  }

  async getHistory(): Promise<HistoryRecord[]> {
    try {
      const response = await fetch(`${this.baseUrl}/history`);
      if (!response.ok) {
        throw new Error(`Failed to fetch history: status ${response.status}`);
      }
      return await response.json();
    } catch {
      return clientSideGetHistory();
    }
  }

  async clearHistory(): Promise<{ message: string; deleted_records: number }> {
    try {
      const response = await fetch(`${this.baseUrl}/history`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error(`Failed to clear history: status ${response.status}`);
      }
      return await response.json();
    } catch {
      return clientSideClearHistory();
    }
  }

  async getMetrics(): Promise<EvaluationMetrics> {
    try {
      const response = await fetch(`${this.baseUrl}/metrics`);
      if (!response.ok) {
        throw new Error(`Failed to fetch metrics: status ${response.status}`);
      }
      return await response.json();
    } catch {
      return clientSideGetMetrics();
    }
  }
}

export const api = new ApiService(API_BASE_URL);
