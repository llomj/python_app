import { GoogleGenAI } from "@google/genai";
export async function getAiHint(desc: string, code: string): Promise<string> {
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
  try {
    const res = await ai.models.generateContent({ model: 'gemini-3-pro-preview', contents: "Analyze: " + desc + "\n" + code });
    return res.text || "Try again!";
  } catch (e) { return "Error: " + e.message; }
}
