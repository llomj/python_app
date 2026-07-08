export interface Exercise { id: number; title: string; description: string; descriptionFr?: string; initialCode: string; solution: string; hint: string; category: string; breakdown?: string; }
export interface Stats { shots: number; success: number; failed: number; }
