import { EditorView } from '@codemirror/view';
import { HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { tags as t } from '@lezer/highlight';
export const editorUiTheme = EditorView.theme({ "&": { backgroundColor: "#050c18 !important", fontSize: "14px", height: "100%", color: "#ffffff" }, ".cm-gutters": { backgroundColor: "#050c18 !important", color: "#2d4a77", border: "none" } }, { dark: true });
export const pythonHighlightStyle = HighlightStyle.define([
  { tag: t.comment, color: "#858585" },        // Gray comments
  { tag: t.keyword, color: "#389EDB" },        // Blue keywords (if, for, def, etc.)
  { tag: t.variableName, color: "#FF1900" },   // Red variables only
  { tag: t.name, color: "#ffffff" },           // White for other names
  { tag: t.number, color: "#FF00FF" },         // Magenta numbers
  { tag: t.string, color: "#00AD89" }          // Teal strings
]);

export const customPythonTheme = [editorUiTheme, syntaxHighlighting(pythonHighlightStyle)];
