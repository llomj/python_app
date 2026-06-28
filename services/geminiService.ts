import { GoogleGenAI } from "@google/genai";
export async function getAiHint(desc: string, code: string, apiKey: string): Promise<string> {
  const ai = new GoogleGenAI({ apiKey });
  try {
    const res = await ai.models.generateContent({ model: 'gemini-2.0-flash', contents: "Analyze: " + desc + "\n" + code });
    return res.text || "Try again!";
  } catch (e) { return "Error: " + e.message; }
}
